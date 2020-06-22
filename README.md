# Python Game Engine

__note: game engine requires the while True loop to work there is no way around it.__

documentation template - """type param - purpose"""

Usage of this pygame game engine requires quite a bit of python knowledge

# change log:

# version 0.6
- added a sprite generator
- added dummy players (for regeneration)
- added player class (now is a template)
- added the SCENE API
- added text and buttons to the API
- fixed problem where text won't update when given a variable in the API
- added str attribute to the scene class to print all of the contained layers
- moved the engine to a package (now import it using Game_Engine.[MODULE])
- added distribute function to the API to easily dismantle the params given in the execution
- added load function to load a scene onto the pygame screen


# version 0.5
- added clock function
- re-added sprites (now is a template)
- added custom exceptions
- redoing the second engine test
- added ground and background to engine test 2
- added bird movement for engine test 2
- replaced all functions' names to snake_case from CamelCase


# version 0.4
- added player
- added player movements
- added player animations
- added engine test 2

# version 0.3
- added input fields - WORKING (but there is a bug regarding reaction time)
- engine test 1 successful
- added many ways to delete an input field
- added a way to load images based on prefix (using yield)
- added a bit of documentation

# version 0.2
- added overriding decorator
- added sprite (for moving images)
- added blit for the sprite
- added sprite movement
- added sprite deletion
- added multiple sprite deletion and even all of them
- added delay for the sprite movement (without harming FPS)

# version 0.1
- added a fill function
- added an event handler (overridable)
- added terminate (cooler than quit) and enabling exit-saves (overridable)
- added update screen
- added text function
- added button function
- added check for click function
- added an image load function
- added a background set
- added blit function
- added a resize function
- added middle constants
- added button and text together (in a seperate function)
- added fit function for background
- documented changes