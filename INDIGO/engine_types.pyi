import pygame

from INDIGO.objects.sprites.player import Player
from INDIGO.objects.sprites.placeholder import Placeholder
from INDIGO.objects.sprites.group import Group
from INDIGO.counters.counter import Counter
from INDIGO.objects.buttons.button import Button
from INDIGO.objects.buttons.button_with_borders import ButtonWithBorders
from INDIGO.objects.buttons.button_meta import Button_Meta
from INDIGO.screen import Screen
from INDIGO.objects.engineobject import EngineObject
from INDIGO.objects.buttons.button import Button
from INDIGO.objects.shapes.rect import Rect
from INDIGO.objects.shapes.circle import Circle
from INDIGO.objects.buttons.button_meta import ButtonMeta
from typing import *

func = Callable[[Any], Any]
Sprite = Union[Player, Placeholder]
num = Union[int, float]
color_tup = (int, int)
Optional = Optional
EngineObject = EngineObject
Button = Button
Rect = Rect
Circle = Circle
ButtonMeta = ButtonMeta
Image = Union[str, pygame.image]
Any = Any
