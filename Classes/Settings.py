import pygame, sys, random, json, random

window_size = (1400, 850)
# color
green_hp = (112, 248, 168)
back_hp = (75, 78, 88)

pos_combat_enemi = (800, 300)
pos_combat_player = (300, 530)

# base stats!
with open("Data/JSON/pokemon.json", "r") as f:
    base_stats = json.load(f)