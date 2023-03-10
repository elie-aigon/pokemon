import pygame, sys, random, json, random
pygame.init()


window_size = (1400, 850)
# color
green_hp = (112, 248, 168)
back_hp = (75, 78, 88)
# font
font_1 = pygame.font.Font("Data/Font/upheavtt.ttf", 20)


pos_combat_enemi = (800, 300)
pos_stats_enemi = (500, 150)
pos_combat_player = (300, 530)
pos_stats_player = (600, 600)

# base stats!
with open("Data/JSON/pokemon.json", "r") as f:
    base_stats = json.load(f)

stab_relation = {"Feu,Feu": 0.5, "Feu,Eau": 0.5, "Feu,Normal":2, "Normal,Normal": 1, "Electric,Feu": 1, "Electric,Eau": 2, "Electric,Normal": 1, "Eau,Normal": 1, "Eau,Eau": 0.5, "Electric,Electric": 0.5}
