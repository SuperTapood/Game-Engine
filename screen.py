import pygame
from colors import *
from sprite import Sprite
from inputField import InputField
import os


class Screen:
	def __init__(self, x, y, color, caption=""):
		"""
		int x - height of the window
		int y - width of the window
		int tuple color - the color of the window (R,G,B)
		str caption - the caption of the window
		"""
		pygame.init()
		self.__sprites = []
		self.__fields = []
		self.display = pygame.display.set_mode((x, y))
		self.MIDDLEX = x // 2
		self.MIDDLEY = y // 2
		self.color = None
		self.fill(color)
		pygame.display.set_caption(caption)
		return

	def fill(self, color):
		"""
		fills the window with a color
		int tuple color - the color to fill
		"""
		self.color = color
		self.display.fill(color)
		return

	def eventHandler(self):
		## override this function in order to add events ##
		for event in pygame.event.get():
			self.__quitHandle(event)
		self.update()
		return

	def terminate(self):
		"""
		terminates the program
		override for exit saves or something
		"""
		pygame.quit()
		quit()
		return

	def update(self):
		# update the display
		pygame.display.update()
		self.fill(self.color)
		self.updateSprites()
		self.updateFields()
		return

	def __quitHandle(self, event):
		"""
		private method
		event event - the event (from pygame.event.get())
		"""
		if event.type == pygame.QUIT:
			self.terminate()
		return

	def addText(self, txt, x, y, size, color=WHITE, font="freesansbold.ttf", center=True):
		"""
		str txt - the text to be displayed
		int x - x position of the text
		int y - y position of the text
		int size - the size of the text
		int tuple color - the color of the text
		str font - the name of the font to be used (unless you know what you are doing, don't change that)
		bool center - whether x and y should be for the center or the top left

		returns int tup
		"""
		font = pygame.font.Font(font, size)
		text = font.render(txt, True, color)
		rect = text.get_rect()
		if center:
			rect.center = (x, y)
		else:
			rect.topleft = (x, y)
		self.__blit(text, rect)
		return rect

	def __blit(self, obj, rect):
		"""
		private method
		blits an object to the display
		any obj - the object to be blitted
		int tuple - pos (x, y) of the object
		"""
		self.display.blit(obj, rect)
		return

	def addButton(self, x, y, w, h, color):
		"""
		int x - the x position of the button
		int y - the y position of the button
		int w - the width of the button
		int h - the height of the button
		int tuple color - the color of the button (R, G, B)

		returns int tuple
		"""
		tup = (x, y, w, h)
		pygame.draw.rect(self.display, color, tup)
		return tup

	def checkClick(self, tup):
		"""
		checks if the button is "clicked"
		int tuple tup - the x loc, y loc , width and height respectivly

		returns bool
		"""
		x = tup[0]
		y = tup[1]
		w = tup[2]
		h = tup[3]
		# get the position of the mouse
		mouse = pygame.mouse.get_pos()
		# get what buttons the mouse are pressed
		click = pygame.mouse.get_pressed()
		# return bool
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1

	def fitForBG(self, loc):
		"""
		r str loc - the location of the background picture
		"""
		img = self.__loadImage(loc)
		rect = img.get_rect()
		x = rect.w
		y = rect.h
		self.resize(x, y)
		self.__loadBG(img)
		return

	def __loadImage(self, loc):
		"""
		r str loc - the location of the image

		returns surface
		"""
		return pygame.image.load(loc)

	def resize(self, x, y):
		"""
		int x - the new height of the display
		int y - the new width of the display
		"""
		self.MIDDLEX = x // 2
		self.MIDDLEY = y // 2
		self.display = pygame.display.set_mode((x, y))
		return

	def __loadBG(self, img):
		"""
		surface img - the image to load as background
		"""
		self.__blit(img, (0, 0))
		return

	def loadBG(self, loc):
		"""
		r str loc - the location of the background picture
		"""
		img = self.__loadImage(loc)
		self.__loadBG(img)
		return

	def addTextButton(self, txt, x, y, size, txtColor, btnColor, font="freesansbold.ttf"):
		"""
		adds a button with text on it
		str txt - the text to be written
		int x - the x loc of the button and text
		int y - the y loc of the latters
		int size - the size of the text
		int tuple txtColor - the color of the text (R,G,B)
		int tuple btnColor - the color of the button (R,G,B)
		str font - the font of the text

		returns int tuple
		"""
		# get the text's rect
		textRect = self.addText(txt, x, y, size, txtColor, center=False)
		# create it
		rect = self.addButton(textRect.x, textRect.y, textRect.w, textRect.h, btnColor)
		# draw the text
		textRect = self.addText(txt, x, y, size, txtColor, center=False)
		return rect

	def addSprite(self, spriteType, sprite, x, y):
		"""
		str spriteType - the type of the sprite
		any sprite - the "mask"
		int x, y - the initial location of the sprite
		"""
		if spriteType == "img":
			sprite = self.__loadImage(sprite)
		s = Sprite(self.display, sprite, x, y)
		self.__sprites.append(s)
		return s

	def removeSprite(self, sprite):
		"""
		Sprite sprite - the sprite to be deleted
		"""
		self.__sprites.remove(sprite)
		return

	def removeAllSprites(self):
		self.__sprites = []
		return

	def removeMultipleSprites(self, *args):
		"""
		Sprite args - the sprites to be deleted
		"""
		for sprite in args:
			if sprite in self.__sprites:
				self.removeSprite(sprite)
			else:
				exit(f"EngineError: sprite {sprite} not found")
		return

	def updateSprites(self):
		for sprite in self.__sprites:
			sprite.update()
		return

	def updateFields(self):
		for field in self.__fields:
			field.update(self.addTextButton)
		return

	def moveSprite (factor, x, y):
		"""
		int factor - by how much to move the sprite
		bool x, y - whether to move this axis or not
		"""
		self.__sprites[index].move(factor, x, y)
		return

	def addField(self, ID, txt, x, y, size, emptyLength=15):
		"""
		str ID - the ID of the field (v. important!!)
		str txt - the initital text to be displayed
		int x, y - the position of the field
		int size - the size of the text
		int emptyLength - the minimum length (in spaces) of text in the field (not yet implemented)
		"""
		for field in self.__fields:
			if field.ID == ID:
				return field
		if txt is None:
			txt = ""
			for i in range(emptyLength):
				txt += " "
		self.__fields.append(InputField(ID, txt, x, y, size))
		return self.__fields[0]

	def fieldCheck(self):
		for field in self.__fields:
			field.checkClick()
		return

	def __sendInputToFields(self, letter):
		"""
		str letter - the letter to send to the active field
		"""
		for f in self.__fields:
			if f.active:
				f.sendLetters(letter)
				return
		return

	def delAllFields(self):
		self.__fields = []
		return

	def delField(self, field):
		"""
		InputField field - the field to be deleted
		"""
		try:
			self.__fields.remove(field)
		except:
			exit(f"EngineError: Input Field {field} not found")
		return

	def delFieldByID(self, ID):
		"""
		str ID - the ID of the field to be deleted
		"""
		for field in self.__fields:
			if field.ID == ID:
				self.delField(field)
				return
		exit(f"EngineError: No field ID'd as {ID}")
		return

	def delMultipleFields(self, *args):
		"""
		InputField args - the fields to be deleted
		"""
		for field in args:
			try:
				self.__fields.remove(field)
			except:
				exit(f"EngineError: field {field} not found")
		return

	def delMultipleFieldsByID(self, *args):
		"""
		str args - a list of all the IDs to delete
		"""
		targets = []
		for ID in args:
			for field in self.__fields:
				if field.ID == ID:
					targets.append(field)
					break
			exit(f"EngineError: No field ID {ID}")
		self.delMultipleFields(t for t in targets)
		return

	def loadImagesBaseOnPrefix(self, loc, prefix):
		"""
		str loc - the location of the images
		str prefix - the prefix of the images

		yields all the images with the prefix (post load)
		"""
		lis = os.listdir(loc)
		leng = len(prefix)
		for item in lis:
			if item[:leng] == prefix:
				yield self.__loadImage(f"{loc}\\{item}")
		return