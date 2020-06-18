# DOCUMENTATION
this documentation will assume you import the engine like this:
import engine as eng


# eng.Screen(x=500, y=500, color=BLACK, caption="") -> Screen object
this will return a Screen object

# eng.Screen.fill(color)
fills the screen with color color and sets the screen color to it

# eng.Screen.event_handler()
this is an automated version of the pygame loop, if you don't need anything to happen with these events

# eng.Screen.terminate()
terminates the pygame screen then the python program (wrote this to be overridable for exit-saving or something)

# eng.Screen.update()
updates the screen -> resets the window, then redraws everything back on

# eng.Screen.__quit_handle(event)