import os
import random
import pygame
from pygame.locals import *


class arbre:

    def __init__(self):
        # Charge les images depuis le dossier 'arbre' à côté du module
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, 'arbre')
        files = ['arbre1.png', 'arbre2.png', 'arbre3.png', 'arbre4.png']
        self.images = []
        for f in files:
            path = os.path.join(img_dir, f)
            try:
                self.images.append(pygame.image.load(path).convert_alpha())
            except Exception as e:
                print(f"Warning: impossible de charger {path}: {e}")
                # placeholder surface
                surf = pygame.Surface((50, 100), pygame.SRCALPHA)
                surf.fill((34, 139, 34))
                self.images.append(surf)

        # Créer plusieurs positions 'x' pour les arbres (une par image)
        self.x = [random.randint(400, 2000) for _ in range(len(self.images))]
        self.y = 70

    def affichage_arbres(self, fenetre):
        # blit permet d'afficher un élément à l'écran
        for i in range(len(self.images)):
            fenetre.blit(self.images[i], (self.x[i], self.y))

    def bouge_arbres(self, fenetre):
        for i in range(len(self.x)):
            self.x[i] -= 5
            if self.x[i] < -self.images[i].get_width():
                self.x[i] = random.randint(800, 1000)



