import pygame.event

from INDIGO.engine_types import *


class Screen:
    X: num
    Y: num
    MIDDLEX: num
    MIDDLEY: num
    bg_color: color_tup
    display: Any

    def __init__(self, x: num, y: num, bg_color: color_tup, caption: Optional[str]="pygame window"):
        ...

    def update(self):
        ...

    def quit_handler(self, event: pygame.event.Event):
        ...

    def quit(self):
        ...

    def blit(self, obj: Any, x: num, y: num):
        ...

    def fill(self, color: color_tup):
        ...

    def set_bg_img(self, bg_img: Image):
        ...

    def resize_for_bg(self, bg_img: Image):
        ...

    def resize(self, x: num, y):
        ...

    def toggle_fullscreen(self):
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...
