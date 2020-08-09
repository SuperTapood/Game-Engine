import pygame


class Music_Player:
	def __init__(self, file_path):
		pygame.mixer.init()
		self.path = file_path
		self.play = pygame.mixer.music.play
		self.pause = pygame.mixer.music.pause
		self.unpause = pygame.mixer.music.unpause
		self.stop = pygame.mixer.music.stop
		self.set_volume = pygame.mixer.music.set_volume
		self.still_playing = pygame.mixer.music.get_busy
		return

	def ready(self):
		pygame.mixer.music.load(self.path)
		return
	pass