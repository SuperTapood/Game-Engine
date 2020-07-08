from Game_Engine import *
import pygame
from time import time


class Screen(Screen):
	@override(Screen)
	def event_handler(self):
		for event in pygame.event.get():
			self.__quit_handle(event)
			if event.type == pygame.KEYDOWN:
				key = pygame.key.name(event.key)
				self.__sendInputToFields(key)
		self.update()
		return

def test(guess, num):
	t = False
	r = ""
	if guess == num:
		t = True
	if guess > num:
		r = "bigger"
	elif num > guess:
		r = "smaller"
	return f"the number you guessed is {r} then the actual number", t

def start(mi, ma):
	rand = random(mi, ma)
	print(rand)
	scr.delAllFields()
	true = False
	resp = ""
	while not true:
		scr.eventHandler()
		scr.addText("Guess the number!!", scr.MIDDLEX, 50, 50)
		scr.addText("Your guess:", scr.MIDDLEX, 150, 50)
		guess = scr.addField("guess", None, scr.MIDDLEX - 100, 220, 50)
		scr.addText(resp, scr.MIDDLEX, 300, 17)
		testbtn = scr.addTextButton("Test", scr.MIDDLEX - 50, 400, 50, BLACK, WHITE)
		if scr.checkClick(testbtn):
			resp, true = test(int(guess.txt), rand)
	end()
	return

def displayBegin():
	global start
	scr.add_text("Guessing Game", 250, 50, 50)
	scr.add_text("minimum: ", 130, 150, 50)
	mi = scr.add_field("Minimum", None, 330, 120, 50, emptyLength=8)
	scr.add_text("maximum: ", 140, 250, 50)
	ma = scr.add_field("Maximum", None, 330, 220, 50, emptyLength=8)
	startB = scr.add_text_button("Start", 230, 400, 50, BLACK, WHITE)
	if scr.check_click(startB):
		mini = int(mi.txt)
		maxi = int(ma.txt)
		start(mini, maxi)
		return
	return



if __name__ == "__main__":
	scr = Screen(500, 500, BLACK, "Guessing Game")
	while True:
		won = False
		while not won:
			scr.event_handler()
			t = time()
			displayBegin()
			# start(1, 5)		
			e = time() - t
			print(f"loop took {e} seconds, FPS = {1 / e}")
