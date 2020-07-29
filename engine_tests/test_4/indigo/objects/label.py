import pygame
from .engine_object import Engine_Object

class Label(Engine_Object):
	def __init__(self, scr, txt, x, y, font_size, color, font="freesansbold.ttf"):
		self.scr = scr
		font = pygame.font.Font(font, font_size)
		self.text = font.render(txt, True, color)
		self.rect = self.text.get_rect()
		self.rect.topleft = (x, y)
		super().__init__()
		return

	def blit(self):
		self.scr.blit(self.text, self.rect.x, self.rect.y)
		return