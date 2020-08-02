from ..engine_object import Engine_Object
from pygame.draw import circle

class Circle(Engine_Object):
	def __init__(self, scr, color, pos, radius, width=0):
		"""
		Screen scr - the screen object
		tup color - the color of the circle
		tup pos - the pos of the circle
		num radius - the radius of the circle
		int width - the width of the circle
		"""
		self.scr = scr
		self.color = color
		self.pos = pos
		self.r = radius
		self.width = width
		super().__init__()
		return

	def blit(self):
		circle(self.scr.display, self.color, self.pos, self.r, self.width)
		return