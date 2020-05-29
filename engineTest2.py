from screen import Screen
from override import override
from colors import *
from time import time
import pygame
from time import sleep as wait

def fall():
	global JUMP, JTime, scr
	if JUMP and time() - JTime > 0.5:
		JUMP = False
		scr.player.y += 1
		ang = 300
	elif not JUMP:
		scr.player.y += 1
		ang = 300
	elif JUMP:
		ang = 30
	scr.overridePlayerAnim(ang)
	return


## overriding begins here ##
class Screen(Screen):
	@override(Screen)
	def eventHandler(self):
		for event in pygame.event.get():
			self.__quitHandle(event)
			if event.type == pygame.KEYDOWN:
				key = self.__returnKeyName(event)
				if key == "space":
					self.movePlayer()
		fall()
		self.update()

	@override(Screen)
	def movePlayer(self):
		global JUMP, JTime
		JUMP = True
		JTime = time()
		self.player.y += -100
		return

	@override(Screen)
	def overridePlayerAnim(self, ang):
		change = [ang, ang, ang]
		anim = self.player.first
		new = []
		for a, c in zip(anim, change):
			new.append(pygame.transform.rotate(a, c))
		self.player.anim = new
		return
	pass

if __name__ == "__main__":
	global JUMP, JTime, scr
	JUMP = False
	JTime = time() - 5
	scr = Screen()
	scr.fitForBG("folder\\bg.png")
	player = scr.addPlayer("bird", 50, scr.MIDDLEY, scr.loadImagesBasedOnPrefix("folder", "bird"))
	clock = pygame.time.Clock()
	while True:
		if player.y <= 0 or player.y >= scr.MIDDLEY * 2 - 20:
			scr.terminate()
		start = time()
		clock.tick(120)
		scr.eventHandler()
		end = time() - start
		print(f"loop took {end} seconds. {1 / end} FPS")