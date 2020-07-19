"""
error frame:
class exception(Exception):
	-> this is where I'll provide an explanation to when the error will be raised <-
	# create a class that acts like a REAL exception
	# this is here to make the exception look WAYY better (removes the location where the exception was raised)
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, msg):
		self.msg = msg
		return
	def __str__(self):
		# return the message that will be printed at the end of the exception
		return str
	pass
"""


class GroupAddError(Exception):
	## raise this when the group object gets a non-addable object (non group or engine object) ##
	__module__ = Exception.__module__

	def __init__(self, inst, class_type):
		self.type = str(class_type)[7:]
		self.type = self.type[:-1]
		self.inst = inst
		return

	def __str__(self):
		return f"instance '{self.inst}' of class type {self.type} cannot be added to a Group"


class PlaceholderBlitError(Exception):
	## raise this when the group object gets a non-addable object (non group or engine object) ##
	__module__ = Exception.__module__

	def __init__(self, ph):
		self.ph = ph
		return

	def __str__(self):
		return f"cannot blit dull placeholder {self.ph}"