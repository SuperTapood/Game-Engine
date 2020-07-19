from indigo import Screen, Group, Line, Button, BLACK, WHITE
import numpy as np

def set_up_buttons():
	buttons = Group()
	return buttons



def set_up_board():
	global scr
	board = Group()
	board.append(Line(300, 50, 300, 700, 20, WHITE, scr.display))
	board.append(Line(500, 50, 500, 700, 20, WHITE, scr.display))
	board.append(Line(100, 300, 750, 300, 20, WHITE, scr.display))
	board.append(Line(100, 500, 750, 500, 20, WHITE, scr.display))
	board_array = np.zeros((3, 3))
	return board, board_array


if __name__ == "__main__":
	scr = Screen(800, 800, BLACK)
	board, board_array = set_up_board()
	board_buttons = set_up_buttons()
	while True:
		board.blit()
		scr.update(show_fps=True)