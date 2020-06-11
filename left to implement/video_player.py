from screen import Screen
from frame import get_movies, get_movie
import os
import pygame
from time import sleep as wait


def pre_load_videos(f_path, multiple=True):
	if multiple:
		_ = get_movies(f_path)
	else:
		_ = get_movie(f_path)
	return


class Music_Player:
	def __init__(self, loc):
		self.loc = loc
		return

	def load(self):
		print("Loading music...")
		pygame.mixer.music.load(self.loc)
		pygame.mixer.music.set_volume(1)
		return

	def play(self):
		print("playing music...")
		pygame.mixer.music.play()
		return

	def is_playing(self):
		return pygame.mixer.music.get_busy()
	pass



class Video_Player:
	def __init__(self, f_path, multiple=True):
		self.dict = get_movie(f_path)
		self.music = Music_Player(self.dict["AUDIO_LOCATION"])
		return

	def prepare(self, screen):
		self.screen = screen
		self.music.load()
		print("Loading frames...")
		self.frames = []
		lis = []
		for f in os.listdir(self.dict["IMAGES_LOCATION"])[:-2]:
			lis.append(int(f.split(".")[0][5:]))
		lis.sort()
		for value in lis:
			for file in os.listdir(self.dict["IMAGES_LOCATION"])[:-2]:
				if str(value) == file[5:5+len(str(value))]:
					path = f'{self.dict["IMAGES_LOCATION"]}\\{file}'
					self.frames.append(pygame.image.load(str(path)))
					break
		try:
			screen.shape
		except AttributeError:
			raise TypeError(f"Screen type {type(screen)} is not usable. use Screen object instead.")
		return

	def play(self):
		self.music.play()
		clock = pygame.time.Clock()
		i = 0
		while self.still_playing():
			clock.tick(self.dict["FPS"])
			try:
				self.screen.apply_BG(self.frames[i])
			except IndexError:
				break
			self.screen.eventHandler()
			i += 1
		return

	def still_playing(self):
		return self.music.is_playing()
	pass