import os

class Sanity_Check:
	def __init__(self):
		self.__missing_modules = []
		self.__cmd = os.system
		return

	def __call__(self, venv=None, install_missing=False):
		if not venv is None:
			self.__set_venv(venv)
		self.__import_modules()
		print(self)
		if install_missing:
			self.__install_modules()
		elif len(self) > 0:
			self.__notify_install()
		return

	def __repr__(self):
		module = self.__class__.__module__
		class_name = self.__class__.__name__
		memory_location = hex(id(self))
		return f"<{module}.{class_name} object at {memory_location}>"

	def __str__(self):
		out = f"Sanity Check {repr(self)} results:\n"
		if len(self) == 0:
			out += "No missing modules"
		else:
			out += f"Missing Modules:\n"
			for module in self.__missing_modules:
				out += f"{module}\n"
		return out

	def __len__(self):
		return len(self.__missing_modules)

	def __notify_install(self):
		print("\nMissing modules will not be installed")
		return

	def __import_pygame(self):
		try:
			import pygame
		except ModuleNotFoundError:
			self.__missing_modules.append("pygame")
		return

	def __import_numpy(self):
		try:
			import numpy
		except ModuleNotFoundError:
			self.__missing_modules.append("numpy")
		return


	def __import_modules(self):
		self.__import_pygame()
		self.__import_numpy()
		return

	def __set_venv(self, venv):
		self.__cmd(f"activate {venv}")
		return

	def __install_modules(self):
		for module in self.__missing_modules:
			self.__cmd(f"pip install {module}")
		return
