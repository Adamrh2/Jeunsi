

import pygame
import sys

# Initialisation donc tout ce qui est variable etc
pygame.init()
pygame.display.set_caption("America 1")


desktop_sizes = pygame.display.get_desktop_sizes()
screen_larg, screen_haut = desktop_sizes[0]  #

screen = pygame.display.set_mode((screen_larg, screen_haut))
imagecharacter = pygame.image.load("tile000.png")
liste_animation = [
      pygame.image.load("tile024.png"),
    pygame.image.load("tile025.png"),
    pygame.image.load("tile026.png"),
    pygame.image.load("tile027.png"),
     pygame.image.load("tile028.png"),
     pygame.image.load("tile029.png"),
    pygame.image.load("tile030.png"),
    pygame.image.load("tile031.png")
]
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
