from .button import Button
from ..label import Label
from ..engine_object import Engine_Object

class Text_Button(Engine_Object):
	def __init__(self, scr, txt, x, y, txt_size, txt_color, button_color, resp, button_width=0):
		self.att_tuple = (scr, x, y, txt_size, txt_color, button_color, resp, button_width)
		rect = Label(scr, txt, x, y, txt_size, txt_color).get_rekt()
		x, y, w, h = rect
		self.button = Button(scr, x, y, w, h, button_color, resp, button_width)
		self.text = Label(scr, txt, x, y, txt_size, txt_color)
		return

	def blit(self):
		self.button.blit()
		self.text.blit()
		return

	def update_text(self, new_txt):
		scr, x, y, txt_size, txt_color, button_color, resp, button_width = self.att_tuple
		rect = Label(scr, new_txt, x, y, txt_size, txt_color).get_rekt()
		x, y, w, h = rect
		self.button = Button(scr, x, y, w, h, button_color, resp, button_width)
		self.text = Label(scr, new_txt, x, y, txt_size, txt_color)
		return