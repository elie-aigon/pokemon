from Settings import *

class Button:
    def __init__(self, surface, font , color, pos, width, height, text, background, command):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.surface = surface
        self.text_button = self.font.render(self.text, True, self.color)
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.background_normal = pygame.image.load("Data/Images/"+ background + "/"+ background + "_normal.png").convert_alpha()
        self.background_normal = pygame.transform.scale(self.background_normal, (width, height))
        self.background_hover = pygame.image.load("Data/Images/"+ background + "/"+ background + "_hover.png").convert_alpha()
        self.background_hover = pygame.transform.scale(self.background_hover, (width, height))
        self.background_clicked = pygame.image.load("Data/Images/"+ background + "/"+ background + "_clicked.png").convert_alpha()
        self.background_clicked = pygame.transform.scale(self.background_clicked, (width, height))

        self.background = self.background_normal
        self.command = command

    def draw_button(self):
        self.surface.blit(self.background, self.button_rect)
        self.surface.blit(self.text_button, (self.pos[0] + (self.width // 2) - (self.text_button.get_width() // 2), self.pos[1] + (self.height // 2) - (self.text_button.get_height() // 2) - 3))
    
    def is_clicked(self, pos):
        if self.button_rect.collidepoint(pos):
            self.background = self.background_clicked
            self.command()
    
    def is_hover(self, pos):
        if self.button_rect.collidepoint(pos):
            self.background = self.background_hover
        else:
            self.background = self.background_normal