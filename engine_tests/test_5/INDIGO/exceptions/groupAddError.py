from .exceptions_meta import Exception_Meta

class GroupAddError(Exception_Meta):
	def __str__(self):
		inst, class_type = self.args
		class_type = str(class_type)[7:]
		class_type = type[:-1]
		return f"instance '{self.inst}' of class type {self.type} cannot be added to a Group"