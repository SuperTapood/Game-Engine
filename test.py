## this is used to test the engine and see if it works ##
from screen import Screen
from colors import *
import pygame
from random import randint as random

if __name__ == "__main__":
	scr = Screen(400, 400)
	while True:
		scr.addRect(random(0, 200), random(0, 200), random(0, 200), random(0, 200), WHITE)
		scr.blit()
		for event in pygame.event.get():
			scr.update(event)
		pygame.display.update()
		scr.empty()