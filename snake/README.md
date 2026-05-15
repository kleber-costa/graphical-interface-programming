# Snake

A simple Snake game implemented in Python using Tkinter.

## Overview

This project provides a graphical interface to play Snake. The snake moves on a grid, grows when it eats food, and the game ends when the snake collides with the walls or with its own body.

## Requirements

- Python 3.x
- Tkinter (usually included with the standard Python installation)

## How to run

1. Open a terminal in the `snake` folder.
2. Run:

```bash
python snake.py
```

## How to play

- Use the arrow keys to control the snake direction (↑ ↓ ← →).
- Each time the snake eats the red food, the score increases and the snake grows.
- The current score is shown at the top-left corner as "Score: X".
- The game ends if the snake touches a wall or collides with itself. When this happens, "Game Over" is displayed in the center of the window.

## Interface and behavior

- The game window uses the title "Snake Game" and is non-resizable by default.
- Food is drawn as a red oval on the grid.
- Colors, grid size and speed can be adjusted via constants at the top of `snake.py`.

## Project structure

- `snake.py` - Main game implementation using Tkinter.

## Notes

- Adjust `WIDTH`, `HEIGHT`, `GRID_SIZE`, `SPEED`, `BG_COLOR`, `SNAKE_COLOR`, and `FOOD_COLOR` in `snake.py` to customize the game.
- The game is designed for a single human player; no AI is implemented.
