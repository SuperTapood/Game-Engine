class Interactable:
	def __init__(self, img, screen, touch_conseq=None, dummy=False):
		self.screen = screen
		self.img = img
		if touch_conseq is not None:
			assert callable(touch_conseq)
		self.conseq = touch_conseq
		self.x = 0
		self.y = 0
		self.w = self.img.get_width()
		self.h = self.img.get_height()
		if not dummy:
			self.screen.add_interactable()
		return

	def blit(self):
		self.screen.blit(self.img, (self.x, self.y))
		return

	def check_for_contact(self, obj):
		pos = obj.get_pos()
		if self.check_rect(pos):
			self.conseq()
		return

	def check_rect(self, pos):
		return self.x + self.w > pos[0] > self.x and self.y + self.h > pos[1] > self.y


