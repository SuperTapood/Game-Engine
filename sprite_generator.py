from sprite import Sprite


class Sprite_Generator:
	def __init__(self, img, x, y , screen, custom_sprite=Sprite):
		self.dummy = custom_sprite(img, x, y, screen, dummy=True)
		self.children = []
		screen.add_generator(self)
		return

	def update_children(self):
		for child in self.children:
			child.update()
		return

	def update(self):
		pass
