from Game_Engine.screen import Screen
from Game_Engine.scene import Scene
from Game_Engine.colors import *
from time import time


class Game_Data:
	def __init__(self):
		self.min = 0
		self.max = 0
		self.guess = 0
		self.turns = 0
		return

	def get_min(self):
		return str(self.min)

	def add_min(self):
		self.min += 1
		return

	def sub_min(self):
		self.min -= 1
		return

	def get_max(self):
		return str(self.max)

	def add_max(self):
		self.max += 1
		return

	def sub_max(self):
		self.max += 1
		return

def set_up_scenes(screen):
	global game
	# set up the settings scene
	setting = Scene(screen)
	setting.add_text(game.get_min, 250, 100, 50)
	setting.add_text("MIN:", 100, 100, 50)
	setting.add_text_button("+", 350, 70, 50, BLACK, WHITE, check_click=True, click_result=game.add_min)
	setting.add_text_button("-", 400, 70, 50, BLACK, WHITE, check_click=True, click_result=game.sub_min)
	setting.add_text(game.get_max, 250, 200, 50)
	setting.add_text("MAX:", 100, 200, 50)
	setting.add_text_button("+", 350, 170, 50, BLACK, WHITE, check_click=True, click_result=game.add_max)
	setting.add_text_button("-", 400, 170, 50, BLACK, WHITE, check_click=True, click_result=game.sub_max)
	str(setting)
	exit()
	guess = Scene(screen)
	return setting, guess



if __name__ == "__main__":
	scr = Screen()
	game = Game_Data()
	choose_range_scene, guess_scene = set_up_scenes(scr)
	while True:
		s = time()
		scr.event_handler()
		choose_range_scene.load()
		e = time() - s
		print(1 / e)
