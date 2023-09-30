# Minesweeper AI

Minesweeper is a classic puzzle game where players must identify and flag all the mines on a grid without detonating any of them. This project implements an AI to play Minesweeper, intelligently identifying safe cells and mines using propositional logic.

## Game Overview

In Minesweeper, the grid contains a mix of safe cells and mines. Clicking on a mine detonates it and results in a loss. Clicking on a safe cell reveals a number indicating how many neighboring cells contain mines. The objective is to flag all mines without detonating any.

## AI Strategy

The AI uses knowledge-based agents to infer safe moves. The knowledge is based on the numbers revealed when safe cells are clicked. Each cell is treated as a propositional variable that is true if the cell contains a mine and false otherwise.

For instance, if a cell reveals the number 1, it means one of its neighbors is a mine. This can be expressed as a logical expression involving all neighboring cells. The AI makes use of such expressions and their derivatives to make inferences about safe cells and mines.

The AI's knowledge base is represented using sentences. Each sentence contains a set of cells and a count indicating how many of those cells are mines.

## Running the Game

1. Ensure you have Python 3.10 installed.
2. Install the required packages:
``` bash
pip3 install -r requirements.txt
```
3. Run the game:
``` bash
python3 runner.py
```
You can play the game yourself or let the AI make moves on your behalf!

## Understanding the Code

The project is primarily divided into two main files:
1. `runner.py`: Contains the code to run the graphical interface for the game.
2. `minesweeper.py`: Contains the game logic and the AI implementation.

The AI implementation is in the `MinesweeperAI` class inside `minesweeper.py`. This class maintains knowledge about the game board and makes inferences based on it to determine safe moves.

## Contributing

Feel free to fork this repository and make enhancements or adapt the AI for other similar games!