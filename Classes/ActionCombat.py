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
        self.choice1 = font_20.render("ATTACK = 'A'", True, back_hp)
        self.choice2 = font_20.render("POKEMON = 'Z'", True, back_hp)

        # ATTACK
        self.attack1 = font_20.render("ATTACK Physical = 'A'", True, back_hp)
        self.attack2 = font_20.render("ATTACK Special = 'Z'", True, back_hp)
        self.back = font_20.render("Escape = 'esc'", True, back_hp)


    def draw_self(self, surface):
        if self.state == "CHOICE":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.choice1, (self.pos_attack_choice[0]+ 50, self.pos_attack_choice[1]+ 30))
            surface.blit(self.choice2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ 30 ))
            
        if self.state == "FIGHT":
            surface.blit(self.rect, self.pos_attack_choice)
            surface.blit(self.attack1, (self.pos_attack_choice[0]+ 50, self.pos_attack_choice[1]+ 30))
            surface.blit(self.attack2, (self.pos_attack_choice[0] + self.rect.get_width()//2 + 30, self.pos_attack_choice[1]+ 30 ))
        if self.state == "POKEMON":
            pass
    def update_death(self):
        if self.player.getCurrentHp() <= 0:
            self.player.state = "KO"
        if self.enemi.getCurrentHp() <= 0:
            self.enemi.state = "KO"

    def enemi_attack(self):
        if random.choice([True, False]):
            self.enemi.attack(self.player, random.choice([True, False]))
