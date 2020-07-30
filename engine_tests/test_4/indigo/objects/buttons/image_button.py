from ..engine_object import Engine_Object
from pygame.mouse import get_pos, get_pressed

class Image_Button(Engine_Object):
	def __init__(self, scr, img, x, y, resp):
		self.scr = scr
		self.img = img
		self.x = x
		self.y = y
		self.resp = resp
		super().__init__()
		self.rect = self.get_rekt()
		return

	def blit(self):
		self.scr.blit(self.img, self.x, self.y)
		if self.check_click():
			self.resp()
		return

	def check_click(self):
		mouse = get_pos()
		click = get_pressed()
		x, y, w, h = self.rect
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1