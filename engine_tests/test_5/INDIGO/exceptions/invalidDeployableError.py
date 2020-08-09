from .exceptions_meta import Exception_Meta

class InvalidDeployableError(Exception_Meta):
	# raised when a non-deployable object is being defined as deployable
	def __str__(self):
		class_name = self.args[0]
		return f"{class_name} cannot be used a deployable"