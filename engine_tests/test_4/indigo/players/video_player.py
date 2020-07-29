from ..objects.engine_object import Engine_Object
from .music_player import Music_Player
import os

class Video_Player(Engine_Object):
	def __init__(self, video_path):
		self.path = video_path
		self.get_sound()
		super().__init__()
		return

	def get_sound(self):
		# get the audio file
		command = "ffmpeg -i C:\\Users\\yoavo\\Documents\\GitHub\\Game-Engine\\engine_tests\\test_4\\test_4_assets\\video.webm -vn -acodec copy C:\\Users\\yoavo\\Documents\\GitHub\\Game-Engine\\engine_tests\\test_4\\test_4_assets\\output.ogg"
		os.system(f'cmd /k {command}')
		# get the buffer thing
		# load said buffer thing into the music player