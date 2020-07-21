import inspect

## this is seemingly useless, but this will handle collision later on ##
## the engine object meta classes will talk to each other ##
## to decide if a collision was made ##

class Engine_Object:
	def __init__(self):
		self.type = "Engine_Object"
		return

	# we also got this sick useless function
	def get_attributes(self, output=False):
		att_dict = {}
		memebers = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
		for memeber in memebers:
			attribute = memeber[0]
			value = memeber[1]
			# exclude builtin attributes
			if not attribute[:2] == attribute[-2:] == "__":
				att_dict[attribute] = value
		if output:
			print(att_dict)
		return att_dict