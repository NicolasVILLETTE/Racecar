# -*- coding: utf-8 -*-


# Bibliotheques

import pygame

import time

import random

import os

import pickle


# Données de base du programme

pygame.init()

FENETRE_LARGEUR = 600          # largeur de la fenetre de jeu

FENETRE_HAUTEUR = 700          # hauteur de la fenetre de jeu

NOIR = (0,0,0)                 # affectation de couleur (rgb)

BLANC = (255,255,255)          # affectation de couleur

GRIS = (100,100,100)           # affectation de couleur

fenetre_jeu = pygame.display.set_mode((FENETRE_LARGEUR,FENETRE_HAUTEUR))  # crée la fenêtre de jeu

pygame.display.set_caption('Jeux Projet Info')       # Titre de la fenetre de jeu

horloge = pygame.time.Clock()                        # Horloge (nécessaire pour la rapidité du jeu par ex)

VOITURE_IMG = pygame.image.load('voiture.png')          # charge la photo de la voiture (chemin relatif) (ne sert pas à l'afficher)

OBSTACLE_IMG = pygame.image.load('voiture1.png')

VOITURE_LARGEUR = VOITURE_IMG.get_width()            # affectation taille de l'img de la voiture (utile pr test)



direction = "normal"

score_monScore = 0



scores_joueur = {"joueur1": 0}



if os.path.isfile("Scores Jeu"):                        # Si le file existe

    score_Fichier = open("Scores Jeu", "rb+")           # on l'ouvre

    score_unpickler = pickle.Unpickler(score_Fichier)   # on crée une var qui va récupérer notre obj

    ligne = score_Fichier.read()                        # on lit notre fichier

    if ligne:                                           # si il contient quelquechose (notre objet)

        score_Fichier.seek(0)                           # on se replace au début

        scores_joueur = score_unpickler.load()          # on charge notre objet dans notre variable



    elif not ligne:                                     # si il ne contient rien

        score_pickler = pickle.Pickler(score_Fichier)   # on créer une var qui save notre objet initial (joueur1 : 0) dans le fichier

        score_pickler.dump(scores_joueur)               # on le save

    score_Fichier.close()                               #on referme



else :

    score_Fichier = open("Scores Jeu", "wb")            # Crée le file si n'existe pas

    score_pickler = pickle.Pickler(score_Fichier)       # on créer une var qui save notre objet initial (joueur1 : 0) dans le fichier

    score_pickler.dump(scores_joueur)                   # on le save

    score_Fichier.close()                               #on referme





# Fonctions

def set_meilleurScore():

    if score_monScore > get_meilleurScore():            # si mon score > au score contenut dans note file

        score_Fichier = open("Scores Jeu", "wb")        # on ouvre le file

        score_pickler = pickle.Pickler(score_Fichier)   # on créer une var qui save notre objet initial (joueur1 : 0) dans le fichier

        scores_joueur["joueur1"] = score_monScore       # on modifie la valeur du score du joueur

        score_pickler.dump(scores_joueur)               # on le save

        score_Fichier.close()                           # on referme





def get_meilleurScore():

    return scores_joueur["joueur1"]                     # renvoie son meilleur score contenu dans le dico



# permet  de mettre le jeu en pause

def jeu_pause(texte='Jeu en pause'):
    pause = True
    while pause:        # Tant que pause est vrai
        for e in pygame.event.get():    # liste d'évènement saisi par l'user
            if e.type == pygame.QUIT:   # si on chercher a quitter
                pygame.quit()           # fermeture de pygame
                quit()                  # fermeture de python

            if e.type == pygame.KEYDOWN:    # si une touche est pressée
                if e.key == pygame.K_c:     # touche 'c'
                    pause = False           # permet de sortir de la boucle

                if e.key == pygame.K_q:
                    pygame.quit()
                    quit()


        fenetre_jeu.fill(BLANC)             # font d'écran blanc
        afficher_texte(texte, NOIR, 70, 'SEASRN__.ttf')    # appel de fonction
        afficher_texte("'c' pour reprendre, 'q' pour quitter", NOIR, 25, 'SEASRN__.ttf', 500)
        afficher_score(score_monScore, FENETRE_LARGEUR/2, 200)
        score_meilleurScore = get_meilleurScore()
        afficher_score(score_meilleurScore, FENETRE_LARGEUR/2, 250) # a corrigé
        pygame.display.update()          # On rafraichit pour afficher



# affiche le score du joueur

def afficher_score(nombre_obstacles, scorePosition_X = 40, scorePosition_Y=1):

    score_style = pygame.font.SysFont(None, 25)     # on définit le style du texte

    score_blocTexte = score_style.render('Score: ' + str(nombre_obstacles), True, NOIR)     # on crée la surface du texte

    fenetre_jeu.blit(score_blocTexte, (scorePosition_X - score_blocTexte.get_width()/2,scorePosition_Y))        # on l'affiche





def fond_ecran(ligne_positionY):

    fenetre_jeu.fill(GRIS)      # fond d'écran gris

    pygame.draw.line(fenetre_jeu, BLANC, (FENETRE_LARGEUR/3, ligne_positionY - 100), (FENETRE_LARGEUR/3, ligne_positionY), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)

    pygame.draw.line(fenetre_jeu, BLANC, (FENETRE_LARGEUR/3, ligne_positionY - FENETRE_HAUTEUR/2 - 200), (FENETRE_LARGEUR/3, ligne_positionY - FENETRE_HAUTEUR/2 - 100), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)

    pygame.draw.line(fenetre_jeu, BLANC, (2*FENETRE_LARGEUR/3, ligne_positionY - 100), (2*FENETRE_LARGEUR/3, ligne_positionY), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)

    pygame.draw.line(fenetre_jeu, BLANC, (2*FENETRE_LARGEUR/3, ligne_positionY - FENETRE_HAUTEUR/2 - 200), (2*FENETRE_LARGEUR/3, ligne_positionY - FENETRE_HAUTEUR/2 - 100), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)



def creer_obstacle(monImage, obstacle_positionX, obstacle_positionY):

    fenetre_jeu.blit(monImage, (obstacle_positionX, obstacle_positionY)) # Affiche un obstacle





    # Fonction pour créer la voiture a partir d'une photo

def voiture(x,y):

    if direction == "gauche":

        monImage = pygame.transform.rotate (VOITURE_IMG, 5)     # on effectue une rotation de l'img pour simuler un virage



    if direction == "droite":

        monImage = pygame.transform.rotate (VOITURE_IMG, 355)



    if direction == "normal":

        monImage = VOITURE_IMG



    fenetre_jeu.blit(monImage,(x,y)) # blit permet de rajouter notre image sur la fenêtre de jeu à la position (x,y)

                                        # (0,0) se trouve en haut à gauche







    # Fonction qui permet d'afficher le message

def afficher_texte(texte, couleur, taille, police='freesansbold.ttf', positionTexte_Y=(FENETRE_HAUTEUR/2)):

    texte_style = pygame.font.Font(police,taille)           # On définit le style et la taille du message

    monTexte = texte_style.render(texte, True, couleur)     # paramètre (textAEcrire, lissageDuTexte, couleur)

    fenetre_jeu.blit(monTexte, (FENETRE_LARGEUR/2 - monTexte.get_width()/2, positionTexte_Y))                    # Affichage du texte à la postion établit ci dessus





    # Fonction qui affiche le message

def crash():

    set_meilleurScore()

    jeu_pause('Tu as perdu !')

    time.sleep(2)                    # Met en pause

    jeu_main()                       # On recommance notre boucle ppale





    # Fonction principale

def jeu_main():

    voiture_x = (FENETRE_LARGEUR * 0.5)

    voiture_y = (FENETRE_HAUTEUR * 0.7)



    x_change = 0
    obstacle_largeur = OBSTACLE_IMG.get_width()
    obstacle_hauteur = OBSTACLE_IMG.get_height()
    obstacle_voie1 = random.randrange(0, FENETRE_LARGEUR/3 - obstacle_largeur)
    obstacle_voie2 = random.randrange(FENETRE_LARGEUR/3, 2*FENETRE_LARGEUR/3 - obstacle_largeur)
    obstacle_voie3 = random.randrange(2*FENETRE_LARGEUR/3, FENETRE_LARGEUR - obstacle_largeur)
    obstacle_vitesse = 5
    obstacle_X = random.randrange(obstacle_voie1, obstacle_voie3)
    obstacle_Y = - 200
    ligne_Y = FENETRE_HAUTEUR/2
    ligne_vitesse = 10

    accident = False

    global direction        # global permet de pouvoir la modifié

    global score_monScore

    global scores_joueur

    score_monScore = 0

    while not accident:
    # On gère les actions du joueur

        for e in pygame.event.get():
            if e.type == pygame.QUIT:   # Si on cherche à fermer le jeu
                pygame.quit()               # fermeture de pygame
                quit()                      # fermeture de python

            if e.type == pygame.KEYDOWN:    # si une touche du clavier est enfoncée
                if e.key == pygame.K_p:      # touche 'p'
                    jeu_pause()
                if e.key == pygame.K_LEFT:  # flèche directionnelle gauche
                    x_change = -10
                    direction = "gauche"
                elif e.key == pygame.K_RIGHT:   # flèche directionnelle gauche
                    x_change = 10
                    direction = "droite"
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    x_change = 0
                    direction = "normal"

        # On gère l'affichage de nôtre fenêtre
        voiture_x += x_change           # enregistre le déplacement
        fond_ecran(ligne_Y)
        ligne_Y += ligne_vitesse
        creer_obstacle(OBSTACLE_IMG , obstacle_X, obstacle_Y)
        obstacle_Y += obstacle_vitesse      # permet de faire descendre l'obstacle
        afficher_score(score_monScore)      # appel de la fonction qui affiche le score
        voiture(voiture_x,voiture_y)        # appel de la fonction "voiture"

        # On gère les differents cas possibles
        if ligne_Y > FENETRE_HAUTEUR + 100:
            ligne_Y = FENETRE_HAUTEUR/2
        if voiture_x > FENETRE_LARGEUR - VOITURE_LARGEUR or voiture_x < 0: # Si la voiture touche les bords de la fenêtre c'est perdu !
            crash()
        if obstacle_Y > FENETRE_HAUTEUR:        # Si l'objet est "tombé" sous la fenêtre du jeu
            obstacle_Y = 0 - obstacle_hauteur   # on réinitialise x et y de obstacle pour en faire "tomber" un nouveau
            obstacle_X = random.randrange(0, FENETRE_LARGEUR - obstacle_largeur)   # A améliorer pour faire des lvls
            score_monScore += 1                 # on incremente le score

            if score_monScore%5 == 0:           # tous les 5 obstacle on up la vitesse

                obstacle_vitesse += 2

                ligne_vitesse += 2





        if voiture_y <= obstacle_Y + obstacle_hauteur: # si voiture dépasse un obstacle

            if voiture_y < obstacle_Y + obstacle_hauteur + 6 and voiture_y > obstacle_Y + obstacle_hauteur - 6:

                print('voiture dépasse obstacle (y)')



            # si il existe une intersection (selon les x, y testé ci-dessus) entre voiture et obstacle

            if voiture_x > obstacle_X and voiture_x < obstacle_X + obstacle_largeur or voiture_x + VOITURE_LARGEUR > obstacle_X and voiture_x + VOITURE_LARGEUR < obstacle_X + obstacle_largeur or voiture_x + VOITURE_LARGEUR/2 > obstacle_X and voiture_x + VOITURE_LARGEUR/2 < obstacle_X + obstacle_largeur:

                print('voiture percute obstacle (y et x)')

                crash()

        pygame.display.update()     # rafraîchit la fenêtre jeu

        horloge.tick(60)            # 60 images par secondes, rapidité du jeu

jeu_main()

pygame.quit()

quit()