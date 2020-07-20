import pygame
from time import time


class Screen:
	def __init__(self, x, y, bg_color, caption="pygame window"):
		pygame.init()
		self.X = x
		self.Y = y
		self.bg_color = bg_color
		self.display = pygame.display.set_mode((x, y))
		pygame.display.set_caption(caption)
		return

	def update(self, show_fps=False):
		start = time()
		for event in pygame.event.get():
			self.quit_handler(event)
		pygame.display.update()
		end = time() - start
		if show_fps:
			try:
				print(f"{1 / end} FPS")
			except ZeroDivisionError:
				print(f"1000.0 FPS (end time is 0)")
		return

	def quit_handler(self, event):
		if event.type == pygame.QUIT:
			self.quit()
		return

	def quit(self):
		exit()
		return