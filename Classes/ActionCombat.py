from Settings import *

class ActionCombat:
    def __init__(self, player, enemi):
        self.player = player
        self.enemi = enemi
        self.state = "CHOICE"
        self.load_ressources()
        self.pos_attack_choice = (window_size[0] - self.rect.get_width(), window_size[1] - self.rect.get_height())
    
    def load_ressources(self):
        self.rect = pygame.image.load("Data/Images/rect_action.png")
        self.rect = pygame.transform.scale(self.rect, (800, 170))
        self.instruc_rect = pygame.image.load("Data/Images/instruc_rect.png")
        self.instruc_rect = pygame.transform.scale(self.instruc_rect, (window_size[0] - self.rect.get_width(), 130))
        # CHOICES
        self.choice1 = font_1.render("FIGHT = 'A'", True, back_hp)
        self.choice2 = font_1.render("RUN = 'Z'", True, back_hp)
        self.choice3 = font_1.render("POKEMON = 'E'", True, back_hp)
        self.choice4 = font_1.render("BAG = 'R'", True, back_hp)
        # ATTACK
        self.attack1 = font_1.render("ATTACK 1 = 'A'", True, back_hp)
        self.attack2 = font_1.render("ATTACK SPE = 'Z'", True, back_hp)
        self.attack3 = font_1.render("ATTACK 3 = 'E'", True, back_hp)
        self.attack4 = font_1.render("ATTACK 4 = 'R'", True, back_hp)

    def draw_self(self, surface):
        surface.blit(self.instruc_rect, (0, window_size[1] - self.instruc_rect.get_height()))
        if self.state == "CHOICE":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.choice1, (self.pos_attack_choice[0]+ 50, self.pos_attack_choice[1]+ 30))
            surface.blit(self.choice2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ 30 ))
            surface.blit(self.choice3, (self.pos_attack_choice[0] + 50, self.pos_attack_choice[1] + self.rect.get_height()//2 + 20))
            surface.blit(self.choice4, (self.pos_attack_choice[0]+ self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ self.rect.get_height()//2 + 20))  
        if self.state == "FIGHT":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.attack1, (self.pos_attack_choice[0]+ 50, self.pos_attack_choice[1]+ 30))
            surface.blit(self.attack2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ 30 ))
            surface.blit(self.attack3, (self.pos_attack_choice[0] + 50, self.pos_attack_choice[1] + self.rect.get_height()//2 + 20))
            surface.blit(self.attack4, (self.pos_attack_choice[0]+ self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ self.rect.get_height()//2 + 20))
        if self.state == "RUN":
            pass
        if self.state == "POKEMON":
            pass
    
    def check_death(self):
        if self.player.getCurrentHp() <= 0:
            self.player.state = "KO"
            return self.player.getNom()
        if self.enemi.getCurrentHp() <= 0:
            self.enemi.state = "KO"
            return self.enemi.getNom()

    def enemi_attack(self):
        a = random.choice([True, False])
        print(a)
        self.enemi.attack(self.player, a)
