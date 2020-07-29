from ..exceptions import CollideResponseError, CollideTypeError
from inspect import signature

def check_valid_resp(resp):
	if len(signature(resp).parameters) != 2:
		raise CollideResponseError(resp.__name__)
	return

def check_valid_group(group):
	if hasattr(group, "object_type"):
		if group.object_type == "Group":
			return
	raise CollideTypeError(type(group).__name__)