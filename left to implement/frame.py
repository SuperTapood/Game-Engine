import cv2 
import os
import moviepy.editor
import json
from audio import get_audio
import sys
from os import system, name
from numba import jit


ACCEPTED_FORMATS = [".mp4", "webm", ".mkv"]


def get_movie(f_path):
    folder_name_full = f_path.split("\\")[-1]
    folder_name = folder_name_full[0:-4]
    try:
        print(f"Attempting to open file {folder_name}\\{folder_name}.json")
        j = open_file(f_path, folder_name, folder_name_full)
        print(f"Success")
    except OSError:
        print(f"No Json file detected. Creating...")
        j = convert(f_path, folder_name, folder_name_full)
    return j

def open_file(f_path, folder_name, folder_name_full):
    return json.load(open(f"{f_path[0:-(len(folder_name) + 5)]}\\{folder_name}\\{folder_name}.json", "r"))

def convert(f_path, folder_name, folder_name_full):
    print("Creating frames (this is a one time process)...")
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError:
        raise OSError(f"Error: failed to create folder {folder_name} for file {folder_name_full}")
    cam = cv2.VideoCapture(f_path)

    current_frame = 0

    while True: 

        ret,frame = cam.read()
      
        if ret: 
            # if video is still left continue creating images 
            name = f'./{folder_name}/frame' + str(current_frame) + '.png'
            b = 'Creating...' + name
            print(b)
      
            # writing the extracted images 
            cv2.imwrite(name, frame) 
      
            # increasing counter so that it will 
            # show how many frames are created 
            current_frame += 1
        else: 
            break
    try:
        assert current_frame > 0
    except AssertionError:
        raise ValueError(f"Error: File {folder_name_full} loading failed")

    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()

    # get the frame rate

    video = moviepy.editor.VideoFileClip(f_path)
    video_duration = int(video.duration)
    fps = current_frame / video_duration
    info = {}
    info["FPS"] = fps
    info["MAX_FRAMES"] = current_frame
    info["IMAGES_LOCATION"] = f'{f_path[0:-(len(folder_name) + 5)]}\\{folder_name}\\'
    info["AUDIO_LOCATION"] = get_audio(f_path, info["IMAGES_LOCATION"], folder_name)
    with open(f"{f_path[0:-(len(folder_name) + 5)]}\\{folder_name}\\{folder_name}.json", "w") as file:
        json.dump(info, file)
    return json.load(open(f"{f_path[0:-(len(folder_name) + 5)]}\\{folder_name}\\{folder_name}.json", "r"))


def get_movies(direc):
    print(f"detecting videos in directory {direc}\\...")
    dicts = []
    list_dir = os.listdir(direc)
    accepted = []
    for item in list_dir:
        if item[-4:] in ACCEPTED_FORMATS:
            accepted.append(item)
    print(f"{len(accepted)} videos detected")
    for item in accepted:
        path = f"{direc}\\{item}"
        dicts.append(get_movie(path))
    return dicts