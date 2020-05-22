import pygame
from colors import *
from sprite import Sprite

class Screen:
	def __init__(self, x, y, caption=None, color=BLACK):
		self.display = pygame.display.set_mode((x, y))
		self.__objects = []
		self.color = color
		if caption is not None:
			pygame.display.set_caption(caption)
		if color != BLACK:
			self.display.fill(color)
		return

	def update(self, event):
		if event.type == pygame.QUIT:
			self.quit()
		return

	def fill(self, color):
		self.color = color
		self.display.fill(color)
		return

	def quit(self):
		pygame.quit()
		quit()
		return

	def empty(self):
		for sprite in self.__objects:
			self.delete(sprite)
		return

	def addSprite(self, object, x, y):
		self.__objects.append(Sprite(object, x, y))
		return self.__objects[-1]

	def blit(self):
		self.fill(self.color)
		for sprite in self.__objects:
			sprite.blit(self.display)
		return

	def delete(self, sprite):
		self.__objects.remove(sprite)
		# sprite.delete()
		return

	def __loadImage(self, image):
		return pygame.image.load(image)

	def addImgAsSprite(self, img, x, y):
		img = self.__loadImage(img)
		return self.addSprite(img, x, y)

	def setBackground(self, img):
		img = self.__loadImage(img)
		self.addSprite(img, 0, 0)
		return

	def addRect(self, x, y, w, h, color):
		rect = pygame.draw.rect(self.display, color, (x, y, w, h))
		return self.addSprite(rect, x, y)

	def addCircle(self, x, y, r, color):
		circle = pygame.draw.circle(self.display, color, (x, y), r)
		return self.addSprite(circle, x, y)

	def move(self, obj, pixels, x, y):
		if x:
			obj.moveX(pixels)
		if y:
			obj.moveY(pixels)
		return