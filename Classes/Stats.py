from Settings import *
from BarHp import BarHp

class Stats(BarHp):
    def __init__(self, pos, pokemon, not_enemi):
        self.pos = pos
        self.not_enemi = not_enemi
        self.setBarPos(not_enemi)
        self.pokemon = pokemon
        super().__init__()
        self.image = pygame.image.load("Data/Images/stats_block.png")
        if not_enemi:
            self.image = pygame.transform.flip(self.image, True, False)
        self.name = font_1.render(str(self.pokemon.getNom()), True, back_hp)
        self.hp_aff = font_1.render(str(self.pokemon.current_hp) + "/" + str(self.pokemon.getHp()), True, back_hp)

    def draw_self(self, surface):
        surface.blit(self.image, self.pos)
        if self.not_enemi:
            surface.blit(self.name, (self.pos[0]+30, self.pos[1]+10))
            surface.blit(self.hp_aff, (self.pos_bar[0]+ 28, self.pos_bar[1] + 8))
        else:
            surface.blit(self.name, (self.pos[0]+12, self.pos[1]+10))
            surface.blit(self.hp_aff, (self.pos_bar[0] + 28, self.pos_bar[1] + 8))
        super().draw_self(surface, self.pos_bar, self.pokemon.current_hp, self.pokemon.getHp())

    def setBarPos(self, not_enemi):
        if not_enemi:
            self.pos_bar = (730, 630)
        else:
            self.pos_bar = (610, 180)

    def update_stats(self):
        self.hp_aff = font_1.render(str(self.pokemon.current_hp) + "/" + str(self.pokemon.getHp()), True, back_hp)