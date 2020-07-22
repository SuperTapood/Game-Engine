from .engine_object import Engine_Object

class Player(Engine_Object):
	def __init__(self, x, y, up, down, left, right, movement_frames):
		self.actions = [up, down, left, right]
		self.responses = [self.up, self.down, self.left, self.right]
		self.x = x
		self.y = y
		self.frames = movement_frames
		self.remain_smooth = 0
		return

	def blit(self):
		for action, resp in zip(self.actions, self.responses):
			if action():
				resp()
		self.screen.blit(self.mask, (self.x, self.y))
		return

	def up(self):
		pass

	def down(self):
		pass

	def right(self):
		pass

	def left(self):
		pass