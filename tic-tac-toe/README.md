# Tic Tac Toe

A simple Tic Tac Toe application built with Python and Tkinter.

## Overview

This project implements a graphical interface to play Tic Tac Toe between two human players. The game uses Tkinter buttons to represent the nine board cells, switches between players X and O, and detects wins or ties.

## Requirements

- Python 3.x
- Tkinter (usually included with the standard Python installation)

## How to run

1. Open a terminal in the `tic-tac-toe` folder.
2. Run:

```bash
python tic_tac_toe.py
```

## How to play

- Click an empty cell to mark it with the current player's symbol.
- The game automatically alternates between player X and player O.
- When a player wins, the application displays a message and restarts the game.
- If all cells are filled without a winner, the game displays "Tie!" and restarts.

## Project structure

- `tic_tac_toe.py` - Main game implementation using Tkinter.

## Notes

- The game does not include AI; it is intended for two human players.
- If needed, you can customize the button colors or size directly in `tic_tac_toe.py`.
