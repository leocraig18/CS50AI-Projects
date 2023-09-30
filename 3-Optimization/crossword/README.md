# Crossword Puzzle Generator

An AI-powered crossword puzzle generator built using Python. This generator can take in a list of words and generate a crossword puzzle that fits the given structure.

## Overview

The generator employs constraint satisfaction problem-solving techniques to create crossword puzzles. Given a structure of a crossword puzzle and a list of words, the program determines which words should go in each vertical or horizontal sequence of squares.

## Usage:

``` bash
python generate.py data/structure1.txt data/words1.txt output.png
```

## Features
- **Model as Constraint Satisfaction Problem (CSP)**: The problem is modeled as a CSP where each sequence of squares in the crossword represents a variable. The goal is to decide the value (word) for each variable.
- **Enforce Node Consistency**: The program ensures that every value in a variable's domain is consistent with the variable’s unary constraints.
- **Arc Consistency**: It uses the AC-3 algorithm to enforce arc consistency, ensuring that binary constraints between variables are met.
- **Backtracking Search**: The generator employs backtracking search to find a solution to the crossword puzzle. This involves recursively trying to assign values to variables and backtracking when a constraint is violated.

## How the Generator Works:
- **Unary and Binary Constraints**: The generator considers both unary constraints (like the length of words) and binary constraints (like overlapping letters between two words).
- **Node Consistency**: For each variable, every value in its domain must be consistent with the variable’s unary constraints.
- **Arc Consistency**: For any two variables that overlap, there's a constraint that the overlapping letters must be the same. The program ensures that every value in a variable's domain has a corresponding value in another overlapping variable's domain that doesn't cause a conflict.
- **Backtracking with Heuristics**: The generator uses backtracking to recursively try different word assignments for the variables. It also employs heuristics like the minimum remaining value and degree heuristic to improve the efficiency of the backtracking search.
