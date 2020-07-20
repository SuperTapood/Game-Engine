import pygame

class Image:
	def __init__(self, path, prefix=None, get_all_with_prefix=False):
		if not get_all_with_prefix:
			self.images = [self.load_image(path)]
		else:
			paths = self.match(path, prefix)
			for path in paths:
				self.images.append(self.load_image(path))
		return

	def load_image(self, path):
		return pygame.image.load(path)

	def match(path, prefix):
		pass

	def get_img(self):
		for img in self.images:
			yield img
		return
