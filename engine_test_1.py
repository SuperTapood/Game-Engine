from indigo import Screen, Group, Line, Button, BLACK, WHITE, Placeholder, Image
import numpy as np

def get_placeholders():
	global scr
	img_x = Image(r"test1_assets\\x.png")
	img_o = Image(r"test1_assets\\circle.png")
	x = Placeholder(scr, img_x.get_img())
	o = Placeholder(scr, img_o.get_img())
	return x, o

def set_up_buttons():
	global scr
	buttons = Group()
	buttons.append(Button(scr.display, 125, 125, 150, 150, BLACK))
	buttons.append(Button(scr.display, 325, 125, 150, 150, BLACK))
	buttons.append(Button(scr.display, 525, 125, 150, 150, BLACK))
	buttons.append(Button(scr.display, 125, 325, 150, 150, BLACK))
	buttons.append(Button(scr.display, 325, 325, 150, 150, BLACK))
	buttons.append(Button(scr.display, 525, 325, 150, 150, BLACK))
	buttons.append(Button(scr.display, 125, 525, 150, 150, BLACK))
	buttons.append(Button(scr.display, 325, 525, 150, 150, BLACK))
	buttons.append(Button(scr.display, 525, 525, 150, 150, BLACK))
	return buttons



def set_up_board():
	global scr
	board = Group()
	board.append(Line(300, 50, 300, 700, 20, WHITE, scr.display))
	board.append(Line(500, 50, 500, 700, 20, WHITE, scr.display))
	board.append(Line(100, 300, 750, 300, 20, WHITE, scr.display))
	board.append(Line(100, 500, 750, 500, 20, WHITE, scr.display))
	board_array = np.zeros((3, 3)).tolist()
	return board, board_array


if __name__ == "__main__":
	scr = Screen(800, 800, BLACK)
	board, board_array = set_up_board()
	board_buttons = set_up_buttons()
	x, o = get_placeholders()
	while True:
		# board.blit()
		# board_buttons.blit()
		# for i, button in enumerate(board_buttons):
		# 	if button.check_click():
		# 		line = i // 3
		# 		row = i % 3
		# 		print(board_array[line][row])
		scr.update(show_fps=True)