# idée jeu : combatton
# c'est un jeu dial le combat

import pygame
import sys

# Initialisation donc tout ce qui est variable etc
pygame.init()
pygame.display.set_caption("America 1")
images = ["tile000.png", "tile024.png", "tile025.png"]  # Listeux dial les imagees de sprite
index = 0  # index des images
nb_frame = 0  # c simple
animation_frames = 10  # c  le nb de frame avant de changer l'animation


desktop_sizes = pygame.display.get_desktop_sizes()
screen_larg, screen_haut = desktop_sizes[0]  #

screen = pygame.display.set_mode((screen_larg, screen_haut))


background = pygame.image.load("War.png")
background = pygame.transform.scale(background, (screen_larg, screen_haut))

# la boucla
continuer = 1
while continuer == 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

    # Afficher le fond
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Nettoyage
pygame.quit()
sys.exit()
