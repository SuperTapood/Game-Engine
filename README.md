# Python Game Engine

__note: game engine requires the while True loop to work there is no way around it.__

Usage of this pygame game engine requires quite a bit of python knowledge

The is currently no ready version of the engine, the latest one is in the folder with the latest engine test

the old game engine will be deleted once it is fully depcrecated.



# TODO

### ADD SOME BLOODY DOCUMENTATION YOU MORON

#### General
border input field\
repuprpose method? set as? (shapes to buttons and players and such)\
allow shapes to be players\
ellipse\
ellipse button\
redo the code for animation\
add change text to a label\
optimize the text button\
group fill function\
add a sanity check\
exceptions master class (with kwargs and such)\

#### Music Player
player just refuses to work, halting progress on both players

#### Video Player
Use the music player, cv2 and pygame.surfarray.make_surface to turn a read image to a numpy array and then to a presentable image at a certain frame rate (maybe even figure it out on its own)
EDIT: there doesn't seem to be a way around using files to play audio, need to extract using ffmpeg and play from that