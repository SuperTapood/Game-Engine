from screen import Screen
from sprite import Sprite
from player import Player
from sprite_generator import Sprite_Generator
import pygame
from override import override


class Base(Sprite):
	@override(Sprite)
	def update(self):
		self.move_x(-1)
		left_x = self.x + self.WIDTH
		if left_x <= 0:
			self.set_defaults(self.screen.X, self.y)
		return
	pass

class Bird(Player):
	@override(Player)
	def __init__(self, imgs, x, y, screen):
		super().__init__(imgs, x, y, screen)
		self.flapping = False
		return

	@override(Player)
	def input(self, event):
		if event.type == pygame.KEYDOWN:
			event = self.screen.return_key_name(event)
			if event == "space":
				self.flap()
		return

	def flap(self):
		self.flapping = True
		self.move_smoothly_y(-30, 10)
		return

	def fall(self):
		self.move_y(1)
		self.check_death()
		return

	@override(Player)
	def update(self):
		self.blit()
		self.smooth()
		if not self.flapping:
			self.fall()
		if self.x_remain <= 0:
			self.flapping = False
		return

	def check_death(self):
		if self.y >= base_y - 20 or self.y <= 0:
			lose()
		return
	pass

class Pipe_Generator(Sprite_Generator):
	pass



def lose():
	print(f"YOU LOST WITH A SCORE OF {score}")
	exit()
	return

if __name__ == "__main__":
	scr = Screen()
	score = 0
	scr.fit_for_BG(r"folder\\bg.png")
	base_img = scr.load_image(r"folder\\base.png")
	bird_imgs = list(scr.load_images_based_on_prefix(r"folder", "bird"))
	pipe_img = scr.load_image(r"folder\\pipe.png")
	base_y = 450
	base = Base(base_img, scr.X - 336, base_y, scr)
	base2 = Base(base_img, scr.X, base_y, scr)
	bird = Bird(bird_imgs, 50, scr.MIDDLEY, scr)
	pipes = Pipe_Generator(pipe_img, 50, 50, scr)
	scr.add_clock(60)
	while True:
		scr.add_text(str(score), scr.MIDDLEX, 50, 50)
		scr.event_handler()