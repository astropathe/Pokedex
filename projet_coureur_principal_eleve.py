import pygame, sys
from pygame.locals import *
import random

from projet_coureur_personnage import *
from projet_coureur_arbre import *
from projet_coureur_maison import *


def affichage_rue():
    pygame.draw.rect(window, (192, 192, 192), (0, 200, WIDTH, HEIGHT // 2), 0)


# Programme principal
pygame.init()
WIDTH, HEIGHT = 800, 300
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Balade en ville')
CIEL = (135, 206, 235)

sonic = personnage()
arbres = arbre()
maisons = maison()
moving = False
tick_animation = 0

# Main game loop
while True:
    window.fill(CIEL)
    affichage_rue()

    maisons.affichage_maisons(window)
    sonic.affichage_personnage(window)
    arbres.affichage_arbres(window)

    if moving or sonic.saut_en_cours > 0:
        if tick_animation == 0:
            if sonic.saut and sonic.saut_en_cours > 0:
                sonic.saute_personnage()
                sonic.saut_en_cours -= 1
            elif not sonic.saut:
                sonic.bouge_personnage()

            arbres.bouge_arbres(window)
            maisons.bouge_maisons(window)
            tick_animation = 13

    if tick_animation > 0:
        tick_animation -= 1

    # Keyboard events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = True
            elif event.key == pygame.K_UP and not sonic.saut:
                sonic.saut = True
                sonic.saut_en_cours = 45

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving = False
                sonic.index_run = 0
            elif event.key == pygame.K_UP:
                sonic.saut = False
                sonic.saut_en_cours = 0
                sonic.index_jump = 0

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
import pygame, sys
from pygame.locals import *
import random

from projet_coureur_personnage import *
from projet_coureur_arbre import *
from projet_coureur_maison import *

def affichage_rue():
    pygame.draw.rect(window, (192,192,192), (0, 200, WIDTH, HEIGHT // 2), 0)

# Programme principal
pygame.init()
WIDTH, HEIGHT = 800, 300
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Balade en ville')
CIEL = (135, 206, 235)

sonic = personnage()
arbres = arbre()
maisons = maison()
moving = False
tick_animation = 0

# Main game loop
while True:
    window.fill(CIEL)
    affichage_rue()

   
    maisons.affichage_maisons(window)
    sonic.affichage_personnage(window)
    arbres.affichage_arbres(window)
    

    
    if moving or sonic.saut_en_cours > 0:  
        if tick_animation == 0:
            if sonic.saut and sonic.saut_en_cours > 0:
                sonic.saute_personnage()  
                sonic.saut_en_cours -= 1  
            elif not sonic.saut:
                sonic.bouge_personnage()  

            arbres.bouge_arbres(window)
            maisons.bouge_maisons(window)
            tick_animation = 13

    if tick_animation > 0:
        tick_animation -= 1

    # Keyboard events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = True
            elif event.key == pygame.K_UP and not sonic.saut:
                sonic.saut = True  
                sonic.saut_en_cours = 45  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving = False
                sonic.index_run = 0 
            elif event.key == pygame.K_UP:
                sonic.saut = False  
                sonic.saut_en_cours = 0  
                sonic.index_jump = 0  

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

  
    pygame.display.flip()