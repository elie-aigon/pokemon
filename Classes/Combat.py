from Settings import *
from Pokemon import Pokemon
from Stats import Stats
from ActionCombat import ActionCombat

class Combat:
    def __init__(self, surface, name):
        self.surface = surface
        self.load_ressources()
        self.player = Pokemon(int(pokedex[name][0]), self.surface, "player")
        self.player_stats = Stats(pos_stats_player, self.player, "player")
        self.enemi = Pokemon(int(random.choice(pokemon_available)), self.surface, "enemi")
        self.enemi_stats = Stats(pos_stats_enemi, self.enemi, "enemi")
        self.actioncombat = ActionCombat(self.player, self.enemi)

# UI
    def load_ressources(self):
        self.background = pygame.image.load("Data/Images/background.png")
        self.background = pygame.transform.scale(self.background, window_size)
        self.messages = pygame.image.load("Data/Images/messages.png")


    def draw_all(self):
        self.surface.blit(self.background, (0, 0))
        self.enemi.draw_self(pos_combat_enemi)
        self.enemi_stats.draw_self(self.surface)
        self.player.draw_self(pos_combat_player)
        self.player_stats.draw_self(self.surface)
        self.actioncombat.draw_self(self.surface)
        self.action_death()

    def draw_death(self, message):
        self.surface.blit(self.messages, (window_size[0]//2 - self.messages.get_width()//2, window_size[1]//2 - self.messages.get_height()//2))
        self.surface.blit(message, (window_size[0]//2 - self.death_message.get_width()//2, window_size[1]//2 - self.death_message.get_height() + 20))
    
    def action_death(self):
        for pokemon in [self.player, self.enemi]:
            if pokemon.state == "KO":
                self.death_message = font_20.render(str(pokemon.getNom()) + "  est KO!", True, white)
                self.draw_death(self.death_message)
# EVENT
    def check_events(self, event):
        self.actioncombat.update_death()

        if self.actioncombat.state == 'CHOICE':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.actioncombat.state = 'FIGHT'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.actioncombat.state = 'POKEMON'

        elif self.actioncombat.state == 'FIGHT':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.actioncombat.player.attack(self.actioncombat.enemi, False)
                self.actioncombat.enemi_attack()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.actioncombat.player.attack(self.actioncombat.enemi, True)
                self.actioncombat.enemi_attack()

        elif self.actioncombat.state == "POKEMON":
            if event.type == pygame.KEYDOWN and event.key == pygame.k_a:
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.k_z:
                pass