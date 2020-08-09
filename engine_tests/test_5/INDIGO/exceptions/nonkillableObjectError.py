from .exceptions_meta import Exception_Meta


class NonKillableObjectError(Exception_Meta):
	# raised when the engine tries to kill a non killable object
	def __str__(self):
		obj = self.args[0]
		return f"object {obj} has no attribute 'kill' and can't be marked to be killed during collision"