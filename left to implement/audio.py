import sys
from moviepy.editor import *

fpath = "C:\\Users\\SuperTapood\\Documents\\GitHub\\Python-Game\\(Original) Ultimate Custom Night in a Nutshell-lRLEGyo8BEs.mp4"
def get_audio(file_loc, f_path, name):
	video = VideoFileClip(file_loc)
	audio = video.audio
	audio.write_audiofile(f"{f_path}\\{name}.mp3")
	return f"{f_path}\\{name}.mp3"