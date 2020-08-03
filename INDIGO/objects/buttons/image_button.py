from ..engine_object import Engine_Object
from .button_meta import Button_Meta
from pygame.mouse import get_pos, get_pressed

class Image_Button(Button_Meta):
	def __init__(self, scr, img, x, y, resp=lambda:None, delay_time=0.3):
		"""
		Screen scr - the screen object
		pygame image img / str - the image or its location
		num x, y - the location of the button
		func resp - the response for a click
		"""
		self.scr = scr
		self.img = img
		self.x = x
		self.y = y
		self.resp = resp
		self.rect = self.get_rekt()
		self.delay_time = delay_time
		return

	def blit_func(self):
		self.scr.blit(self.img, self.x, self.y)
		return