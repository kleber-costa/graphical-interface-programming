# Pomodoro Timer

A simple Pomodoro timer application implemented in Python using Tkinter.

## Overview

This project provides a graphical Pomodoro timer with an order of work and break periods. The timer cycles through Pomodoro, Short Break, Pomodoro, Short Break, Pomodoro, and Long Break. Users can adjust the length of each period in the Settings view.

## Requirements

- Python 3.x
- Tkinter (usually included with the standard Python installation)

## How to run

1. Open a terminal in the `pomodoro` folder.
2. Run:

```bash
python app.py
```

## How to use

- Click `Start` to begin the current timer.
- Click `Stop` to pause the timer.
- Click `Reset` to stop the timer and return to the first Pomodoro period.
- Click `Settings` to adjust the Pomodoro, Short Break, and Long Break durations.
- In Settings, use the spinboxes to choose the desired time values, then click `← Back` to return to the timer.

## Interface and behavior

- The main window displays the current timer type and the remaining time.
- The timer automatically advances to the next period when the countdown reaches `00:00`.
- The timer order is:
  - Pomodoro
  - Short Break
  - Pomodoro
  - Short Break
  - Pomodoro
  - Long Break
- After the long break is complete, the cycle restarts from the beginning.

## Project structure

- `app.py` - Main application entry point and frame controller.
- `frames/settings.py` - Settings screen for adjusting timer durations.
- `frames/timer.py` - Timer screen with countdown controls and period switching.
- `frames/__init__.py` - Package initializer for frame modules.

## Notes

- The application uses `ttk` widgets with the `clam` theme.
- Default values are 25 minutes for Pomodoro, 5 minutes for Short Break, and 10 minutes for Long Break.
- Customize the timer values directly in the Settings screen before starting the timer.
