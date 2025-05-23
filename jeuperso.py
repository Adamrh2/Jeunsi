import pygame 
import sys
import random
# INITIALISATION
pygame.init()
pygame.display.set_caption("America 1")

imgbougepas = pygame.image.load("img/tile000.png")
screen = pygame.display.set_mode((800, 800))
imagecharacter = imgbougepas
positionperso = (100,700)
vitesse_y = 0
gravite = 1
saut = False
hauteur_sol = positionperso[1]  
regarddr = True

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

liste_anim_hits = [
    pygame.image.load("img/tile002.png"),
    pygame.image.load("img/tile003.png"),
    pygame.image.load("img/tile004.png"),
    pygame.image.load("img/tile005.png")
]

liste_anim_hits2 = [
    pygame.image.load("img/tile002b.png"),
    pygame.image.load("img/tile003b.png"),
    pygame.image.load("img/tile004b.png"),
    pygame.image.load("img/tile005b.png")
]

liste_enemy_mort = [
    pygame.image.load("img/enemy018.png"),
    pygame.image.load("img/enemy019.png"),
    pygame.image.load("img/enemy020.png"),
    pygame.image.load("img/enemy021.png"),
    pygame.image.load("img/enemy022.png"),
    pygame.image.load("img/enemy023.png"),
    pygame.image.load("img/enemy024.png")
]

background = pygame.image.load("War.png")
background = pygame.transform.scale(background, (800, 800))
clock = pygame.time.Clock()

indexanim = 0
framactuel= 0
anim_framechange= 5
attaque = False
img_hit = 0
fram_hit = 0
fram_chg_hit = 10

score = 0
font = pygame.font.SysFont(None, 40)

base_speed_enemy = 2

# Liste d'ennemis, chaque ennemi est un dict
ennemis_list = []

def spawn_enemy():
    pos_x = random.randint(850, 1200)
    pos_y = hauteur_sol
    ennemi = {
        "img": pygame.image.load("img/enemy000.png"),
        "pos": [pos_x, pos_y],
        "speed": base_speed_enemy,
        "mort": False,
        "img_mort_index": 0,
        "mort_anim_frame": 0,
        "rect": None
    }
    ennemi["rect"] = ennemi["img"].get_rect(topleft=ennemi["pos"])
    ennemis_list.append(ennemi)

# Spawn enemi la function
for _ in range(3):
    spawn_enemy()

def dessiner():
    global imagecharacter ,screen , positionperso , indexanim ,framactuel , anim_framechange, score
    screen.blit(background, (0, 0))
    for e in ennemis_list:
        screen.blit(e["img"], e["pos"])
    screen.blit(imagecharacter,positionperso)
    score_text = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()

def avancer_ennemi(e):
    if not e["mort"]:
        e["pos"][0] -= e["speed"]
        if e["pos"][0] < -50:
            # reset position à droite pour respawn infini
            e["pos"][0] = random.randint(850, 1200)
    e["rect"].topleft = e["pos"]

def mort_anime(e):
    if e["mort"]:
        e["mort_anim_frame"] +=1
        if e["mort_anim_frame"] >= 8:
            e["mort_anim_frame"] = 0
            e["img_mort_index"] +=1
            if e["img_mort_index"] >= len(liste_enemy_mort):
                return True
        if e["img_mort_index"] < len(liste_enemy_mort):
            e["img"] = liste_enemy_mort[e["img_mort_index"]]
    return False

def claviersouris():
    global continuer
    global imagecharacter , screen , positionperso , indexanim ,framactuel , anim_framechange , saut , gravite , vitesse_y , hauteur_sol , attaque, img_hit, fram_hit, regarddr, score, base_speed_enemy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global continuer
            continuer = 0

    touchesPressees = pygame.key.get_pressed()

    if touchesPressees[pygame.K_RIGHT] == True and positionperso[0] < 800 - 46:
        positionperso = (positionperso[0] + 5, positionperso[1])
        framactuel += 1
        if framactuel >= anim_framechange:
            framactuel = 0
            indexanim += 1
            if indexanim == len(liste_animation):
                indexanim = 0
        imagecharacter = liste_animation[indexanim]
        regarddr = True

    elif touchesPressees[pygame.K_LEFT] == True and positionperso[0] > 0:
        positionperso = (positionperso[0] - 5, positionperso[1])
        framactuel += 1
        if framactuel >= anim_framechange:
            framactuel = 0
            indexanim += 1
            if indexanim == len(liste_animation2):
                indexanim = 0
        imagecharacter = liste_animation2[indexanim]
        regarddr = False
    
    if touchesPressees[pygame.K_UP] and not saut:
        vitesse_y = -18
        saut = True
    
    vitesse_y += gravite
    positionperso = (positionperso[0], positionperso[1] + vitesse_y)

    if positionperso[1] >= hauteur_sol:
        positionperso = (positionperso[0], hauteur_sol)
        vitesse_y = 0
        saut = False
    
    if touchesPressees[pygame.K_SPACE]:
        if not attaque:
            attaque = True
            img_hit = 0
            fram_hit = 0

    if attaque:
        fram_hit += 1
        if fram_hit >= fram_chg_hit:
            fram_hit = 0
            if img_hit < len(liste_anim_hits) - 1:
                img_hit += 1
            else:
                attaque = False
                img_hit = 0
        if regarddr:
            imagecharacter = liste_anim_hits[img_hit]
        else:
            imagecharacter = liste_anim_hits2[img_hit]

    if not (touchesPressees[pygame.K_RIGHT] or touchesPressees[pygame.K_LEFT]) and not attaque:
        imagecharacter = imgbougepas
        indexanim = 0
        framactuel = 0

    rect_perso = pygame.Rect(positionperso[0], positionperso[1], 46, 64)

    if not attaque:
        for e in ennemis_list:
            if not e["mort"] and rect_perso.colliderect(e["rect"]):
                screen.blit(font.render("T'a perdu noob", True, (255,0,0)), (300,400))
                pygame.display.flip()
                pygame.time.delay(2000)
                continuer = 0

    if attaque:
        for e in ennemis_list:
            if not e["mort"] and rect_perso.colliderect(e["rect"]):
                e["mort"] = True
                score += 1
                base_speed_enemy = 2 + score*0.05
                for enn in ennemis_list:
                    enn["speed"] = base_speed_enemy

    for e in ennemis_list[:]:
        if e["mort"]:
            fini = mort_anime(e)
            if fini:
                ennemis_list.remove(e)

    for e in ennemis_list:
        avancer_ennemi(e)

    if random.random() < 0.01:  # petite chance chaque frame de spawn un nouvel ennemi
        spawn_enemy()


continuer = 1
while continuer == 1:
    dessiner()
    claviersouris()
    clock.tick(50)

pygame.quit()
sys.exit()
