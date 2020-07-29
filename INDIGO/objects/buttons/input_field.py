from ..engine_object import Engine_Object
from .text_button import Text_Button

class Input_Field(Engine_Object):
	def __init__(self, scr, x, y, txt_size, txt_color, button_color, max_len):
		self.max_len = max_len
		self.txt = ""
		self.active = False
		self.button = Text_Button(scr, self.get_text(), x, y, txt_size, txt_color, button_color, self.change_active_state)
		return

	def get_text(self):
		if len(self.txt) == self.max_len:
			out = self.txt
		elif len(self.txt) > self.max_len:
			out = self.txt[:self.max_len]
		else:
			out = self.txt + " " * (self.max_len - len(self.txt))
		return out 

	def blit(self):
		self.button.blit()
		return

	def change_active_state(self):
		self.active = not self.active
		return

	def update_text(self, txt):
		if self.active:
			self.txt += txt
			self.button.update_text(self.get_text())
		return