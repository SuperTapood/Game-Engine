from ..engine_object import Engine_Object
from pygame.draw import polygon

class Polygon(Engine_Object):
	def __init__(self, scr, color, *points):
		self.scr = scr
		self.color = color
		self.points = list(points)
		print(self.points)
		return

	def blit(self):
		polygon(self.scr.display, self.color, self.points)
		return