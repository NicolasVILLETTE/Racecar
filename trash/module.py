# -*- coding: utf-8 -*-
# Créé par Jade, le 25/11/2015 en Python 3.2


"""
Created on Tue Nov 24 01:03:29 2015

@author: Jade
"""

# Bibliotheques

import pygame
import time
import random

pygame.init()

fenetre = pygame.display.set_mode((447, 435))

#Chargement et collage du fond
fond = pygame.image.load("background1.jpg").convert()
fenetre.blit(fond, (2,0))

#Chargement et collage de la voiture




       #fenetre.blit(voiture, (192,315))

#Rafraîchissement de l'écran
pygame.display.flip()

pygame.display.set_caption('Mortal Race')  #Titre de la fenetre de jeu

clock = pygame.time.Clock() #Horloge


#Maintient de la fenetre
continuer = 1

while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
          if event.type == pygame.KEY_DOWN:
            if event.key == pygame.K_LEFT:

                continuer = 0      #On arrête la boucle

"""game_loop()"""

pygame.quit()

#quit()