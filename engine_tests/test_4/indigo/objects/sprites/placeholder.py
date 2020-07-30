from ..exceptions import PlaceholderBlitError
from ..exceptions import CollideTypeError
from ..exceptions import InvalidDeployableError
from .engine_object import Engine_Object
from ...collision import sprite_sprite_collision, sprite_group_collision
from inspect import signature


class Placeholder(Engine_Object):
	def __init__(self, scr, img, x=None, y=None, delpoyable=Placeholder):
		self.scr = scr
		self.img = img
		self.x = x
		self.y = y
		if len(signature(delpoyable).__init__) != 2:
			raise InvalidDeployableError(delpoyable.__name__)
		self.delpoyable = delpoyable
		super().__init__()
		return

	def deploy(self, x, y):
		return self.clone(x, y)

	def clone(self, x, y):
		return self.delpoyable(self.scr, self.img, x, y)

	def blit(self):
		if self.x is None or self.y is None:
			raise PlaceholderBlitError(self, self.x, self.y)
		else:
			self.scr.blit(self.img, self.x, self.y)
		return

	def check_collide(self, other, resp):
		if hasattr(other, "object_type"):
			if other.object_type == "Group":
				sprite_group_collision(self, other, resp)
			elif other.object_type == "Engine_Object":
				sprite_sprite_collision(self, other, resp)
			else:
				raise CollideTypeError(type(other).__name__)
		else:
			raise CollideTypeError(type(other).__name__)
		return