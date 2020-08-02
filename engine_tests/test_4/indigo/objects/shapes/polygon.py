from ..engine_object import Engine_Object
from pygame.draw import polygon

class Polygon(Engine_Object):
	def __init__(self, scr, color, *points):
		"""
		Screen scr - the screen object
		tup color - the color of the polygon
		args points - the lists of points as a generator object
		"""
		self.scr = scr
		self.color = color
		self.points = list(points)
		return

	def blit(self):
		polygon(self.scr.display, self.color, self.points)
		return