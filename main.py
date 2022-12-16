import requests
import re
import chess.pgn
import io
import csv
import sys


def get_games(player, year, month):
    games_file = open(f'{player}-games-{year}-{month}.csv', 'a', newline='')
    moves_file = open(f'{player}-moves-{year}-{month}.csv', 'a', newline='')
    games_writer = csv.writer(games_file)
    games_writer.writerow(
        [
            'game_id',
            'game_date',
            'white_player',
            'black_player',
            'white_elo',
            'black_elo',
            'opening_id',
            'opening',
            'result',
            'termination',
            'time_control',
            'time_class',
            'variant',
            'rated',
            'white_accuracy',
            'black_accuracy',
        ]
    )

    moves_writer = csv.writer(moves_file)
    moves_writer.writerow(
        [
            'game_id',
            'white_move',
            'black_move',
            'white_clock',
            'black_clock',
        ]
    )

    response = requests.get(f"https://api.chess.com/pub/player/{player}/games/{year}/{month}")

    games = response.json()['games']

    for game in games:
        game_id = re.findall(r"\d{1,}", game['url'])[0]
        pgn = io.StringIO(game['pgn'])
        pgn = chess.pgn.read_game(pgn)
        game_date = pgn.headers.get('Date')
        white_player = pgn.headers.get('White')
        black_player = pgn.headers.get('Black')
        white_elo = pgn.headers.get('WhiteElo')
        black_elo = pgn.headers.get('BlackElo')
        opening_id = pgn.headers.get('ECO')
        opening = pgn.headers.get('ECOUrl')[31:]
        result = pgn.headers.get('Result')
        termination = pgn.headers.get('Termination')
        time_control = game.get('time_control', None)
        time_class = game.get('time_class', None)
        variant =  game.get('rules', None)
        rated = game.get('rated', None)
        accuracies = game.get('accuracies')
        white_accuracy = accuracies.get('white') if accuracies else None
        black_accuracy = accuracies.get('black') if accuracies else None
        games_writer.writerow(
            [
                game_id,
                game_date,
                white_player,
                black_player,
                white_elo,
                black_elo,
                opening_id,
                opening,
                result,
                termination,
                time_control,
                time_class,
                variant,
                rated,
                white_accuracy,
                black_accuracy
            ]
        )
        moves_dict = {
            'white_moves': [],
            'white_clock_times': [],
            'black_moves': [],
            'black_clock_times': []
        }
        for move in pgn.mainline():
            if not move.turn():
                moves_dict['white_moves'].append(move.move)
                moves_dict['white_clock_times'].append(move.clock())
            else:
                moves_dict['black_moves'].append(move.move)
                moves_dict['black_clock_times'].append(move.clock())
        for move_item in zip(moves_dict['white_moves'], moves_dict['black_moves'], moves_dict['white_clock_times'], moves_dict['black_clock_times']):
            moves_writer.writerow(
                [game_id, *move_item]
            )


if __name__ == '__main__':

    get_games(sys.argv[1], sys.argv[2], sys.argv[3])



