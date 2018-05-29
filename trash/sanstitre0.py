# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:03:29 2015

@author: Jade
"""
import pygame
from pygame.locals import *
import time
import random



if event.type == KEYDOWN:
     if event.key == K_SPACE:
          print("Espace")
     if event.key == K_RETURN:
          print("Entrée")

#Rafraîchissement de l'écran
pygame.display.flip()


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0


    # Fonction pour creer un espace d'affichage

def text_objects(text, font):

    textSurface = font.render(text, True, black)

    return textSurface, textSurface.get_rect()



    # Fonction qui permet d'afficher le message

def message_display(text):

    largeText = pygame.font.Font('freesansbold.ttf',90)

    TextSurf, TextRect = text_objects(text, largeText)

    TextRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()



    # Fonction qui affiche le message

def crash():

    message_display('GameOver')

pygame.quit()
print(pygame.version.ver)

