# Pong

A simple Pong game implemented in Python using Tkinter.

## Overview

This project provides a graphical interface to play a two-player Pong game. Each player controls one paddle, and the game ends when the ball reaches the left or right edge of the window.

## Requirements

- Python 3.x
- Tkinter (usually included with the standard Python installation)

## How to run

1. Open a terminal in the `pong` folder.
2. Run:

```bash
python pong.py
```

## How to play

- Player 1 uses `W` and `S` to move the left paddle up and down.
- Player 2 uses the `Up` and `Down` arrow keys to move the right paddle.
- The ball bounces off the top and bottom walls and the paddles.
- The game ends when the ball passes the left or right side of the window.

## Interface and behavior

- The game window uses a black background with white paddles and ball.
- The ball starts moving from the center of the screen.
- When the game is over, the text "Game Over!" is displayed in the center of the window.

## Project structure

- `pong.py` - Main game implementation using Tkinter.

## Notes

- Adjust `WIDTH`, `HEIGHT`, `BALL_SPEED`, `PADDLE_SPEED`, and other constants at the top of `pong.py` to customize the game.
- The game is designed for local two-player play; no AI is implemented.
