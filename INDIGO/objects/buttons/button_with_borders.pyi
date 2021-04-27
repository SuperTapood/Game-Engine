from INDIGO.engine_types import *


class ButtonWithBorders(EngineObject):
    rect: Rect
    button: Button
    def __init__(self, scr: Screen, x: num, y: num, w: num, h: num, color1: color_tup, color2: color_tup,
                 size_factor: num=1, resp: func=lambda: None, delay_time: num=0.3):
        ...

    def blit(self):
        ...

    pass
