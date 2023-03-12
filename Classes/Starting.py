from Settings import *
from Starter import Starter
from Pokemon import Pokemon 

class Starting:
    def __init__(self, surface):
        self.surface = surface
        self.starter = [Starter(surface, 4, (window_size[0]//3 - 100, window_size[1]//3), lambda: self.create_pokedex(4)), Starter(surface, 7, (2 * (window_size[0]//3) - 100, window_size[1]//3), lambda: self.create_pokedex(7)), Starter(surface, 25, (window_size[0]//3 - 100, 2 * (window_size[1]//3)), lambda: self.create_pokedex(25)), Starter(surface, 129, (2 * (window_size[0]//3) - 100, 2 * (window_size[1]//3)), lambda: self.create_pokedex(129))]
        self.name = []

    def draw_self(self):
        for starter in self.starter:
            starter.draw_self()

    def create_pokedex(self, id):
        pokedex["".join(self.name)] = [id]
        with open("Data/JSON/pokedex.json", "w") as f:
            json.dump(pokedex, f)
        