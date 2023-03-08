from Settings import *
from BarHp import BarHp

class Stats(BarHp):
    def __init__(self, pos, pokemon, not_enemi):
        self.pos = pos
        self.setBarPos(not_enemi)
        self.pokemon = pokemon
        super().__init__()
        self.image = pygame.image.load("Data/Images/stats_block.png")
        if not_enemi:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw_self(self, surface):
        surface.blit(self.image, self.pos)
        super().draw_self(surface, self.pos_bar)

    def setBarPos(self, not_enemi):
        if not_enemi:
            self.pos_bar = (730, 630)
        else:
            self.pos_bar = (610, 180)