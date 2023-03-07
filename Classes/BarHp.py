from Settings import *

class BarHp:
    def __init__(self):
        self.image = pygame.image.load("Data/Images/bar_hp.png")
        self.percent = 100
        
    def draw_self(self, surface):
        surface.blit(self.image, (0, 0))
        pygame.draw.rect(surface, green_hp, [pos_combat_enemi[0],pos_combat_enemi[1], 100, 10])
        