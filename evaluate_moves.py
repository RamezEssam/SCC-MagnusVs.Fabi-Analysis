from stockfish import Stockfish
import pandas as pd
import sys
from tqdm import tqdm


def evaluate_games(file):
    game_moves = pd.read_csv(file)
    game_moves['eval_type_white'] = None
    game_moves['eval_type_black'] = None
    game_moves['eval_after_white'] = None
    game_moves['eval_after_black'] = None
    game_ids = game_moves['game_id'].unique()

    for game_id in tqdm(game_ids):
        stockfish = Stockfish(
            r"C:\Users\ramez\stockfish_15.1_win_x64_popcnt\stockfish-windows-2022-x86-64-modern.exe",
            depth=18,
            parameters={"Threads": 2, "UCI_Elo": 3000})
        df = game_moves.loc[game_moves.game_id == game_id]
        df_dict = df.to_dict('records')
        i = 0
        for row in df_dict:
            stockfish.make_moves_from_current_position([row['white_move']])
            eval = stockfish.get_evaluation()
            df.iloc[i, 5] = eval['type']
            df.iloc[i, 7] = eval['value']

            stockfish.make_moves_from_current_position([row['black_move']])
            eval = stockfish.get_evaluation()
            df.iloc[i, 6] = eval['type']
            df.iloc[i, 8] = eval['value']

            i += 1
        game_moves.loc[game_moves.game_id == game_id, 'eval_type_white'] = df['eval_type_white']
        game_moves.loc[game_moves.game_id == game_id, 'eval_type_black'] = df['eval_type_black']
        game_moves.loc[game_moves.game_id == game_id, 'eval_after_white'] = df['eval_after_white']
        game_moves.loc[game_moves.game_id == game_id, 'eval_after_black'] = df['eval_after_black']

    print(game_moves[['white_move', 'black_move', 'eval_after_white', 'eval_after_black']].head(10))
    game_moves.to_csv(file)


if __name__ == '__main__':
    evaluate_games(sys.argv[1])
