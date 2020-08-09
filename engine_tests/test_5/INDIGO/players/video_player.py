from . import Music_Player
from cv2 import imwrite, VideoCapture, imread
from os import remove
from shutil import move
import subprocess
from time import time
import pygame

class Video_Player:
	def __init__(self, scr, videofile, soundfile):
		self.video = VideoCapture(videofile)
		self.sound = Music_Player(soundfile)
		self.ready = self.sound.ready
		self.is_done = self.sound.still_playing
		self.__blit = scr.set_bg_img
		_, image = self.video.read()
		dims = image.shape[:2]
		scr.reshape(dims[0], dims[1])
		frames = self.__get_frames()
		duration = self.__get_length(videofile)
		self.__spf = frames / duration
		self.__frame_loc = 0
		self.__time_last = 0
		return

	def __get_length(self, filename):
	    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
	                             "format=duration", "-of",
	                             "default=noprint_wrappers=1:nokey=1", filename],
	        stdout=subprocess.PIPE,
	        stderr=subprocess.STDOUT)
	    return float(result.stdout)

	def __get_frames(self):
		true = True
		i = 0
		while true:
			true, _ = self.video.read()
			i += 1
		return i

	def blit(self):
		if not self.is_done:
			self.sound.play()
		if time() - self.__time_last > self.__spf:
			true, img = self.video.read()
			assert true
			imwrite("temp.png", img)
			self.__blit(pygame.image.load("temp.png"))
			self.__frame_loc += 1
			self.__time_last = time()
		return self.is_done()
