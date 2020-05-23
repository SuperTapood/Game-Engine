from colors import *
from screen import Screen
import pygame
from time import time
from time import sleep as wait

class Screen(Screen):
	def eventHandler(self):
		## override ##
		for event in pygame.event.get():
			self.__quitHandle(event)
		self.update()

if __name__ == "__main__":
	scr = Screen(500, 500, BLACK, "Window")
	scr.fitForBG(r"folder\\bg.png")
	while True:
		start = time()
		scr.eventHandler()
		scr.addText("Hello World", scr.MIDDLEX, scr.MIDDLEY, 50)
		btn = scr.addTextButton("Quit", 50, 50, 70, BLACK, WHITE)
		if scr.checkClick(btn):
			scr.terminate()
		end = time() - start
		print(f"loop took {end} seconds")