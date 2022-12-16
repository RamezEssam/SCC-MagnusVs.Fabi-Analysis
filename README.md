# SCC-MagnusVs.Fabi-Analysis


In December 2022, Magnus Carlsen (Current World Chess Champion) and Fabiano Caruana (Top 10 Player and a former contender to the world title) played a quarter final match in Chess.com Speed Chess Chamionships where Carlsen Defeated Caruana 22-4 without losing a single game!

This made me question what exactly happened for Magnus to defeat a world class player in such a dominating fashion? Did Caruana simply have a bad day? Was Magnus Performing at his peak level? How long did the match stay competitive? And what was Magnus' secret for winning in such a dominating fashion?

I set out to attempt to answer these questions and investigate their match by using the data.

1. Thanks to Chess.com public API, I was able to obtain all of Magnus' december games and transform them to two files:
  - magnuscarlsen-games-2022-12.csv
  - magnuscarlsen-moves-2022-12.csv
2. By using the strongest chess engine available (StockFish 15), I was able to analyze every move in all of the games to obtain the engine evaluation after every single move



## Project Files:
  1. `main.py`: this script pulls the data from chess.com public apis and creates the two csv files: games file, and moves file
  2. `evaluate_moves.py`: this script uses stockfish 15 to evaluate each move made in the moves file
  
 
### runtime requirements:

  1. [pandas](https://pandas.pydata.org/)
  2. [chess](https://python-chess.readthedocs.io/en/latest/#)
  3. [stockfish python wrapper](https://pypi.org/project/stockfish/) 
