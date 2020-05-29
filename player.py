import pygame

class Player:
	def __init__(self, name, x, y, anim):
		self.name = name
		self.x = x
		self.y = y
		self.anim = list(anim)
		self.first = self.anim
		self.animIndex = 0
		self.currentAnim = self.anim[0]
		return

	def blit(self, window):
		window.blit(self.currentAnim, (self.x, self.y))
		self.animIndex += 1
		if self.animIndex == len(self.anim):
			self.animIndex = 0
		self.currentAnim = self.anim[self.animIndex]
		return