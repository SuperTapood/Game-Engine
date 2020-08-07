class Exception_Meta(Exception):
	__module__ = Exception.__module__

	def __init__(self, *args):
		self.args = args
		return
	pass