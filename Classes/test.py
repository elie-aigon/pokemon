import pygame
import moviepy.editor as mp

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Charger l'animation GIF avec moviepy
animation = mp.VideoFileClip("Data/Images/Feu/charmander.gif")

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Afficher l'animation à chaque frame
    frame = animation.get_frame(pygame.time.get_ticks() / 1000)
    surf = pygame.surfarray.make_surface(frame)
    screen.blit(surf, (0,0))
    pygame.display.flip()
