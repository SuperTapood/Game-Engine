from . import Screen
from .colors import BLACK

def test_screen():
	with Screen(500, 500, BLACK, "TEST") as scr:
		while True:
			scr.update()