from indigo import Screen
from indigo import BLACK
from indigo import Image
from indigo import Placeholder
from indigo import Group
from indigo import override
from indigo import Player
from indigo import Test_Counter

import pygame
import random


class Bullet(Placeholder):
	def blit(self):
		self.y -= 10
		super().blit()
		return

	@override(Placeholder)
	def clone(self, x, y):
		return Bullet(self.scr, self.img, x, y)
	pass


class Ship(Player):
	@override(Player)
	def process_event(self, event):
		if event.type == pygame.KEYDOWN:
			key = event.unicode
			if key == "a":
				self.move_smoothly("x", -1000, 750)
			elif key == "d":
				self.move_smoothly("x", 1000, 750)



class Meteor(Placeholder):
	@override(Placeholder)
	def __init__(self, screen, image, x=None, y=None, gravity_multiply=1):
		super().__init__(screen, image, x, y)
		self.g = gravity_multiply
		return

	@override(Placeholder)
	def blit(self):
		self.y += gravity * self.g
		super().blit()
		return

	@override(Placeholder)
	def clone(self, x, y, g):
		return Meteor(self.scr, self.img, x, y, g)

	@override(Placeholder)
	def deploy(self, x, y, g):
		return self.clone(x, y, g)
	pass


if __name__ == "__main__":
	gravity = 1
	scr = Screen(700, 700, BLACK, "SPACE INVADERS")
	bg = Image("test2_assets\\spaceBG.png")
	bg.resize(700, 700)
	max_meteors = 10
	meteor = Meteor(scr, "test2_assets\\meteor.png")
	meteors = Group()
	ship = Ship(scr, "test2_assets\\spaceShip1.png", 350, 600)
	bullets = Group()
	bullet = Bullet(scr, "test2_assets\\bullet.png")
	test = Test_Counter()
	for i in range(2000):
		test.start()
		scr.set_bg_img(bg.get_img())
		meteors.blit()
		ship.blit()
		bullets.blit()
		ship.check_group_collide(meteors, respa=lambda: exit())
		meteors.eliminate(lambda obj: obj.x >= 700 or obj.y >= 700)
		if len(meteors) < max_meteors:
			meteors.append(meteor.deploy(random.randint(0, 700), -50,  random.uniform(0.5, 1.5)))
		for event in pygame.event.get():
			scr.quit_handler(event)
			ship.process_event(event)
			if event.type == pygame.KEYDOWN:
				if chr(event.key) == "w":
					bullets.append(bullet.deploy(ship.x + 50, ship.y - ship.get_rekt().h))
		pygame.display.update()
		test.lap()
	print(test)