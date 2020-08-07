## PLAYERS TESTING AND BUILDING ##


from pydub import AudioSegment
from pygame.mixer import Sound, init
from indigo import Screen
from indigo.colors import *
import pygame, mutagen.mp3, wave
from pydub.playback import play
import os


if __name__ == "__main__":
	"""
	ffmpeg -i [INPUT] -vn -acodec copy [OUTPUT]
	"""
	# print(1 / 0.004126925945281982)
	# exit()
	scr = Screen(700, 700, BLACK)
	video_path = "assets\\video.mp4"
	sound_path = os.path.join(os.path.dirname(__file__), "assets\\video.ogg")
	video_name = video_path.split("\\")[1].split(".")[0]
	os.system(f"ffmpeg -i {video_path} -vn -acodec copy {sound_path}")
	os.system(f"ffmpeg -i {sound_path} -ar 48000 {sound_path}")
	pygame.mixer.init(48000, -16, 1, 1024)
	pygame.mixer.Sound(sound_path).play()
	# sound = AudioSegment.from_mp3("assets\\audio.mp3")

	# # sound._data is a bytestring
	# raw_data = sound._data

	# file_wav = wave.open("assets\\audio.wav")
	# frequency = file_wav.getframerate()
	# print(frequency)
	# pygame.mixer.init(frequency=frequency)
	# mp3 = mutagen.mp3.MP3("assets\\audio.mp3")
	# beep = pygame.mixer.Sound(raw_data)
	# beep.play()
	while True:
		scr.update()
