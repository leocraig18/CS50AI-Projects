# Tic-Tac-Toe AI

An optimal Tic-Tac-Toe AI implemented using the Minimax algorithm.

## Overview

This project involves an AI that can play Tic-Tac-Toe without losing, using the Minimax algorithm. Given optimal play from the opponent, the game should always result in a tie.

## Technical Details

- **Language**: Python (up to version 3.10)
- **Libraries**: `pygame`
- **Key Files**: 
  - `runner.py`: Provides the graphical interface for the game.
  - `tictactoe.py`: Contains the game logic and Minimax AI implementation.

## Features

- **Optimal AI Player**: Uses the Minimax algorithm to make the best possible move.
- **Graphical Interface**: Play interactively against the AI.
- **No Loss Guarantee**: Given optimal play by the human player, the AI will never lose.

## How to Play

1. Ensure the required Python package (`pygame`) is installed:
 ```bash
 pip3 install -r requirements.txt
 ```
1. Run the game using:
```bash
python3 runner.py
```

Play your moves on the grid and try to beat the AI (or at least achieve a tie)!