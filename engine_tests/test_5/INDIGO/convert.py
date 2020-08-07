from .objects.buttons import *
from .exceptions import UnknownShapeError

class convert:
	def __switch(self, value):
		self.__switch_x_value = value
		return

	def __case(self, value):
		return self.__switch_x_value == value

	def __get_shape_type(self, shape):
		class_name = shape.__class__.__name__
		return class_name

	def __circle_to_button(self, circle, func):
		return Circle_Button(circle.scr, circle.color, circle.pos[0], circle.pos[1], circle.r, func)

	def __rect_to_button(self, rect, func):
		return Button(rect.scr, rect.x, rect.y, rect.w, rect.h, rect.color, func)

	def __get_proper_shape_func_button(self, in_type):
		func = None
		self.__switch(in_type)
		case = self.__case
		if case("Circle"):
			func = self.__circle_to_button
		# elif case("Rect"):
		# 	func = self.__rect_to_button
		if func is None:
			raise UnknownShapeError(in_type)
		return func

	def to_button(self, shape, func):
		shape_type = self.__get_shape_type(shape)
		constructor = self.__get_proper_shape_func_button(shape_type)
		return constructor(shape, func)