from Settings import *
from Pokemon import Pokemon

class Combat:
    def __init__(self, surface):
        self.surface = surface
        self.load_images()
        self.init_test()

    def init_test(self):
        self.enemi = Pokemon(133, pos_combat_enemi, "enemi")
        self.player = Pokemon(4, pos_combat_player, "player")

# UI
    def load_images(self):
        self.background = pygame.image.load("Data/Images/background.png")
        self.background = pygame.transform.scale(self.background, window_size)

    def draw_all(self):
        self.surface.blit(self.background, (0, 0))
        self.enemi.draw_self(self.surface)
        self.player.draw_self(self.surface)

# EVENT
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()