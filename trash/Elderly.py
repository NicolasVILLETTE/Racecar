# -*- coding: utf-8 -*-

# Créé par Jade, le 28/11/2015 en Python 3.2


"""

La voiture est censé bouger quand on utilise les flèches directionnelles
   Modifié le 28/11/2015

"""
import pygame


pygame.init()
ecran = pygame.display.set_mode((960, 720))
class Voiture(pygame.sprite.Sprite):                               #Création du premier Sprite avec sa classe pour la premiere image
    def __init__(self):                                            #Méthode intégrée au sprite et appellée quand l'objet est crée
        pygame.sprite.Sprite.__init__(self)                        #Appelle le constructeur du Sprite
        self.image = pygame.image.load("voiture.png")              #Charge l'image
        self.image = self.image.convert_alpha()                    #Cree le sprite image & une nouvelle copie de la surface avec le format désiré en pixels.
        self.rect = self.image.get_rect()              #Cree l'attribut rectangle du Sprite
        self.rect.centerx = 200                        #Position horizontale de l'image
        self.rect.centery = 200                        #Postion verticale de l'image
        self.dx = 0                                    #Initialise x
        self.dy = 0

        def update(self):
              self.rect.center = pygame.image.load()
#              if self.rect.right > ecran.get_width():
#                 self.rect.left = 0

    """def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown" """

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("voituregrande.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 800
        self.rect.centery = 450

        def update(self):
            self.rect.center = pygame.image.load()
            #if self.rect.right > ecran.get_width():
             #   self.rect.left = 0
def main():
    #fond
    fond = pygame.Surface(ecran.get_size())
    fond = pygame.image.load("background1.jpg").convert()
    ecran.blit(fond, (320, 150))
    voiture = Voiture()
    obstacle = Obstacles()
    allSprites = pygame.sprite.Group(voiture, obstacle)
    horloge =pygame.time.Clock()
    continuer = True
    while continuer:
        horloge.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    voiture.dy -= 20
                if event.key == pygame.K_DOWN:
                    voiture.dy += 20
                if event.key == pygame.K_RIGHT:
                    voiture.dx -= 20
                if event.key == pygame.K_LEFT:
                    voiture.dx += 20
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    voiture.movepos = [0,0]
                    voiture.state = "still"
        allSprites.clear(ecran, fond)
        allSprites.update()
        allSprites.draw(ecran)
        pygame.display.flip()

if __name__ == "__main__":
    main()

