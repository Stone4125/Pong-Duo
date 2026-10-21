# Pong

A simple two-player Pong game built with Python's standard `turtle` module.
Control the paddles, bounce the ball, and score points when your opponent
misses.

## Requirements

- Python 3.12 or newer
- A graphical environment that supports `turtle`

No third-party packages are required.

## Run the game

Open a terminal in the project directory and run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Controls

| Player | Move up | Move down |
| --- | --- | --- |
| Right | Up Arrow | Down Arrow |
| Left | `W` | `S` |

When a player misses the ball, their opponent scores a point. Click the game
window to close it.

## Project structure

- `main.py`: sets up the window, controls, and game loop.
- `ball.py`: handles the ball's movement and bouncing.
- `paddle.py`: defines the paddles and their movement.
- `scoreboard.py`: displays and updates the score.
