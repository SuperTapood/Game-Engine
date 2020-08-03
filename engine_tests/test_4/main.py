from indigo.objects.buttons import Input_Field
from indigo import Screen
from indigo.colors import *





if __name__ == "__main__":
	scr = Screen(500, 500, BLACK)
	btn = Input_Field(scr, scr.MIDDLEX, scr.MIDDLEY, 20, WHITE, GREEN, 5)
	while True:
		btn.blit()
		print(btn.active)
		scr.update()