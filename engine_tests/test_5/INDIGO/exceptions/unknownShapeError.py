from .exceptions_meta import Exception_Meta

class UnknownShapeError(Exception_Meta):
	def __str__(self):
		shape_type = self.args[0]
		return f"Shape of type {shape_type} is not supported"