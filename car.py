# Créé par Jade, le 29/11/2015 en Python 3.2
# -*- coding: utf-8 -*-
import pygame, random, time
fenetre_hauteur=800
fenetre_largeur=1280
couleur  = (255, 255, 255)
class Voiture(pygame.sprite.Sprite):  #Cette classe represente une voiture. Elle dérive de la classe Sprite dans Pygame.

    def __init__(self):

        super().__init__() # Appelle la classe mere Sprite constructeur

        self.image = pygame.image.load('voiture.png')
        # Sinon nous pouvons dessiner un rectangle representant la voiture de la sorte
        # pygame.draw.rect(self.image, color, [0, 0, largeur, hauteur])

        # Cree un rectangle au dimension de l'image
        self.rect = self.image.get_rect()

    def droite(self, pixels):
        self.rect.x += pixels
        self.image = pygame.image.load('voiture_droite.png')

    def gauche(self, pixels):
        self.rect.x -= pixels
        self.image = pygame.image.load('voiture_gauche.png')

    def gauche_droite_up (self):
         self.image = pygame.image.load('voiture.png')

    def accelerer(self, pixels):
        self.rect.y -= pixels

    def ralentir(self, pixels):
        self.rect.y += pixels


class Obstacles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("voiture1.png")
        self.rect = self.image.get_rect()

    def apparition_obstacle(self, hauteur_ecran, largeur_ecran):
                couleur=random.randrange(0,14)
                if couleur == 0:
                    self.image = pygame.image.load("voiture1.png")
                if couleur == 1:
                    self.image = pygame.image.load("voiture2.png")
                if couleur == 2:
                    self.image = pygame.image.load("voiture3.png")
                if couleur == 3:
                    self.image = pygame.image.load("voiture4.png")
                if couleur == 4:
                    self.image = pygame.image.load("voiture5.png")
                if couleur == 5:
                    self.image = pygame.image.load("voiture6.png")
                if couleur == 6:
                    self.image = pygame.image.load("voiture7.png")
                if couleur == 7:
                    self.image = pygame.image.load("voiture8.png")
                if couleur == 8:
                    self.image = pygame.image.load("voiture9.png")
                if couleur == 9:
                    self.image = pygame.image.load("voiture10.png")
                if couleur == 10:
                    self.image = pygame.image.load("voiture11.png")
                if couleur == 11:
                    self.image = pygame.image.load("voiture12.png")
                if couleur == 12:
                    self.image = pygame.image.load("voiture13.png")
                if couleur == 13:
                    self.image = pygame.image.load("voiture14.png")

                self.rect = self.image.get_rect()
                self.rect.y = -self.rect.y*0.3   # on réinitialise x et y de obstacle pour en faire "tomber" un nouveau
                self.rect.x = random.randrange(200, largeur_ecran - 200)   # A améliorer pour faire des lvls

"""
class Obstacles_Bord (pygame.sprite.Sprite):

    def __init__(self):

        super().__init__() # Appelle la classe mere Sprite constructeur

        self.rect = self.image.get_rect()

class GameMenu(pygame.sprite.Sprite):

    def __init__(self):

     super().__init__()
"""
