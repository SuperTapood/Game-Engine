from INDIGO import Screen
from INDIGO.colors import *
from INDIGO.players import Music_Player, Video_Player
from INDIGO import test_screen
from os.path import dirname, join
import cv2
import numpy as np
import pygame
import pygame as pg
from time import time



if __name__ == "__main__":
	# vidcap = cv2.VideoCapture("assets\\video.mp4")
	# pygame.mixer.init()
	# pygame.mixer.music.load("assets\\video.mp3")
	# pygame.mixer.music.play()
	# scr = Screen(360, 360, BLACK)
	# success = True
	# surf = pygame.Surface((360, 360))
	# cap= cv2.VideoCapture("assets\\video.mp4")
	# while success:
	# 	start = time()
	# 	success, image = vidcap.read()
	# 	cv2.imwrite("temp.png", image)
	# 	scr.set_bg_img(pygame.image.load("temp.png"))
	# 	scr.update()
	# 	end = time() - start
	# 	print(end)
	scr = Screen(360, 360, BLACK)
	player = Video_Player(scr, videofile=join(dirname(__file__),"assets\\video.mp4"), soundfile=join(dirname(__file__), "assets\\video.mp3"))
	player.ready()
	true = True
	while true:
		true = player.blit()
	