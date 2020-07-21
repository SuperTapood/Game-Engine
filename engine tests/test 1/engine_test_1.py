## TIC TAC TOE ##
## ENGINE TEST PASSED ##
## AVERAGE SPF (Seconds Per Frame) - 0.0009691522105062035 ##
## ABOUT 1031.8296642770738 FPS :D ##

from indigo import Screen
from indigo import Group
from indigo import Line
from indigo import Button
from indigo import BLACK
from indigo import WHITE
from indigo import Placeholder
from indigo import Image
from indigo import Test_Counter
# from indigo import counter
import numpy as np
from time import time


def check_win(board):
	out = False
	players = ["x", "o"]
	for row in board:
		if row[0] == row[1] == row[2] != 0:
			out = f"{players[row[0] - 1]} won"
	for i in range(len(board)):
		if board[0][i] == board[1][i] == board[2][i] != 0:
			out = f"{players[board[0][i] - 1]} won"
	if board[0][0] == board[1][1] == board[2][2] != 0:
		out = f"{players[board[0][0] - 1]} won"
	if board[0][2] == board[1][1] == board[2][0] != 0:
		out = f"{players[board[0][2] - 1]} won"
	return out

def set_up_locs():
	loc_array = [[[120, 100], [320, 100], [550, 100]],
				[[120, 330], [320, 330], [520, 330]], 
				[[120, 530], [320, 530], [550, 530]]]
	return loc_array


def get_placeholders():
	global scr
	img_x = Image(r"test1_assets\\x.png")
	img_x.rescale(0.1)
	img_o = Image(r"test1_assets\\circle.png")
	img_o.rescale(0.3)
	x = Placeholder(scr, img_x.get_img())
	o = Placeholder(scr, img_o.get_img())
	return x, o

def set_up_buttons():
	global scr
	buttons = Group()
	buttons.append(Button(scr.display, 125, 125, 150, 150, WHITE))
	buttons.append(Button(scr.display, 325, 125, 150, 150, WHITE))
	buttons.append(Button(scr.display, 525, 125, 150, 150, WHITE))
	buttons.append(Button(scr.display, 125, 325, 150, 150, WHITE))
	buttons.append(Button(scr.display, 325, 325, 150, 150, WHITE))
	buttons.append(Button(scr.display, 525, 325, 150, 150, WHITE))
	buttons.append(Button(scr.display, 125, 525, 150, 150, WHITE))
	buttons.append(Button(scr.display, 325, 525, 150, 150, WHITE))
	buttons.append(Button(scr.display, 525, 525, 150, 150, WHITE))
	return buttons



def set_up_board():
	global scr
	board = Group()
	board.append(Line(300, 50, 300, 700, 20, BLACK, scr.display))
	board.append(Line(500, 50, 500, 700, 20, BLACK, scr.display))
	board.append(Line(100, 300, 750, 300, 20, BLACK, scr.display))
	board.append(Line(100, 500, 750, 500, 20, BLACK, scr.display))
	board_array = np.zeros((3, 3)).tolist()
	return board, board_array


if __name__ == "__main__":
	scr = Screen(800, 800, WHITE)
	board, board_array = set_up_board()
	board_buttons = set_up_buttons()
	x, o = get_placeholders()
	ph_locs = set_up_locs()
	tics_and_tacs = Group()
	players = [x, o]
	current = 0
	true = True
	result = False
	win_delay = 0.1
	while true:
		start = time()
		scr.fill(scr.bg_color)
		board.blit()
		board_buttons.blit()
		tics_and_tacs.blit()
		if result is False:
			for i, button in enumerate(board_buttons):
				if button.check_click():
					line = i // 3
					row = i % 3
					if board_array[line][row] == 0.0:
						chosen = ph_locs[line][row]
						x = chosen[0]
						y = chosen[1]
						tics_and_tacs.append(players[current].deploy(x, y))
						board_array[line][row] = current + 1
						result = check_win(board_array)
						if result is not False:
							print(result)
							break
						current = abs(current - 1)
		if result is not False:
			win_delay -= (time() - start)
			if win_delay < 0:
				break
		scr.update()
