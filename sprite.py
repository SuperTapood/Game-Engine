class Sprite:
	def __init__(self, obj, x, y):
		self.x = x
		self.y = y
		self.w = obj.w
		self.h = obj.h
		self.obj = obj
		return

	def blit(self, window):
		window.blit(window, (self.x, self.y))
	pass