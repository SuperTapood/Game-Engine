from ..engine_object import Engine_Object
from pygame.draw import rect
from pygame.mouse import get_pos, get_pressed
from time import time

class Button(Engine_Object):
	def __init__(self, scr, x, y, w, h, color, resp=lambda:None, border_width=0, click_delay=0.3):
		"""
		Screen scr - the screen to be blitted on
		num x, y, w, h - the dims and locs of the button
		tup color - the color of the button
		func resp - the response to the click
		num border_width - the width of the border of the button
		"""
		self.resp = resp
		self.display = scr
		self.rect = (x, y,w ,h)
		self.color = color
		self.border_width = border_width
		# implement click delay to prevent instant clicks
		self.delay_time = click_delay
		self.last_click = time()
		super().__init__()
		return

	def blit(self):
		rect(self.display.display, self.color, self.rect, self.border_width)
		# implement click delay to prevent instant clicks
		if self.check_click() and time() - self.last_click >= self.delay_time:
			self.last_click = time()
			self.resp()
		return

	def check_click(self):
		# check if the button is being click
		mouse = get_pos()
		click = get_pressed()
		x, y, w, h = self.rect
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1
	pass