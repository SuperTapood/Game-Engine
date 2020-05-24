from colors import *
from screen import Screen
import pygame
from time import time
from time import sleep as wait
from override import override

## overrides ##
class Screen(Screen):
	@override(Screen)
	def eventHandler(self):
		for event in pygame.event.get():
			self.__quitHandle(event)
		self.update()
## end of overrides ##

if __name__ == "__main__":
	scr = Screen(500, 500, BLACK, "Window")
	# scr.fitForBG(r"folder\\bg.png")
	sprite =  scr.addSprite("img", r"folder\\bg.png", 50, 50)
	while True:
		scr.eventHandler()
		start = time()
		# scr.addText("Hello World", scr.MIDDLEX, scr.MIDDLEY, 50)
		btn = scr.addTextButton("Quit", 50, 50, 70, BLACK, WHITE)
		if scr.checkClick(btn):
			sprite.move(50, True, False)
		end = time() - start
		try:
			print(f"loop took {end} seconds. {1 / end} FPS")
		except:
			continue