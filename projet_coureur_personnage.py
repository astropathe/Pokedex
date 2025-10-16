import os
import pygame
from pygame.locals import *

class personnage:
    def __init__(self):
        # Chargement des sprites de Sonic (chemin relatif au module)
        base_dir = os.path.dirname(__file__)
        img_path = os.path.join(base_dir, 'sonic_104_114.png')
        try:
            perso = pygame.image.load(img_path).convert_alpha()
        except Exception as e:
            # Si l'image est manquante, crée une surface vide de secours pour éviter le plantage
            print(f"Warning: impossible de charger {img_path}: {e}")
            perso = pygame.Surface((104 * 9, 114 * 3), pygame.SRCALPHA)
        
        # Animation de course
        self.image = [perso.subsurface(x, 0, 104, 114) for x in range(0, 9 * 104, 104)]
        
        # Animation de saut (boule)
        self.image_saut = [perso.subsurface(x, 2 * 114, 104, 114) for x in range(0, 7 * 104, 104)]
        
        self.index_run = 0  
        self.index_jump = 0  
        self.saut = False  # Indique si Sonic est en train de sauter
        self.saut_en_cours = 0  # Durée de l'animation de saut

    # Affichage du personnage
    def affichage_personnage(self, fenetre):
        if self.saut and self.saut_en_cours > 0:
            # Affiche l'animation en boule (saut)
            fenetre.blit(self.image_saut[self.index_jump], (400, 75))  # Position plus haute pour le saut
        else:
            # Affiche l'animation de course
            fenetre.blit(self.image[self.index_run], (400, 170))

    # Animation de course
    def bouge_personnage(self):
        self.index_run = (self.index_run + 1) % len(self.image)
        
    # Animation de saut
    def saute_personnage(self):
        self.index_jump = (self.index_jump + 1) % len(self.image_saut)
