from Settings import *

class Inventory:
    def __init__(self, name, surface):
        self.pokedex = pokedex[name]
        self.surface = surface
        self.rect_pokedex = pygame.image.load("Data/Images/rect_action.png")
        self.rect_pokedex = pygame.transform.scale(self.rect_pokedex, (1000, 200))

    def draw_self(self):
        self.load_images()
        self.surface.blit(self.rect_pokedex, (window_size[0]//2 - self.rect_pokedex.get_width()//2, window_size[1]//2 - self.rect_pokedex.get_height()//2))
        self.surface.blit(self.pokemon_1, (200, window_size[1]//2 - self.pokemon_1.get_height()//2))
        # self.surface.blit(self.pokemon_2, (400, window_size[1]//2 - self.pokemon_1.get_height()//2))
        # self.surface.blit(self.pokemon_3, (600, window_size[1]//2 - self.pokemon_1.get_height()//2))
        # self.surface.blit(self.pokemon_4, (800, window_size[1]//2 - self.pokemon_1.get_height()//2))
            
    def load_images(self):
        self.pokemon_1 = pygame.image.load("Data/Images/Pokemon/" + str(self.pokedex[0]) + ".png")
        # self.pokemon_2 = pygame.image.load("Data/Images/Pokemon/" + str(self.pokedex[1]) + ".png")
        # self.pokemon_3 = pygame.image.load("Data/Images/Pokemon/" + str(self.pokedex[2]) + ".png")
        # self.pokemon_4 = pygame.image.load("Data/Images/Pokemon/" + str(self.pokedex[3]) + ".png")

        self.pokemon_1 = pygame.transform.scale(self.pokemon_1, (150, 150))
        # self.pokemon_2 = pygame.transform.scale(self.pokemon_2, (150, 150))
        # self.pokemon_3 = pygame.transform.scale(self.pokemon_3, (150, 150))
        # self.pokemon_4 = pygame.transform.scale(self.pokemon_4, (150, 150))
    
    def swipe_left(self):
        pass
    
    def swipe_right(self):
        pass