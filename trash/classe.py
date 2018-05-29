# Créé par Jade, le 28/11/2015 en Python 3.2

import pygame
from pygame.locals import *

class Voiture(pygame.sprite.Sprite):
	"""
    Movable car with which one hits the other cars
	Returns: Voiture object
	Functions: reinit, update, moveup, movedown
	Attributes: which, speed
    """

	def __init__(self, side):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('Voiture.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.side = side
		self.speed = 10
		self.state = "still"
		self.reinit()

	def reinit(self):
		self.state = "still"
		self.movepos = [0,0]
		if self.side == "left":
			self.rect.midleft = self.area.midleft
		elif self.side == "right":
			self.rect.midright = self.area.midright

	def update(self):
		newpos = self.rect.move(self.movepos)
		if self.area.contains(newpos):
			self.rect = newpos
		pygame.event.pump()

	def moveup(self):
		self.movepos[1] = self.movepos[1] - (self.speed)
		self.state = "moveup"

	def movedown(self):
		self.movepos[1] = self.movepos[1] + (self.speed)
		self.state = "movedown"
