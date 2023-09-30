# Knights - Logic Puzzle Solver

## Overview
This project implements a logic puzzle solver for the classic "Knights and Knaves" puzzles inspired by logician Raymond Smullyan's 1978 book "What is the name of this book?". In these puzzles, each character is either a knight (who always tells the truth) or a knave (who always lies). The objective is to determine the identity of each character based on their statements.

## Puzzles
The implemented puzzles and their descriptions are as follows:

### Puzzle 0
- **Characters**: A
- **Statements**:
  - A says “I am both a knight and a knave.”

### Puzzle 1
- **Characters**: A, B
- **Statements**:
  - A says “We are both knaves.”
  - B says nothing.

### Puzzle 2
- **Characters**: A, B
- **Statements**:
  - A says “We are the same kind.”
  - B says “We are of different kinds.”

### Puzzle 3
- **Characters**: A, B, C
- **Statements**:
  - A makes an ambiguous statement.
  - B says “A said ‘I am a knave.’”
  - B then says “C is a knave.”
  - C says “A is a knight.”

## Implementation
The logic for the puzzles is represented using propositional logic constructs. The `knowledge` bases for each puzzle are populated with the information given by the puzzle's statements. Using a model-checking approach, the program determines the most likely identity (knight or knave) for each character.

## Usage
To solve the puzzles, run:
``` bash
python3 puzzle.py
```
The program will display the determined identities for each character in all the puzzles.