# Créé par Jade, le 25/11/2015 en Python 3.2
import pygame
from pygame.locals import *
from classe import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((1220,640))

#Titre
pygame.display.set_caption("Mortal Race")


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
	#Chargement et affichage de l'écran d'acceuil
	acceuil = pygame.image.load("acceuil.jpg").convert()
	fenetre.blit(acceuil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_acceuil = 1

	#BOUCLE D'acceuil
	while continuer_acceuil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_acceuil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0

			elif event.type == KEYDOWN:
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_acceuil = 0	#On quitte l'acceuil
					choix = 'n1'		#On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_F2:
					continuer_acceuil = 0
					choix = 'n2'



	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load("background.jpg").convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		#voiture = Perso("images/voiture_droite.png", "images/voiture_gauche.png",
		#"images/voiture_haut.png", "images/voiture_bas.png", niveau)


	#BOUCLE DE JEU
	while continuer_jeu:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0

			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0

				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					voiture.deplacer('droite')
				elif event.key == K_LEFT:
					voiture.deplacer('gauche')
				elif event.key == K_UP:
					voiture.deplacer('haut')
				elif event.key == K_DOWN:
					voiture.deplacer('bas')

		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(voiture.direction, (voiture.x, voiture.y)) #voiture.direction = l'image dans la bonne direction
		pygame.display.flip()

		#Victoire -> Retour à l'acceuil
		if niveau.structure[voiture.case_y][voiture.case_x] == 'a':
			continuer_jeu = 0