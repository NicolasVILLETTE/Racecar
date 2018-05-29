# Créé par Jade, le 25/11/2015 en Python 3.2
"""Classes du jeu Mortal Race"""

import pygame
from pygame.locals import *


class Voiture(pygame.sprite.Sprite):
    #Variable de la class variables partagées par toutes ses instances
    image = pygame.Surface((55,110))
    image.set_colorkey((0,0,0)) # black transparent
    """pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2) # red circle"""
    image = self.image.convert_alpha()
    #Code pour chaque instance inviduelle de la classe
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups) #La ligne la plus importante
        self.image = Voiture.image #Fait de la variable de la classe une classe d'instancemake class-variable an instance variable
        self.rect = self.image.get_rect()
        #self.radius = 50 # pour la collision ?
    def update(self, seconds):
        # no need for seconds but the other sprites need it
        self.rect.center = pygame.mouse.get_pos()

class voiture:
	"""Classe permettant de créer une voiture"""
	def __init__(self, voiture):
		#Sprites de la voiture
		self.voiture = pygame.image.load(voiture).convert_alpha()
		#Position de la voiture en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite


	def deplacer(self, direction):
		"""Methode permettant de déplacer la voiture"""

		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas une voiture
				if self.niveau.structure[self.case_y][self.case_x+1] != 'v':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite


		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'v':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite


		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'v':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite


		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'v':
					self.case_y += 1
					self.y = self.case_y * taille_sprite


