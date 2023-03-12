from Settings import *
from Combat import Combat
from Game import Game

screen = pygame.display.set_mode(window_size)
game = Game(screen)

while True:
    game.check_events()
    game.draw_self()
    pygame.display.update()
