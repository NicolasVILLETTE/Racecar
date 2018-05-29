# -*- coding: utf-8 -*-

# Créé par Jade, le 28/11/2015 en Python 3.2


"""

La voiture est censé bouger quand on utilise les flèches directionnelles
   Modifié le 28/11/2015

"""
import pygame
from pygame.locals import *
import classe



"""


#----------------------- Fonction qui permet de modifié le meilleur score du joueur dans un fichier-------------------
def set_meilleurScore():
    if score_monScore > get_meilleurScore():            # si mon score > au score contenut dans note file
        score_Fichier = open("Scores Jeu", "wb")        # on ouvre le file
        score_pickler = pickle.Pickler(score_Fichier)   # on créer une var qui save notre objet initial (joueur1 : 0) dans le fichier
        scores_joueur[joueur_nom] = score_monScore      # on modifie la valeur du score du joueur
        score_pickler.dump(scores_joueur)               # on le save
        score_Fichier.close()                           # on referme


#--------------------- Recupère le meilleur score du joueur ----------------------------
def get_meilleurScore():
    return scores_joueur[joueur_nom]                     # renvoie son meilleur score contenu dans le dico

#---------------------------- permet  de mettre le jeu en pause ----------------------------
def jeu_pause(texte='Jeu en pause'):
    pause = True

    while pause:        # Tant que pause est vrai
        fenetre_jeu.fill(BLANC)                             # font d'écran blanc
        afficher_texte(texte, NOIR, 60, font_police2)       # appel de fonction

        opt_pos1 = get_render("Reprendre (ou 'R') ", NOIR, 25, font_police2).get_size()  # renvoie les dimensions du render
        opt_pos2 = get_render(" Menu", NOIR, 25, font_police2).get_size()

        afficher_texte("Reprendre (ou 'R') ", NOIR, 25, font_police2, 800/1.4, -opt_pos2[0]/2)
        afficher_texte(" Menu", NOIR, 25, font_police2, 800/1.4, opt_pos1[0]/2)

        afficher_score("Score: " + str(score_monScore), 1280/2, 200)
        afficher_score("Meilleur score de " + joueur_nom + ": " + str(get_meilleurScore()), 1280/2, 250)

        for e in pygame.event.get():    # liste d'évènement saisi par l'user
            if e.type == pygame.QUIT:   # si on chercher a quitter
                pygame.quit()           # fermeture de pygame
                quit()                  # fermeture de python

            elif e.type == pygame.KEYDOWN:    # si une touche est pressée
                if e.key == pygame.K_r:     # touche 'c'
                    pause = False           # permet de sortir de la boucle

                elif e.key == pygame.K_m:     # touche 'm'
                    jeu_menu()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()   # get_pos() -> (x,y)
                if mouse_pos[0] > (1280 + (opt_pos2[0]+opt_pos1[0])/2)/2 and mouse_pos[0] < (1280 + (opt_pos1[0] + opt_pos2[0]))/2 and mouse_pos[1] > 800/1.4 - opt_pos2[1]/2 and mouse_pos[1] < 800/1.4 + opt_pos2[1]/2:
                    jeu_menu()
                if mouse_pos[0] > (1280 - (opt_pos1[0] + opt_pos2[0]))/2 and mouse_pos[0] < (1280 + (opt_pos2[0]+opt_pos1[0])/2)/2 and mouse_pos[1] > 800/1.4 - opt_pos1[1]/2 and mouse_pos[1] < 800/1.4 + opt_pos1[1]/2:
                    pause = False


        pygame.display.update()
#---------------------------- Fonction qui permet d'afficher un message ----------------------------
def get_render(texte, couleur, taille, police='freesansbold.ttf'):
    texte_style = pygame.font.Font(police,taille)           # On définit le style et la taille du message
    mon_render = texte_style.render(texte, True, couleur)     # paramètre (textAEcrire, lissageDuTexte, couleur)
    return mon_render

#---------------------------- Fonction qui permet d'afficher un message ----------------------------
def afficher_texte(texte, couleur, taille, police='freesansbold.ttf', positionTexte_Y=(800/2), positionTexte_X=0):
    #texte_style = pygame.font.Font(police,taille)           # On définit le style et la taille du message
    #monTexte = texte_style.render(texte, True, couleur)     # paramètre (textAEcrire, lissageDuTexte, couleur)
    monTexte = get_render(texte, couleur, taille, police)
    fenetre_jeu.blit(monTexte, (1280/2 - monTexte.get_width()/2 + positionTexte_X, positionTexte_Y - monTexte.get_size()[1]/2))                    # Affichage du texte à la postion établit ci dessus

#---------------------------- Fonction qui gère l'accident ----------------------------
def crash():
    set_meilleurScore()
    jeu_pause('Tu as perdu !')
    time.sleep(2)                    # Met en pause
    jeu_main()                       # On recommance notre boucle ppale
'''
