import pygame, sys, random, json, random

window_size = (1400, 850)

pos_combat_enemi = (800, 300)
pos_combat_player = (300, 530)
# Type 
with open("Data/JSON/pokemon.json", "r") as f:
    base_stats = json.load(f)