from screen import Screen
from colors import *
from random import randint
from override import override
import pygame



if __name__ == "__main__":
	scr = Screen(500, 500, BLACK, "Guessing Game")
	input1 = scr.addInputField(50, 50, 50, WHITE)
	while True:
		print(input1.active)
		scr.updateField(input1)
		scr.eventHandler()