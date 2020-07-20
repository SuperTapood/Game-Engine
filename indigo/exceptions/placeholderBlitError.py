class PlaceholderBlitError(Exception):
	## raise this when the group object gets a non-addable object (non group or engine object) ##
	__module__ = Exception.__module__

	def __init__(self, ph, x, y):
		self.x = x
		self.y = y
		self.ph = ph
		return

	def __str__(self):
		return f"cannot blit placeholder {self.ph} to pos ({self.x}, {self.y})"