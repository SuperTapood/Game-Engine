"""
error frame:
class exception(Exception):
	-> this is where I'll provide an explanation to when the error will be raised <-
	# create a class that acts like a REAL exception
	# this is here to make the exception look WAYY better (removes the location where the exception was raised
	i.e. main.GroupAddError)
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, params):
		pass
	def __str__(self):
		# return the message that will be printed at the end of the exception
		return str
	pass
"""

from .collideResponseError import CollideResponseError
from .collideTypeError import CollideTypeError
from .groupAddError import GroupAddError
from .invalidBorderButtonError import InvalidBorderButtonError
from .invalidDeployableError import InvalidDeployableError
from .nonkillableObjectError import NonKillableObjectError
from .overrideError import OverrideError
from .placeholderBlitError import PlaceholderBlitError
from .unsupportedExtensionError import UnsupportedExtensionError
