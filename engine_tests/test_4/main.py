from indigo.objects.shapes import Polygon
from indigo import Screen
from indigo.colors import *
from pygame.draw import polygon






if __name__ == "__main__":
	scr = Screen(500, 500, BLACK)
	btn = Polygon(scr, WHITE, (75, 75), (125, 125), (325, 100), (550, 10))
	while True:
		btn.blit()
		scr.update()