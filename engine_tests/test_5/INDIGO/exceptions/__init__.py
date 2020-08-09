"""
error frame:
class exception(Exception_Meta):
	-> this is where I'll provide an explanation to when the error will be raised <-
	def __str__(self):
		# return the message that will be printed at the end of the exception
		params = self.args
		return str
	pass
"""

from .groupAddError             import GroupAddError
from .placeholderBlitError      import PlaceholderBlitError
from .overrideError             import OverrideError
from .nonkillableObjectError    import NonKillableObjectError
from .collideResponseError      import CollideResponseError
from .collideTypeError          import CollideTypeError
from .invalidBorderButtonError  import InvalidBorderButtonError
from .unsupportedExtensionError import UnsupportedExtensionError
from .invalidDeployableError    import InvalidDeployableError
from .unknownShapeError         import UnknownShapeError