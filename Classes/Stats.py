from Settings import *
from BarHp import BarHp

class Stats(BarHp):
    def __init__(self, pos):
        self.pos = pos
        super().__init__()
        self.image = pygame.image.load("Data/Images/stats_enemi.png")
