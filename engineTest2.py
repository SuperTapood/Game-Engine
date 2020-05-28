from screen import Screen
from override import override
from colors import *
from time import time


if __name__ == "__main__":
	scr = Screen(500, 500, BLACK, "Flappy Bird")
	while True:
		start = time()
		scr.eventHandler()
		end = time() - start
		print(f"loop took {end} seconds")