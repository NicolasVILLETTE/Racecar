# Créé par Jade, le 29/11/2015 en Python 3.2
# -*- coding: utf-8 -*-

import pygame, random

#Importe la classe Voiture
from car import Voiture, Obstacles
pygame.init()

vert = (20, 255, 140)
orange = (255, 220, 10)
gris = (128, 128 ,128)
blanc = (255, 255, 255)

largeur_ecran=1280
hauteur_ecran=800

taille_ecran = (largeur_ecran, hauteur_ecran)
ecran = pygame.display.set_mode(taille_ecran)
surface_ecran = pygame.Surface([largeur_ecran, hauteur_ecran])



#---------------------------- Fonction qui permet d'afficher un message ----------------------------
def get_render(texte, couleur, taille, police='Montserrat-Regular.otf'):
    texte_style = pygame.font.Font(police,taille)           # On définit le style et la taille du message
    mon_render = texte_style.render(texte, True, couleur)     # paramètre (textAEcrire, lissageDuTexte, couleur)
    return mon_render

#---------------------------- Fonction qui permet d'afficher un message ----------------------------
def afficher_texte(texte, couleur, taille, police='Montserrat-Regular.otf', positionTexte_Y=(hauteur_ecran/2), positionTexte_X=0):
    monTexte = get_render(texte, couleur, taille, police)
    ecran.blit(monTexte, (largeur_ecran/2 - monTexte.get_width()/2 + positionTexte_X, positionTexte_Y - monTexte.get_size()[1]/2))

def jeu():
    #Liste qui va contenir tout les sprites que nous allons utiliser.
    all_sprites_list = pygame.sprite.Group()

    voiture_joueur = Voiture()
    voiture_joueur.rect.x = (largeur_ecran - 90)/2
    voiture_joueur.rect.y = hauteur_ecran - 199

    obstacle = Obstacles ()
    obstacle.rect.x = random.randrange(500, 780)
    obstacle.rect.y = -100
    obstacle1=Obstacles ()
    obstacle2=Obstacles ()
    # Ajoute la voiture que nous controlons a la liste des objets
    all_sprites_list.add(voiture_joueur, obstacle, obstacle1, obstacle2)
    horloge=pygame.time.Clock()
    pygame.key.set_repeat(1 , 2)
    obstacle_vitesse = 5
    voiture_vitesse = 3
    horloge_vitesse = 60
    ligne = hauteur_ecran/2
    score = 0
    continuer=True
    while continuer:
            pygame.display.set_caption("Mortal Race")
            obstacle.rect.y += obstacle_vitesse
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    continuer=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                         voiture_joueur.droite(voiture_vitesse)
                    if event.key==pygame.K_LEFT:
                         voiture_joueur.gauche(voiture_vitesse)
                    if event.key==pygame.K_UP:
                         voiture_joueur.accelerer(voiture_vitesse)
                    if event.key==pygame.K_DOWN:
                         voiture_joueur.ralentir(voiture_vitesse)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                       voiture_joueur.gauche_droite_up()

            if pygame.sprite.collide_rect(voiture_joueur,obstacle) or pygame.sprite.collide_rect(voiture_joueur, obstacle1) or pygame.sprite.collide_rect(voiture_joueur, obstacle2) : #or pygame.sprite.collide_rect(voiture_joueur, obstacle_bord)
                    continuer=False
                    #voiture_joueur.rect.colliderect(obstacle.rect)
            if obstacle.rect.y > hauteur_ecran:        # Si l'objet est "tombé" sous la fenêtre du jeu
                      # tous les 5 obstacle on up la vitesse
                obstacle.apparition_obstacle (hauteur_ecran, largeur_ecran)
                score += 1                 # on incremente le score
                modulo=5
                if score%(modulo) == 0:           # tous les 5 obstacle on up la vitesse
                      obstacle_vitesse += 1.3
                      voiture_vitesse +=1
                      ligne += 1.5
                      modulo +=5
                      horloge_vitesse +=2
                if score !=0 and score%3 == 0:
                      obstacle1.apparition_obstacle (hauteur_ecran, largeur_ecran)
                if score != 0 and score%6 == 0:
                      obstacle2.apparition_obstacle (hauteur_ecran, largeur_ecran)
                if score != 7 and score%6 == 0 :
                      obstacle1.apparition_obstacle (hauteur_ecran, largeur_ecran)

            obstacle.rect.y += obstacle_vitesse
            obstacle1.rect.y += obstacle_vitesse
            obstacle2.rect.y += obstacle_vitesse
            ligne += 2.7*obstacle_vitesse
            if ligne > hauteur_ecran + 90:
               ligne = hauteur_ecran/2

                        # ecran.blit(surface_ecran, score)

                        # Logique de jeu
            all_sprites_list.update()

                        #Dessine le fond - l'herbe
            ecran.fill(vert)
                        #Dessine la route - le bitume
            pygame.draw.rect(ecran, gris, [80,0, largeur_ecran-160,hauteur_ecran])
                        #Dessine la ligne blanche, on utilise ligne qu'on implemente pour donner une impression de mouvement
            pygame.draw.line(ecran, blanc, (largeur_ecran/4, ligne - 100), (largeur_ecran/4, ligne), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)
            pygame.draw.line(ecran, blanc, (largeur_ecran/4, ligne - hauteur_ecran/2 - 200), (largeur_ecran/4, ligne - hauteur_ecran/2 - 100), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)
            pygame.draw.line(ecran, blanc, (largeur_ecran/1.33, ligne - 100), (largeur_ecran/1.33, ligne), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)
            pygame.draw.line(ecran, blanc, (largeur_ecran/1.33, ligne - hauteur_ecran/2 - 200), (largeur_ecran/1.33, ligne - hauteur_ecran/2 - 100), 10)  # on dessine une ligne: line(Surface, color, start_pos, end_pos, width=1)
            pygame.draw.line(ecran, orange, (largeur_ecran/2-15, 0), (largeur_ecran/2-15, hauteur_ecran), 10 )
            pygame.draw.line(ecran, orange, (largeur_ecran/2+15, 0), (largeur_ecran/2+15, hauteur_ecran), 10 )
                        #Dessine tout les sprites a l'écran
            all_sprites_list.draw(ecran)

                        #Rafraichit l'écran
            pygame.display.flip()
                        #Nombre de FPS
            horloge.tick(horloge_vitesse)



# --------------------------- Sous menu d'instruction------------------------
def jeu_menuInstru():

    menu_instru = True
    while menu_instru:
        instruction_image = pygame.image.load("background_instruction.png") # on charge une image
        ecran.blit(instruction_image, (0,0))
        afficher_texte("Instruction", blanc, 40,  'Montserrat-Regular.otf', 200)                       # affichage de texte
        afficher_texte("Deplacement : pave directionnelle", blanc, 20,  'Montserrat-Regular.otf', 300)
        afficher_texte("Pause : touche 'p'", blanc, 20,  'Montserrat-Regular.otf', 350)
        instru_retour = get_render("Retour menu", blanc, 20,  'Montserrat-Regular.otf').get_size()    # on récupère les dimensions du render servant à afficher du txt pour gerer les cdtions de click
        afficher_texte("Retour menu", blanc, 20,  'Montserrat-Regular.otf', 400)                      # .get_size() -> (x,y)

        for e in pygame.event.get():                                                    # récupère actions user
            if e.type == pygame.QUIT:                                                   # si on cherche a fermer le prog
                pygame.quit()
                quit()

            elif e.type == pygame.MOUSEBUTTONDOWN:                                      # si click de souris
                mouse_pos = pygame.mouse.get_pos()                                      # on récupère la position de la souris
                # si il click sur 'Retour menu'
                if mouse_pos[0] > largeur_ecran/2 - instru_retour[0]/2 and mouse_pos[0] < largeur_ecran/2 + instru_retour[0]/2 and mouse_pos[1] > 400 - instru_retour[1]/2 and mouse_pos[1] < 400 + instru_retour[1]/2:
                    menu_instru = False


        pygame.display.update()          # On rafraichit pour afficher

#---------------------- MENU PRINCIPALE ---------------------
def jeu_menu():
    menu = True
    while menu:
        pygame.display.set_caption("MENU : Mortal Race")
        menu_image = pygame.image.load("background_menu.png") # on charge une image
        ecran.blit(menu_image, (0,0))                                             # on l'affiche

        #afficher_texte("HOT WHEELS RACER", blanc, 40, 'Montserrat-Regular.otf', hauteur_ecran/6.5) # affichage de txt
        #afficher_texte("MENU", blanc, 50, 'Montserrat-Regular.otf', hauteur_ecran/3.5)

        jouer = get_render("Jouer", blanc, 40, 'Montserrat-Regular.otf').get_size()                 # on récupère les dimensions du render servant à afficher du txt pour gerer les cdtions de click
        instru = get_render("Instruction", blanc, 40, 'Montserrat-Regular.otf').get_size()          # .get_size() -> (x,y)
        quitter = get_render("Quitter", blanc, 40, 'Montserrat-Regular.otf').get_size()             # affichage de txt
        afficher_texte("Jouer", blanc, 40, 'Montserrat-Regular.otf', hauteur_ecran/2)
        afficher_texte("Instruction", blanc, 40, 'Montserrat-Regular.otf', hauteur_ecran/1.7)
        afficher_texte("Quitter", blanc, 40, 'Montserrat-Regular.otf', hauteur_ecran/1.45)

        #ecran.blit(son_coupe,(20, 630))                                           # affichage du logo de son
        for e in pygame.event.get():

            if e.type == pygame.QUIT:                                                   # récupère actions user
                pygame.quit()                                                           # si on cherche a fermer le prog
                quit()

            elif e.type == pygame.MOUSEBUTTONDOWN:                                      # si click de souris
                mouse_pos = pygame.mouse.get_pos()                                      # get_pos() -> (x,y) souris

                # conditions si click sur 'jouer'
                if mouse_pos[0] > largeur_ecran/2 - jouer[0]/2 and mouse_pos[0] < largeur_ecran/2 + jouer[0]/2 and mouse_pos[1] > hauteur_ecran/2 - jouer[1]/2 and mouse_pos[1] < hauteur_ecran/2 + jouer[1]/2:
                    pygame.display.flip()
                    jeu()
                    pygame.display.flip()
                # conditions si click sur 'instruction'
                elif mouse_pos[0] > largeur_ecran/2 - instru[0]/2 and mouse_pos[0] < largeur_ecran/2 + instru[0]/2 and mouse_pos[1] > hauteur_ecran/1.7 - instru[1]/2 and mouse_pos[1] < hauteur_ecran/1.7 + instru[1]/2:
                    jeu_menuInstru()

                # sur 'quitter'
                elif mouse_pos[0] > largeur_ecran/2 - quitter[0]/2 and mouse_pos[0] < largeur_ecran/2 + quitter[0]/2 and mouse_pos[1] > hauteur_ecran/1.45 - quitter[1]/2 and mouse_pos[1] < hauteur_ecran/1.45 + quitter[1]/2:
                    pygame.quit()
                    quit()


        pygame.display.update()          # On rafraichit pour afficher


jeu_menu()
pygame.quit()

