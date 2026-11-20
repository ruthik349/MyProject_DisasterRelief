import pygame
from game.game_engine import GameEngine
from game.fruit import Fruit

pygame.init()
pygame.display.set_mode((1, 1))
engine = GameEngine(600, 500)
engine.spawn_delay = 10**9

# Catch: fruit intersects basket after one update.
fruit = Fruit(600)
fruit.x = engine.basket.x + 10
fruit.y = engine.basket.y - 10
fruit.speed = 1
engine.fruits = [fruit]
engine.update()
assert engine.score == 1 and engine.lives == 3 and not engine.fruits
print('PASS catch awards one point')

# Miss: one life is removed and no point is awarded.
fruit = Fruit(600)
fruit.y = 502
fruit.speed = 1
engine.fruits = [fruit]
engine.update()
assert engine.score == 1 and engine.lives == 2 and not engine.fruits
print('PASS missed fruit removes one life without points')

# Final miss ends the game; later updates do not change state.
engine.lives = 1
fruit = Fruit(600)
fruit.y = 502
fruit.speed = 1
engine.fruits = [fruit]
engine.update()
assert engine.game_state == 'GAME_OVER' and engine.lives == 0 and not engine.fruits
engine.update()
assert engine.game_state == 'GAME_OVER' and engine.score == 1 and engine.lives == 0
print('PASS zero lives enters GAME_OVER and stops updates')

# Restart restores a clean game.
engine.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
assert engine.game_state == 'PLAYING' and engine.score == 0 and engine.lives == 3 and not engine.fruits
print('PASS R restarts score, lives, and fruit state')
pygame.quit()
