from Settings import *

class Pokemon:
    def __init__(self, id, pos, side):
        self.pos = pos
        self.setBase(id - 1)
        self.image = pygame.image.load("Data/Images/" + self.type + "/" + str(id) +".png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        if not side == "enemi":
            self.image = pygame.transform.flip(self.image, True, False)
    def draw_self(self, surface):
        surface.blit(self.image, self.pos)

    def setBase(self, id):
        self.__nom = base_stats[id]["name"]["french"]
        self.type = base_stats[id]["type"]
        self.__hp = base_stats[id]["base"]["HP"]
        self.dmg = base_stats[id]["base"]["Attack"]
        self.defense = base_stats[id]["base"]["Defense"]
        self.sp_dmg = base_stats[id]["base"]["Sp. Attack"]
        self.sp_defense = base_stats[id]["base"]["Sp. Defense"]
        self.speed = base_stats[id]["base"]["Speed"]
        
    def getNom(self):
        return self.__nom

    def setHp(self, valeur):
        self.__hp = valeur

    def attaquer(self, enemi):
        enemi.setHp(self.dmg)

