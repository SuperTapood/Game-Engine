from Game_Engine import Screen, GREEN, override, Sprite, Sprite_Generator
import pygame
from time import time
import numpy as np


class Screen(Screen):
	@override(Screen)
	def event_handler(self):
		global x_box, move_factor, scr
		for event in pygame.event.get():
			self.__quit_handle(event)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x_box -= move_factor
			x_box = max(x_box, 0)
		elif keys[pygame.K_RIGHT]:
			x_box += move_factor
			x_box = min(x_box, scr.X - 50)
		self.update()
		return
	pass

class Meteors(Sprite_Generator):
	@override(Sprite_Generator)
	def check_children(self):
		print(len(self.children))
		for child in self.children:
			x = child.x
			y = child.y
			if x < 0 or x > self.screen.X:
				if y < 0 or y > self.screen.Y:
					self.remove_child(child)
					self.add_child()
		return




class Meteor(Sprite):
	def __init__(self, scr, dummy=False):
		super().__init__(m_img, 0, 0, scr, dummy=dummy)
		self.x = np.random.uniform(0, scr.MIDDLEX)
		self.y = np.random.uniform(0, -200)
		self.speed_x = np.random.uniform(0, 0.2)
		self.speed_y = np.random.uniform(0, 0.2)
		return

	def update(self):
		self.x += self.speed_x
		self.y += self.speed_y
		return



if __name__ == "__main__":
	scr = Screen(x=600, y=500, caption="Space Invaders")
	x_box = scr.MIDDLEX
	m_img = scr.load_image("folder\\bird1.png")
	meteors = Meteors(Meteor, scr, kids=8)
	move_factor = 0.5
	while True:
		scr.event_handler()
		player = scr.add_button(x_box, 425, 50, 50, GREEN)