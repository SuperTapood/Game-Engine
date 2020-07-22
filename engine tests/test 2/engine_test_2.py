from indigo import Screen
from indigo import BLACK
from indigo import Image
from indigo import Placeholder
from indigo import Group
from indigo import override
from indigo import Player
from indigo import blank
from indigo import W_DOWN
from indigo import D_DOWN
from indigo import A_DOWN

import random


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



if __name__ == "__main__":
	gravity = 1
	scr = Screen(700, 700, BLACK, "SPACE INVADERS")
	bg = Image("test2_assets\\spaceBG.png")
	bg.resize(700, 700)
	max_meteors = 10
	meteor_img = Image("test2_assets\\meteor.png")
	meteor = Meteor(scr, meteor_img.get_img())
	meteors = Group()
	ship = Player(50, 50, blank, blank, A_DOWN, D_DOWN, 10)
	while True:
		scr.set_bg_img(bg.get_img())
		meteors.blit()
		ship.blit()
		meteors.eliminate(lambda obj: obj.x >= 700 or obj.y >= 700)
		if len(meteors) < max_meteors:
			meteors.append(meteor.deploy(random.randint(0, 700), -50,  random.uniform(0.5, 2)))
		scr.update()