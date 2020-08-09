from .exceptions_meta import Exception_Meta

class InvalidBorderButtonError(Exception_Meta):
	# raised when an invalid border button is being created
	def __str__(self):
		rect1_dim, rect2_dim = self.args
		return f"Cannot create a button with dims {rect2_dim} within rect with dims {rect1_dim}"
	pass