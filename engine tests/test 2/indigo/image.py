import pygame

class Image:
	def __init__(self, path):
		self.image = self.load_image(path)
		return

	def load_image(self, path):
		return pygame.image.load(path)

	def get_img(self):
		return self.image

	def get_dims(self):
		rect = self.image.get_rect()
		x = rect.x
		y = rect.y
		w = rect.w
		h = rect.h
		return f"x: {x}, y: {y}, w: {w}, h: {h}"

	def rescale(self, new_scale):
		new_x = self.image.get_rect().w * new_scale
		new_y = self.image.get_rect().h * new_scale
		self.resize(new_x, new_y)
		return

	def resize(self, x, y):
		self.image = pygame.transform.scale(self.image, (int(x), int(y)))
		return

	def match_size(self, image):
		## !! ##
		pass

