import inspect
from ..image import Image
from ..exceptions import NonKillableObjectError

## this is seemingly useless, but this will handle collision later on ##
## the engine object meta classes will talk to each other ##
## to decide if a collision was made ##

class Engine_Object:
	def __init__(self):
		self.type = "Engine_Object"
		try:
			# if this is a img given object, make sure it has a valid image
			if type(self.img) == str:
				self.img = Image(self.img).get_img()
		except AttributeError:
			pass
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

	def process_event(self, event):
		pass

	def get_rekt(self):
		try:
			return self.rect
		except AttributeError:
			return self.img.get_rect()
		return

	def check_coll(self, other):
		ox, oy, ow, oh = other.get_rekt()
		x, y, w, h = self.get_rekt()
		return ox < x < ox + ow and oy < y < oy + oh

	def check_for_collision(self, other, dokilla=False, dokillb=False, respa=lambda:None, respb=lambda:None):
		if self.check_coll(other):
			respa()
			respb()
			if dokilla:
				if not "kill" in dir(self):
					raise NonKillableObjectError(self)
				else:
					self.kill()
			if dokillb:
				if not "kill" in dir(other):
					raise NonKillableObjectError(other)
				else:
					other.kill()
		return

	def check_group_collide(self, group, dokilla=False, dokillb=False, respa=lambda:None, respb=lambda:None):
		for obj in group:
			print(self.check_coll(obj))
			if self.check_coll(obj):
				respa()
				respb()
				if dokilla:
					if not "kill" in dir(self):
						raise NonKillableObjectError(self)
					else:
						self.kill()
				if dokillb:
					if not "kill" in dir(group):
						raise NonKillableObjectError(obj)
					else:
						group.kill(obj)
		return
