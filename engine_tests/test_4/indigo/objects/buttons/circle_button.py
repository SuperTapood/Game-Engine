from ..engine_object import Engine_Object
from ..shapes import Circle, Rect
from pygame.mouse import get_pos, get_pressed

class Circle_Button(Engine_Object):
	def __init__(self, scr, color, x, y, radius, resp, width=0):
		self.circle = Circle(scr, color, (x, y), radius, width)
		self.x = x
		self.y = y
		self.resp = resp
		super().__init__()
		self.rect = x - radius, y - radius, radius * 2, radius * 2
		return

	def blit(self):
		self.circle.blit()
		if self.check_click():
			self.resp()
		return

	def check_click(self):
		mouse = get_pos()
		click = get_pressed()
		x, y, w, h = self.rect
		print(self.rect)
		print(mouse)
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1