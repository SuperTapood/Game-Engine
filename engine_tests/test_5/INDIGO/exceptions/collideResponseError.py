from .exceptions_meta import Exception_Meta

class CollideResponseError(Exception_Meta):
	def __str__(self):
		func_name = self.args[0]
		return f"function '{func_name}' does not take exactly 2 arguments and cannot be used as a collide response"