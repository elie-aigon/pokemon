from Settings import *

class BarHp:
    def __init__(self):
        self.bar_container = pygame.image.load("Data/Images/bar_hp.png")
        self.percent = 100
  
    def draw_self(self, surface, pos, hp_current, hp_max):
        surface.blit(self.bar_container, (pos))
        pygame.draw.rect(surface, back_hp, [pos[0] + 24,pos[1] + 2, 63, 5])
        pygame.draw.rect(surface, green_hp, [pos[0] + 24,pos[1] + 2, hp_current * 63 // hp_max, 5])
