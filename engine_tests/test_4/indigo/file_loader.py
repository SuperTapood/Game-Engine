import os
from .players import Video_Player, Music_Player
from .image import Image

sound_extensions = ["ogg"]
video_extensions = ["mp4", "webm"]
image_extension = ["png", "jpeg", "jpg"]

def load_sound(loc):
	return Music_Player(loc)

def load_video(loc):
	return Video_Player(loc)

def load_image(loc):
	return Image(loc)

def load_file(path, file):
	ext = file.split(".")[1]
	loc = path + "\\" + file
	out = ""
	if ext in sound_extensions:
		out = load_sound(loc)
	elif ext in video_extensions:
		out = load_video(loc)
	elif ext in image_extension:
		out = load_image(loc)
	else:
		# raise UnsupportedExtensionError(file, loc, ext)
		pass
	return out


def load_all(path):
	out = []
	for file in os.listdir(path):
		out.append(load_file(path, file))
	return out