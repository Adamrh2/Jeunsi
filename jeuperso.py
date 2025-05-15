

import pygame
import sys

# Initialisation donc tout ce qui est variable etc
pygame.init()
pygame.display.set_caption("America 1")


desktop_sizes = pygame.display.get_desktop_sizes()
screen_larg, screen_haut = desktop_sizes[0]  #

screen = pygame.display.set_mode((screen_larg, screen_haut))
imagecharacter = pygame.image.load("img/tile000.png")
positionperso = (300,900)
liste_animation = [
      pygame.image.load("img/tile024.png"),
    pygame.image.load("img/tile025.png"),
    pygame.image.load("img/tile026.png"),
    pygame.image.load("img/tile027.png"),
     pygame.image.load("img/tile028.png"),
     pygame.image.load("img/tile029.png"),
    pygame.image.load("img/tile030.png"),
    pygame.image.load("img/tile031.png")
]
background = pygame.image.load("War.png")
background = pygame.transform.scale(background, (screen_larg, screen_haut))

def dessiner():
    global imagecharacter ,screen , positionperso
    screen.blit(background, (0, 0))
    screen.blit(imagecharacter,positionperso)

    pygame.display.flip()


def claviersouris():
    global imagecharacter , screen , positionperso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_RIGHT] == True and positionperso[0]< screen_larg - 46:
        positionperso = ( positionperso[0] + 5 , positionperso[1] )
    if touchesPressees[pygame.K_LEFT] == True and positionperso[0]> 0:
        positionperso = ( positionperso[0] -5 , positionperso[1] )

# la boucla
continuer = 1
while continuer == 1:
    dessiner()
    claviersouris()


# Nettoyage
pygame.quit()
sys.exit()
