class UnsupportedExtensionError(Exception):
	__module__ = Exception.__module__

	def __init__(self, file, loc, typ):
		self.file = file
		self.loc = loc[:-len(file) - 1]
		self.type = typ
		return

	def __str__(self):
		return f"File '{self.file}' at location '{self.loc}' of type '{self.type}' cannot be loaded"