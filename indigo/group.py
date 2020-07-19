from .exceptions import GroupAddError
from .engine_object import Engine_Object

class Group:
	def __init__(self):
		self.objects = []
		self.type = "Group"
		return

	def __add__(self, other):
		print(type(other))
		try:
			if other.type == Group:
				self.objects.multi_add(other.dismantle())
			elif other.type == "Engine_Object":
				self.objects.append(other)
		except AttributeError:
			raise GroupTypeError(other, type(other))
		return

	def multi_add(self, *objs):
		for obj in objs:
			self.objects.append(obj)
		return

	def append(self, other):
		return self + other

	def join(self, other):
		return self + other

	def dismantle(self):
		for obj in self.objects:
			yield obj
		return

	def __str__(self):
		out = ""
		for i, obj in enumerate(self.dismantle()):
			out += f"Group Layer {i} - {str(obj)}\n"
		return out

	def blit(self):
		for obj in self.objects:
			obj.blit()
		return

