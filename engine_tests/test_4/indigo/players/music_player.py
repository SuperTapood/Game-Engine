from ..objects.engine_object import Engine_Object
from pygame.mixer import Sound
import pygame

class Music_Player(Engine_Object):
	def __init__(self, music_file):
		pygame.mixer.init()
		self.music = Sound(file=music_file)
		return

	def play(self):
		self.music.play()
		return

	def stop(self):
		self.music.stop()
		return

	def set_volume(self, new_volume):
		self.music.set_volume(new_volume)
		return