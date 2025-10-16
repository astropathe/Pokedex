import os
import random
import pygame
from pygame.locals import *


class maison:

    def __init__(self):
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, 'maison')
        files = ['maison1.png', 'maison2.png', 'maison3.png', 'maison4.png', 'maison5.png', 'maison6.png']
        self.images = []
        for f in files:
            path = os.path.join(img_dir, f)
            try:
                self.images.append(pygame.image.load(path).convert_alpha())
            except Exception as e:
                print(f"Warning: impossible de charger {path}: {e}")
                surf = pygame.Surface((80, 60), pygame.SRCALPHA)
                surf.fill((150, 111, 51))
                self.images.append(surf)

        # Créer plusieurs positions 'x' pour les maisons (une par image)
        self.x = [random.randint(100, 2000) for _ in range(len(self.images))]
        self.y = 25

    def affichage_maisons(self, fenetre):
        for i in range(len(self.images)):
            fenetre.blit(self.images[i], (self.x[i], self.y))

    def bouge_maisons(self, fenetre):
        for i in range(len(self.x)):
            self.x[i] -= 5
            if self.x[i] < -self.images[i].get_width():
                self.x[i] = random.randint(800, 900)