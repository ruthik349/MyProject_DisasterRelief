# Fruit Catcher — Lab 4 Software Testing

This is the student's consolidated copy of the assigned Pygame Fruit Catcher project.

## Fix in this copy
- Catching a fruit adds 1 point.
- Missing a fruit reduces lives by 1 and does not add points.
- At 0 lives, the game enters `GAME_OVER` and stops updating.
- Press `R` on the Game Over screen to restart.

## Run
```bash
pip install pygame
python main.py
```

## Behavior checks
Run `python verify_game.py` from this folder. The checks cover catch scoring, missed fruit and life loss, game over and stopped updates, and restart behavior. Test output is in [the Lab 4 terminal evidence file](../../evidence/terminal-test-results.txt).

The original fork [ruthik349/64_fruit_catcher](https://github.com/ruthik349/64_fruit_catcher) remains separate and unchanged. This consolidated copy contains the corrected game engine.
