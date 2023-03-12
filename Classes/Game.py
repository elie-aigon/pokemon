from Settings import  *
from Button import Button
from Starting import Starting
from Inventory import Inventory
from Combat import Combat

class Game:
    def __init__(self, surface):
        self.state = "Menu"
        self.surface = surface
        self.title = pygame.image.load("Data/Images/title_pokemon.png")
        self.title = pygame.transform.scale(self.title, (512, 188))
        self.background = pygame.image.load("Data/Images/menu_background.png")
        self.background = pygame.transform.scale(self.background, window_size)
        self.new_game = Button(self.surface, font_30, black, (window_size[0]//2 - 130, window_size[1]//2 - 100), 300, 80, "New Game", "green", lambda: self.new_game_command())
        self.load_game = Button(self.surface, font_30, black, (window_size[0]//2 - 130, window_size[1]//2 + 40), 300, 80, "Load Game", "green", lambda: self.load_game_command())
        self.quit_button = Button(self.surface, font_20, black, (window_size[0] - 120, window_size[1]- 70), 100, 50, "QUIT", "red", lambda: self.quit_command())
        self.starting_instruct = font_50.render("Pick your starter : ", True, white)
    # Events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # buttons check
            mouse_pos = pygame.mouse.get_pos()
            self.check_buttons_hover(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons_clicked(mouse_pos)

            if self.state == "Starting":
                if event.type == pygame.KEYDOWN:
                    if event.key in range(96, 123):
                        self.starting.name.append(chr(event.key))
                    if event.key == pygame.K_RETURN:
                        self.state = "Starting + name set"
            if self.state == "Combat":
                self.combat.check_events(event)

    def check_buttons_clicked(self, pos):
        if self.state == "Menu":
            self.new_game.is_clicked(pos)
            self.load_game.is_clicked(pos)
            self.quit_button.is_clicked(pos)
        if self.state == "Starting + name set":
            for starter in  self.starting.starter:
                if starter.is_clicked(pos):
                    self.combat = Combat(self.surface, "".join(self.starting.name))
                    self.state = "Combat"

    def check_buttons_hover(self, pos):
        if self.state == "Menu":
            self.new_game.is_hover(pos)
            self.load_game.is_hover(pos)
            self.quit_button.is_hover(pos)
        
    # UI
    def draw_self(self):
        if self.state == "Menu":
            self.surface.blit(self.background, (0, 0))
            self.surface.blit(self.title, (window_size[0]//2 - self.title.get_width()//2, 30))
            self.new_game.draw_button()
            self.load_game.draw_button()
            self.quit_button.draw_button()
        if self.state == "Starting":
            # set text
            self.starting_instruct = font_50.render("Type your name : ", True, white)
            self.name_aff = font_50.render("".join(self.starting.name), True, white)
            self.surface.blit(self.background, (0, 0))
            self.surface.blit(self.name_aff, (window_size[0]//2 - self.name_aff.get_width()//2, 200))
            self.surface.blit(self.starting_instruct, (window_size[0]//2 - self.starting_instruct.get_width()//2, 50))
        if self.state == "Starting + name set":
            self.starting_instruct = font_50.render("Pick your starter : ", True, white)
            self.surface.blit(self.background, (0, 0))
            self.surface.blit(self.starting_instruct, (window_size[0]//2 - self.starting_instruct.get_width()//2, 50))
            self.starting.draw_self()
        # if self.state == "Inventory":
        #     self.inventory_instruct = font_50.render("Inventory : ", True, white)
        #     self.surface.blit(self.background, (0, 0))
        #     self.surface.blit(self.inventory_instruct, (window_size[0]//2 - self.inventory_instruct.get_width()//2, 50))
        #     self.inventory.draw_self()
        if self.state == "Combat":
            self.combat.draw_all()
    # Commands buttons
    def new_game_command(self):
        self.starting = Starting(self.surface)
        self.state = "Starting"
 
    def load_game_command(self):
        print('bbbbbbbbbbbbbbbbbbb')

    def quit_command(self):
        sys.exit()
        pygame.quit()