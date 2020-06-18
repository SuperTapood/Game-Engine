# DOCUMENTATION
this documentation will assume you import the engine like this:
import engine as eng




# eng.Screen methods:
# eng.Screen.__init__(x=500, y=500, color=BLACK, caption="") -> Screen object
this will return a Screen object

# eng.Screen.fill(color)
fills the screen with color color and sets the screen color to it

# eng.Screen.event_handler()
this is an automated version of the pygame loop, if you don't need anything to happen with these events

# eng.Screen.terminate()
terminates the pygame screen then the python program (wrote this to be overridable for exit-saving or something)

# eng.Screen.update()
updates the screen -> resets the window, then redraws everything back on

# eng.Screen.quit_handle(event)
private method
checks if an event is of pygame.QUIT type

# eng.Screen.add_text(txt, x, y, size, color=WHITE, font="freesansbold.ttf", center=True)
adds text txt in position (x, y) of font font and size size and color color to the screen. this method needs to be constantly called in the "while true" so it will constatnly drawn

# eng.Screen.blit(obj, rect)
blits object obj to position rect (x, y) on the screen

# eng.Screen.add_button(self, x, y, w, h, color) -> (x, y, w, h)
this will create a button on the screen. this method needs to be constantly called so it will be constantly drawn on the screen.

# eng.Screen.check_click(self, tup) -> bool
this will check if the button tup is being clicked on

# eng.Screen.fit_for_BG(loc)
this puts the background at location loc to the screen and fits the screen to the background

# eng.Screen.load_image(loc) -> pygame.Image
this loads an image at location loc and returns a pygame image

# eng.Screen.resize(x, y)
resizes the screen to size (x, y) and updates the relevant Screen properties

# eng.Screen.load_BG(img)
private method.
load image img as the background of the screen

# eng.Screen.load_BG(img)
loads a background on the screen

# eng.Screen.add_text_button(txt, x, y, size, txtColor, btnColor, font="freesansbold.ttf") -> returns (x, y, w, h)
creates a button with text on it and returns the button tuple

# eng.Screen.update_fields()
updates all of the existing fields

# eng.Screen.add_field(ID, txt, x, y, size, emptyLength=15) -> Input_Field
returns an input field of the specified properties. The ID is required so the field will be unique.

# eng.Screen.field_check()
checks for clicks in all of the created fields

# eng.Screen.send_input_to_fields(letter)
sends the letter letter to the first active field.

# eng.Screen.del_all_fields()
deletes all of the active fields

# eng.Screen.del_field(field)
deletes field field from the screen

# eng.Screen.del_field_by_ID(ID)
deletes field of ID ID from the screen

# eng.Screen.del_multiple_fields(args)
deletes fields args from the screen

# eng.Screen.del_multiple_fields_by_ID(args)
deletes all fields with IDs in args

# eng.Screen.load_images_based_on_prefix(loc, prefix) -> generator object
this returns all of the images with the prefix prefix at location loc as pygame images

# eng.Screen.return_key_name(event) -> str
returns the key name of event event

# eng.Screen.update_sprites()
updates all of the created sprites (non dummy)

# eng.Screen.add_clock(fps)
adds a pygame clock object with frame rate fps

# eng.Screen.update_players()
updates all of the created players

# eng.Screen.add_sprite(sprite)
adds sprite sprite to the screen's array

# eng.Screen.add_player(player)
adds player player to the screen's array

# eng.Screen.send_input_events_to_players(event)
inputs event event into all of the players

# eng.Screen.return_dummy_player(img, x, y, screen) -> Player(dummy=True)
returns a dummy player for the generator class

# eng.Screen.add_generator(generator)
adds generator generator to the screen's array

# eng.Screen.update_generators()
updates all of the generators created