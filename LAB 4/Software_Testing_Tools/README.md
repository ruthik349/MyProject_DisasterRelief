# LAB 4 — Software Testing Tools: Fruit Catcher

The corrected Pygame Fruit Catcher project is in [Fruit_Catcher](Fruit_Catcher/). The original starter/fork is [ruthik349/64_fruit_catcher](https://github.com/ruthik349/64_fruit_catcher).

## Fix in the consolidated copy
- Catching a fruit awards one point.
- A fruit that reaches the floor deducts one life and awards no points.
- When lives reach zero, the game enters `GAME_OVER` and stops updating.
- Pressing R on the Game Over screen restarts the game.

Run from inside `Fruit_Catcher`:
```bash
pip install pygame
python main.py
```

See [Evidence_Links.md](Fruit_Catcher/Evidence_Links.md) for the before/after gameplay video links in [SE-DEMO](https://github.com/ruthik349/SE-DEMO). Those external videos have not been copied into this repository; verify they show the same Fruit Catcher task before submission.
