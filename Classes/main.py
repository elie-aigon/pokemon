from Settings import *
from Combat import Combat

screen = pygame.display.set_mode(window_size)
combat = Combat(screen)

while True:
    combat.check_events()
    combat.draw_all()
    pygame.display.update()

        
