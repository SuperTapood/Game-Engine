## SPACE INVADERS ##
## ENGINE TEST PASSED? (some animation latency) ##
## AVERAGE SPF (Seconds Per Frame) - 0.007917278051376342 ##
## ABOUT 126.30603516901363 FPS :D ##
## THIS IS GREAT BECAUSE WE HAVE 11 OBJECTS ON SCREEN ALL THE TIME ##
## THIS IS GOING BETTER THEN EXPECTED ##


from indigo import Screen
from indigo import BLACK, WHITE
from indigo import Image
from indigo import Placeholder
from indigo import Group
from indigo import override
from indigo import Player
from indigo import Test_Counter
from indigo import sprite_group_collision
from indigo import group_group_collision
from indigo import Label
from indigo import Animation

import pygame
import random
import numpy as np


# collision result functions
def ship_meteor_collide(a, b):
	global score, small_splode, splodes
	# a - ship
	# b - meteor
	meteors.kill(b)
	score -= 1
	splodes.append(small_splode.play(b.x, b.y))
	return

def meteor_bullet_collide(a, b):
	global score, big_splode, splodes
	splodes.append(big_splode.play(b.x, b.y))
	meteors.kill(a)
	bullets.kill(b)
	score += 1
	return

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
	print(1 / 0.007917278051376342)
	exit()
	gravity = 1
	score = 0
	scr = Screen(700, 700, BLACK, "SPACE INVADERS")
	bg = Image("test2_assets\\spaceBG.png")
	bg.resize(700, 700)
	max_meteors = 8
	meteor = Meteor(scr, "test2_assets\\meteor.png")
	meteors = Group()
	ship = Ship(scr, "test2_assets\\spaceShip1.png", 350, 600)
	ship.set_rect()
	bullets = Group()
	bullet = Bullet(scr, "test2_assets\\bullet.png")
	test = Test_Counter()
	big_splode = Animation(scr, r"test2_assets\\Explosions").resize(75, 75)
	small_splode = Animation(scr, r"test2_assets\\Explosions").resize(25, 25)
	splodes = Group()
	for i in range(5000):
		print(i)
		test.start()
		scr.set_bg_img(bg.get_img())
		meteors.blit()
		ship.blit()
		bullets.blit()
		splodes.blit()
		splodes.eliminate(lambda obj: obj.wd == len(obj.images))
		meteors.eliminate(lambda obj: obj.x >= 700 or obj.y >= 700)
		if len(meteors) < max_meteors:
			meteors.append(meteor.deploy(random.randint(0, 650), -50,  random.uniform(0.5, 1.5)))
			meteors[-1].set_rect()
		for event in pygame.event.get():
			scr.quit_handler(event)
			ship.process_event(event)
			if event.type == pygame.KEYDOWN:
				if chr(event.key) == "w":
					bullets.append(bullet.deploy(ship.x + 50, ship.y - ship.rect.h))
					bullets[-1].set_rect()
		ship.x = min([ship.x, 700 - ship.rect.w])
		ship.x = max([ship.x, 0])
		sprite_group_collision(ship, meteors, ship_meteor_collide)
		group_group_collision(meteors, bullets, meteor_bullet_collide)
		Label(scr, str(score), 20, 20, 50, WHITE).blit()
		pygame.display.update()
		test.lap()
	print(test)