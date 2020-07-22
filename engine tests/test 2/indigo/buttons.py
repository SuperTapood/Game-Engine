import pygame


def key_down(event, key):
	if event.type == pygame.KEYDOWN:
		return event.key == key

def blank(event):
	return False

def W_DOWN(event):
	return key_down(event, "w")

def D_DOWN(event):
	return key_down(event, "d")

def A_DOWN(event):
	return key_down(event, "a")