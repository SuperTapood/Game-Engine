## decorator for overriding ##

def override(interface_class):
	# assert im overriding an existing method
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider