from Settings import *

class Starter:
    def __init__(self, surface, id, pos, command):
        self.pos = pos
        self.surface = surface
        self.id = id
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 200, 200)
        self.image = pygame.image.load("Data/Images/Pokemon/"+ str(self.id) + ".png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.command = command
    
    def draw_self(self):
        self.surface.blit(self.image, self.pos)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.command()
            return True

     