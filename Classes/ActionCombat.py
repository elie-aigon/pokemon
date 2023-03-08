from Settings import *

class ActionCombat:
    def __init__(self, player, enemi):
        self.player = player
        self.enemi = enemi
        self.state
        self.load_ressources()
        self.pos_attack_choice = (window_size[0] - self.rect.get_width(), window_size[1] - self.rect.get_height())
    
    def load_ressources(self):
        self.rect = pygame.image.load("Data/Images/rect_action.png")
        self.rect = pygame.transform.scale(self.rect, (800, 170))
        # CHOICES
        self.choice1 = font_1.render("FIGHT", True, back_hp)
        self.choice2 = font_1.render("RUN", True, back_hp)
        self.choice3 = font_1.render("POKEMON", True, back_hp)
        self.choice4 = font_1.render("BAG", True, back_hp)
        # ATTACK
        self.attack1 = font_1.render("ATTACK 1", True, back_hp)
        self.attack2 = font_1.render("ATTACK 2", True, back_hp)
        self.attack3 = font_1.render("ATTACK 3", True, back_hp)
        self.attack4 = font_1.render("ATTACK 4", True, back_hp)

    def draw_self(self, surface):
        if self.state == "CHOICE":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.choice1, (self.pos_attack_choice[0]+ 40, self.pos_attack_choice[1]+ 30))
            surface.blit(self.choice2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 20, self.pos_attack_choice[1]+ 30 ))
            surface.blit(self.choice3, (self.pos_attack_choice[0] + 40, self.pos_attack_choice[1] + self.rect.get_height()//2 + 20))
            surface.blit(self.choice4, (self.pos_attack_choice[0]+ self.rect.get_width()//2 + 20, self.pos_attack_choice[1]+ self.rect.get_height()//2 + 20))  
        if self.state == "FIGHT":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.attack1, (self.pos_attack_choice[0]+ 40, self.pos_attack_choice[1]+ 30))
            surface.blit(self.attack2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 20, self.pos_attack_choice[1]+ 30 ))
            surface.blit(self.attack3, (self.pos_attack_choice[0] + 40, self.pos_attack_choice[1] + self.rect.get_height()//2 + 20))
            surface.blit(self.attack4, (self.pos_attack_choice[0]+ self.rect.get_width()//2 + 20, self.pos_attack_choice[1]+ self.rect.get_height()//2 + 20))
        if self.state == "RUN":
            pass
        if self.state == "POKEMON":
            pass
    
    def calculate_interact(self, attack, ):
