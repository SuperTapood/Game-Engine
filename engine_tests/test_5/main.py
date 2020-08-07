from INDIGO import Screen
from INDIGO.objects.shapes import Rect
from INDIGO import convert
from INDIGO.colors import *


if __name__ == "__main__":
	convert = convert()
	scr = Screen(500, 500, BLACK)
	test_shape = Rect(scr, WHITE, 50, 50, 50, 50)
	test_shape = convert.to_button(test_shape, exit)
	while True:
		test_shape.blit()
		scr.update()