from .exceptions_meta import Exception_Meta

class CollideTypeError(Exception_Meta):

	def __str__(self):
		non_group_type = self.args[0]
		return f"class type '{non_group_type}' is not of class type Group"