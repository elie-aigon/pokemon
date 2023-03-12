from Settings import *
from BarHp import BarHp

class Stats(BarHp):
    def __init__(self, pos, pokemon, side):
        self.pos = pos
        self.side = side
        self.setBarPos(side)
        self.pokemon = pokemon
        super().__init__()
        self.image = pygame.image.load("Data/Images/stats_block.png")
        if side == "player":
            self.image = pygame.transform.flip(self.image, True, False)
        self.name = font_20.render(str(self.pokemon.getNom()), True, back_hp)
        self.hp_aff = font_20.render(str(self.pokemon.current_hp) + "/" + str(self.pokemon.getHp()), True, back_hp)
        self.type = pygame.image.load("Data/Images/Types/"+ self.pokemon.type+ ".png")
        self.type = pygame.transform.scale(self.type, (25, 25))

    def draw_self(self, surface):
        self.update_stats()
        surface.blit(self.image, self.pos)
        if self.side == "player":
            surface.blit(self.name, (self.pos[0]+30, self.pos[1]+10))
            surface.blit(self.hp_aff, (self.pos_bar[0]+ 28, self.pos_bar[1] + 8))
            surface.blit(self.type, (self.pos[0]+40, self.pos[1]+28))
        else:
            surface.blit(self.name, (self.pos[0]+12, self.pos[1]+10))
            surface.blit(self.hp_aff, (self.pos_bar[0] + 28, self.pos_bar[1] + 8))
            surface.blit(self.type, (self.pos[0]+22, self.pos[1]+28))
        super().draw_self(surface, self.pos_bar, self.pokemon.getCurrentHp(), self.pokemon.getHp())

    def setBarPos(self, side):
        if side == "player":
            self.pos_bar = (730, 630)
        else:
            self.pos_bar = (610, 180)

    def update_stats(self):
        self.hp_aff = font_20.render(str(self.pokemon.current_hp) + "/" + str(self.pokemon.getHp()), True, back_hp)