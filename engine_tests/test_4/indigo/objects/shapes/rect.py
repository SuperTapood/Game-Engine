from pygame.draw import rect
from ..engine_object import Engine_Object


class Rect(Engine_Object):
	def __init__(self, scr, color, x, y, w, h, width=0):
		"""
		Screen scr - the screen object
		tup color - the color of the rect
		x, y, w, h - the dims of the rect
		int width - the width of the rect
		"""
		self.scr = scr
		self.color = color
		self.rect = (x, y, w, h)
		self.width = width
		super().__init__()
		return
		
	def blit(self):
		rect(self.scr.display, self.color, self.rect, self.width)
		return