from time import sleep as wait
from time import time

class Sprite:
	def __init__(self, window, sprite, x, y):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.window = window
		self.moveStart = time()
		self.__blit()
		return

	def __blit(self):
		self.window.blit(self.sprite, (self.x, self.y))
		return

	def move(self, factor, x, y):
		if time() - self.moveStart >= 0.3:
			self.__moveX(int(x) * factor)
			self.__moveY(int(y) * factor)
			self.moveStart = time()
		return

	def __moveX(self, factor):
		self.x += factor
		self.__blit()
		return

	def __moveY(self, factor):
		self.y += factor
		self.__blit()
		return

	def update(self):
		self.__blit()
		return