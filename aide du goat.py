#aide du goat
#import pygame, sys
#from pygame.locals import *


#*************************************************
class arbre:

    def __init__(self):
        nombre = random.randint(1,4)
        if nombre == 1
            self.nombre.arbre = pygame.image.load('arbre/arbre1.png').convert_alpha()
        self.position.x = 400
        if nombre == 2
            self.nombre.arbre = pygame.image.load('arbre/arbre2.png').convert_alpha()
        self.position.x = 800
        if nombre == 3
            self.nombre.arbre = pygame.image.load('arbre/arbre3.png').convert_alpha()
        self.position.x = 1000
        else nombre == 4
            self.nombre.arbre = pygame.image.load('arbre/arbre4.png').convert_alpha()
        self.position.x = 1200


    def affichage_arbres(self,fenetre):
        #blit permet d'afficher un elément à l'écran
        for i in range(len(self.images)):
            fenetre.blit(self.images[i],(self.x[i],self.y))

    def bouge_arbres(self,fenetre):

        for i in range(len(self.x)):
            self.x[i] -=5

            if self.x[i] < -self.images[i].get_width():
                self.x[i] = 800



    self.images = [
            pygame.image.load('arbre/arbre1.png').convert_alpha(),
            pygame.image.load('arbre/arbre2.png').convert_alpha(),
            pygame.image.load('arbre/arbre3.png').convert_alpha(),
            pygame.image.load('arbre/arbre4.png').convert_alpha(),
        ]

        self.x= [1000, 1254, 1459, 1900]
        self.y= 70














 def __init__(self):

        self.images = [
            pygame.image.load('maison/maison1.png').convert_alpha(),
            pygame.image.load('maison/maison2.png').convert_alpha(),
            pygame.image.load('maison/maison3.png').convert_alpha(),
            pygame.image.load('maison/maison4.png').convert_alpha(),
            pygame.image.load('maison/maison5.png').convert_alpha(),
            pygame.image.load('maison/maison6.png').convert_alpha()
        ]


        self.x= [1000, 1200, 1400, 1600, 1800, 2000]
        self.y=[40,30,20,10,25,35]


    def affichage_maisons(self,fenetre):
        #blit permet d'afficher un elément à l'écran
        for i in range(len(self.images)):
            fenetre.blit(self.images[i],(self.x[i],self.y[i]))

    def bouge_maisons(self,fenetre):

        for i in range(len(self.x)):
            self.x[i] -=5

            if self.x[i] < -self.images[i].get_width():
                self.x[i] = 800
































                import pygame, sys
from pygame.locals import *
import random


class maison:

    def __init__(self):

        self.images = [
            pygame.image.load('maison/maison1.png').convert_alpha(),
            pygame.image.load('maison/maison2.png').convert_alpha(),
            pygame.image.load('maison/maison3.png').convert_alpha(),
            pygame.image.load('maison/maison4.png').convert_alpha(),
            pygame.image.load('maison/maison5.png').convert_alpha(),
            pygame.image.load('maison/maison6.png').convert_alpha(),
        ]

        self.x = [1000, 1200, 1400, 1600, 1800, 2000]
        self.y= 40

    def affichage_maisons(self,fenetre):
        #blit permet d'afficher un elément à l'écran
        for i in range(len(self.images)):
            fenetre.blit(self.images[i],(self.x[i],self.y))

    def bouge_maisons(self,fenetre):

        for i in range(len(self.x)):
            self.x[i] -=5

            if self.x[i] < -self.images[i].get_width():
                self.x[i] = 800




























                import pygame, sys
from pygame.locals import *
import random


#*************************************************
class arbre:

    def __init__(self):

        self.images = [
            pygame.image.load('arbre/arbre1.png').convert_alpha(),
            pygame.image.load('arbre/arbre2.png').convert_alpha(),
            pygame.image.load('arbre/arbre3.png').convert_alpha(),
            pygame.image.load('arbre/arbre4.png').convert_alpha(),
        ]

        self.x= [1000, 1254, 1459, 1900]
        self.y= 70

    def affichage_arbres(self,fenetre):
        #blit permet d'afficher un elément à l'écran
        for i in range(len(self.images)):
            fenetre.blit(self.images[i],(self.x[i],self.y))

    def bouge_arbres(self,fenetre):

        for i in range(len(self.x)):
            self.x[i] -=5

            if self.x[i] < -self.images[i].get_width():
                self.x[i] = 800



