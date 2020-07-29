from ..engine_object import Engine_Object
from pygame.draw import rect
from pygame.mouse import get_pos, get_pressed
from time import time

class Button(Engine_Object):
	def __init__(self, scr, x, y, w, h, color, resp, border_width=0):
		"""
		Screen scr - the screen to blit on
		x, y, w, h - the loc to blit on and the size
		"""
		self.resp = resp
		self.display = scr
		self.rect = (x, y,w ,h)
		self.color = color
		self.border_width = border_width
		self.delay_time = 0.3
		self.last_click = time()
		super().__init__()
		return

	def blit(self):
		rect(self.display.display, self.color, self.rect, self.border_width)
		if self.check_click() and time() - self.last_click >= self.delay_time:
			self.last_click = time()
			self.resp()
		return

	def check_click(self):
		mouse = get_pos()
		click = get_pressed()
		x, y, w, h = self.rect
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1
	pass