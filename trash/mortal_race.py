# -*- coding: utf-8 -*-

"""
Created on Tue Nov 24 01:03:29 2015

@author: Jade
"""

# Bibliotheques

import pygame
import time
import random
import classes


# DonnÃ©es de base du programme

pygame.init()

display_width = 800     # largeur de la fenetre de jeu

display_height = 700    # hauteur de la fenetre de jeu

largeur_voiture = 148

voitureIMG=pygame.image.load("voiture.png")
fenetre = pygame.display.set_mode((1024, 640))

#Chargement et collage du fond
fond = pygame.image.load("background1.jpg").convert()
fenetre.blit(fond, (0,0))
#Rafraîchissement de l'écran
pygame.display.flip()

pygame.display.set_caption('Mortal Race')  # Titre de la fenetre de jeu

clock = pygame.time.Clock()                     # Horloge

#Chargement et collage de la voiture
voiture = pygame.image.load('voiture.png').convert_alpha()
position_voiture = voiture.get_rect()
fenetre.blit(voiture, position_voiture)
gameDisplay = pygame.display.set_mode((700,800))


# Fonctions

    # Fonction pour créer les obstacles

def obstacles(obstaclex, obstacley, obstaclew, obstacleh, color):

    pygame.draw.rect(gameDisplay, color, [obstaclex, obstacley, obstaclew, obstacleh])



    # Fonction pour créer la voiture a partir d'une photo

def voiture(x,y):

    voitureIMG.set_colorkey((0,0,0),pygame.RLEACCEL)

    gameDisplay.blit(voitureIMG,(x,y))



    # Fonction pour creer un espace d'affichage

def text_objects(text, font):

    textSurface = font.render(text, True, black)

    return textSurface, textSurface.get_rect()


    # Fonction qui affiche le message

def crash():

    message=pygame.image.load("gameover.png")
    fenetre.blit(message, (250,100))

    pygame.display.update()

    time.sleep(2)

    game_loop()


    # Fonction principale

def game_loop():

    x = (700 * 0.5)

    y = (800 - 1.3 * 200)

    x_change = 0

    obstacle_startx = random.randrange(0, 700)

    obstacle_starty = - 800

    obstacle_speed = 7

    obstacle_width = 200

    obstacle_height = 200

    gameExit = False





    while not gameExit:



        for event in pygame.event.get():



            if event.type == pygame.QUIT:

                pygame.quit()

                quit()





            if event.type == pygame.KEYDOWN:



                if event.key == pygame.K_LEFT:

                    x_change = - 15



                elif event.key == pygame.K_RIGHT:

                    x_change = + 15



            if event.type == pygame.KEYUP:



                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                    x_change = 0





        x += x_change

        voiture(x,y)

#        gameDisplay("background1.jpg", 800, 700) # fond d'Ã©cran



        # obstacles(obstaclex, obstacley, obstaclew, obstacleh, color)

        obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, red)

        obstacle_starty += obstacle_speed


        if x > 700 - 200 or x < 0:

            crash()



        if obstacle_starty > 800:

            obstacle_starty = 0 - obstacle_height

            obstacle_startx = random.randrange(0, 700)



        if y < obstacle_starty + obstacle_height:

            print('y crossover')

            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + 200 > obstacle_startx and x + 200 < obstacle_startx + obstacle_width:

                print('x crossover')

                crash()





        pygame.display.update()

        clock.tick(60)





game_loop()

pygame.quit()

quit()















