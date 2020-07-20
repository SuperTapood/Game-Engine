from ..exceptions import PlaceholderBlitError


class Placeholder:
	def __init__(self, scr, img, x=None, y=None):
		self.scr = scr
		self.img = img
		self.x = x
		self.y = y
		return

	def deploy(self, x, y):
		return self.clone(self.img, x, y)

	def clone(self, img, x, y):
		return Placeholder(img, x, y)

	def blit(self):
		if self.x is None or self.y is None:
			raise PlaceholderBlitError(self, self.x, self.y)