import pygame
from time import time


class Screen:
	def __init__(self, x, y, bg_color, caption="pygame window"):
		pygame.init()
		self.X = x
		self.Y = y
		self.bg_color = bg_color
		self.display = pygame.display.set_mode((x, y))
		self.fill(self.bg_color)
		pygame.display.set_caption(caption)
		return

	def update(self):
		for event in pygame.event.get():
			self.quit_handler(event)
		pygame.display.update()
		return

	def quit_handler(self, event):
		if event.type == pygame.QUIT:
			self.quit()
		return

	def quit(self):
		exit()
		return

	def blit(self, obj, x, y):
		self.display.blit(obj, (x, y))
		return

	def fill(self, color):
		self.bg_color = color
		self.display.fill(color)
		return