from Settings import *
from Pokemon import Pokemon
from Stats import Stats
from ActionCombat import ActionCombat

class Combat:
    def __init__(self, surface):
        self.surface = surface
        self.load_images()
        self.init_test()

    def init_test(self):
        self.enemi = Pokemon(133, pos_combat_enemi, "enemi")
        self.enemi_stats = Stats(pos_stats_enemi, self.enemi, False)
        self.player = Pokemon(25, pos_combat_player, "player")
        self.player_stats = Stats(pos_stats_player, self.player, True)
        self.combat = ActionCombat(self.player, self.enemi)


# UI
    def load_images(self):
        self.background = pygame.image.load("Data/Images/background.png")
        self.background = pygame.transform.scale(self.background, window_size)
       

    def draw_all(self):
        self.surface.blit(self.background, (0, 0))
        self.enemi.draw_self(self.surface)
        self.enemi_stats.draw_self(self.surface)
        self.player.draw_self(self.surface)
        self.player_stats.draw_self(self.surface)
        self.combat.draw_self(self.surface)

# EVENT
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.combat.first_choice_done = True