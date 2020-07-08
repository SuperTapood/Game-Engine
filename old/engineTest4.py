from Game_Engine import Screen, GREEN, override, Sprite, Sprite_Generator, Interactable, Player
import pygame
from time import time
import numpy as np


class Screen(Screen):
	@override(Screen)
	def event_handler(self):
		global x_box, move_factor
		for event in pygame.event.get():
			self.__quit_handle(event)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x_box -= move_factor
			x_box = max(x_box, 0)
			player.reposition(x=x_box)
		elif keys[pygame.K_RIGHT]:
			x_box += move_factor
			x_box = min(x_box, self.X - 50)
			player.reposition(x=x_box)
		self.update()
		return
	pass

class Meteors(Sprite_Generator):
	@override(Sprite_Generator)
	def check_children(self):
		for child in self.children:
			x = child.x
			y = child.y
			if x < 0 or x > self.screen.X:
				if y < 0 or y > self.screen.Y:
					self.remove_child(child)
					self.add_child()
		return
	pass


def func():
	print("hit")


class Meteor(Interactable):
	def __init__(self, scr):
		super().__init__(m_img, scr, dummy=True, touch_conseq=func)
		self.x = np.random.uniform(0, scr.X)
		self.y = 0
		self.speed_x = np.random.uniform(-0.2, 0.2)
		self.speed_y = np.random.uniform(0.1, 0.2)
		return

	def update(self):
		self.x += self.speed_x
		self.y += self.speed_y
		self.check_for_contact(player)
		self.blit()
		return
	pass

if __name__ == "__main__":
	scr = Screen(x=600, y=500, caption="Space Invaders")
	scr.add_clock(400)
	x_box = scr.MIDDLEX
	m_img = scr.load_image("folder\\bird1.png")
	meteors = Meteors(Meteor, scr, kids=20)
	move_factor = 0.5
	p_img = scr.load_image(r"folder\\pipe.png")
	player = Player(p_img, x_box, 400, scr)
	while True:
		scr.event_handler()
		