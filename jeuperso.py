

import pygame
import sys

# Initialisation donc tout ce qui est variable etc
pygame.init()
pygame.display.set_caption("America 1")

imgbougepas = pygame.image.load("img/tile000.png")
desktop_sizes = pygame.display.get_desktop_sizes()  #

screen = pygame.display.set_mode((800, 800))
imagecharacter = imgbougepas
positionperso = (100,700)
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
liste_animation2 = [
      pygame.image.load("img/tile024b.png"),
    pygame.image.load("img/tile025b.png"),
    pygame.image.load("img/tile026b.png"),
    pygame.image.load("img/tile027b.png"),
     pygame.image.load("img/tile028b.png"),
     pygame.image.load("img/tile029b.png"),
    pygame.image.load("img/tile030b.png"),
    pygame.image.load("img/tile031b.png")
]
background = pygame.image.load("War.png")
background = pygame.transform.scale(background, (800, 800))
clock = pygame.time.Clock()
# variables d'animation : 
indexanim = 0
framactuel= 0
anim_framechange= 5
    
def dessiner():
    global imagecharacter ,screen , positionperso , indexanim ,framactuel , anim_framechange
    screen.blit(background, (0, 0))
    screen.blit(imagecharacter,positionperso)

    pygame.display.flip()


def claviersouris():
    global imagecharacter , screen , positionperso  , positionperso , indexanim ,framactuel , anim_framechange
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_RIGHT] == True and positionperso[0]< 800 - 46:
        positionperso = ( positionperso[0] + 5 , positionperso[1] )
        framactuel = framactuel +1
        if framactuel >= anim_framechange:
            framactuel = 0
            indexanim = indexanim + 1
            if indexanim == len(liste_animation):
                indexanim = 0
        imagecharacter = liste_animation[indexanim]

    elif touchesPressees[pygame.K_LEFT] == True and positionperso[0]> 0:
        positionperso = ( positionperso[0] -5 , positionperso[1] )
        framactuel += 1
        if framactuel >= anim_framechange:
            framactuel = 0
            indexanim += 1
            if indexanim >= len(liste_animation2):
                indexanim = 0
        imagecharacter = liste_animation2[indexanim]
    
    #if touchesPressees[pygame.K_UP] == True and positionperso[1] == 700:
     #   for i in range(10):
      #      positionperso = (positionperso[0], positionperso[1] - 5)  # Monte
       # for i in range(10):
         #   positionperso = (positionperso[0], positionperso[1] + 5) # Redescend"

   # elif touchePressees[pygame.K_SPACE] == True :
        

    else : 
        imagecharacter = imgbougepas
        indexanim = 0
        framactuel = 0


# la boucla
continuer = 1
while continuer == 1:
    dessiner()
    claviersouris()
    clock.tick(50)


# Nettoyage
pygame.quit()
sys.exit()
