from INDIGO.engine_types import *


class CircleButton(ButtonMeta):
    circle: Circle
    x: num
    y: num
    resp: func
    delay_time: num
    def __init__(self, scr: Screen, color: color_tup, x: num, y: num, radius: num, resp: func=lambda: None,
                 width: num=0, delay_time: num=0.3):
        ...

    def blit_func(self):
        ...
