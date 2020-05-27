## decorator for overriding ##

def override(interface_class):
	# assert im overriding an existing method
	def overrider(method):
		try:
			assert(method.__name__ in dir(interface_class))
			return method
		except AssertionError:
			exit(f'EngineOverrideError: Method "{method.__name__}" does not exist')
	return overrider