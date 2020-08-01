from ..engine_object import Engine_Object
from ...exceptions import InvalidBorderButtonError
from .button import Button
from ..shapes import Rect

class Button_With_Borders(Engine_Object):
	def __init__(self, scr, x, y, w1, h1, color1, w2, h2, color2, resp):
		"""
		Screen scr - the screen object
		num x, y, w1, h1, w2, h2 - the loc and sizes of the two buttons
		tup color1, color2 - the colors of the two buttons
		func resp - the response to the click
		"""
		if w1 < w2 or h1 < h2:
			raise InvalidBorderButtonError(w1, h1, w2, h2)
		self.rect = Rect(scr, color1, x, y, w1, h1)
		self.button = Button(scr, x + ((w1 - w2) / 2), y + ((h1 - h2) / 2), w2, h2, color2, resp)
		return

	def blit(self):
		self.rect.blit()
		self.button.blit()
		return
	pass