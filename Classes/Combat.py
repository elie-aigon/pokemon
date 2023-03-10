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
        self.enemi = Pokemon(7, pos_combat_enemi, "enemi")
        self.enemi_stats = Stats(pos_stats_enemi, self.enemi, False)
        self.player = Pokemon(4, pos_combat_player, "player")
        self.player_stats = Stats(pos_stats_player, self.player, True)
        self.actioncombat = ActionCombat(self.player, self.enemi)


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
        self.actioncombat.draw_self(self.surface)

# EVENT
    def check_events(self):
        # print(self.actioncombat.check_death())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.actioncombat.state == 'CHOICE':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.actioncombat.state = 'FIGHT'
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    self.actioncombat.state = 'RUN'
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.actioncombat.state = 'POKEMON'
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.actioncombat.state = 'BAG'

            elif self.actioncombat.state == 'FIGHT':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.actioncombat.player.attack(self.actioncombat.enemi, False)
                    self.actioncombat.enemi_attack()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    self.actioncombat.player.attack(self.actioncombat.enemi, True)
                    self.actioncombat.enemi_attack()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.actioncombat.player.attack(self.actioncombat.enemi)
                    self.actioncombat.enemi_attack()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.actioncombat.player.attack(self.actioncombat.enemi)
                    self.actioncombat.enemi_attack()