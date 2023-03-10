from Settings import *

class Pokemon:
    def __init__(self, id, pos, side):
        self.pos = pos
        self.setBase(id - 1)
        self.current_hp = self.__hp
        self.lvl = 1
        self.state = str()
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
        self.current_hp -= valeur

    def getCurrentHp(self):
        return self.current_hp
    def getHp(self):
        return self.__hp
    
    def attack(self, other, is_spe):
        random = 2
        if is_spe:
            spe_normal_att = self.sp_dmg
            spe_normal_def = other.sp_defense
        else:
            spe_normal_att = self.dmg
            spe_normal_def = other.defense
        if self.type+ ","+ other.type in stab_relation:
            stab = stab_relation[self.type+ ","+ other.type]
        else:
            stab = 1 // stab_relation[other.type + "," + self.type]
        print(stab)
        dmg = round((((((self.lvl * 2)//5) + 2) * self.dmg * spe_normal_att //50 // spe_normal_def) * random) * stab)
        print(dmg)
        other.setHp(dmg)
