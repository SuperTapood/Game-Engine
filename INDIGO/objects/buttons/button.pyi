from INDIGO.engine_types import *


class Button(Button_Meta):
    scr: Screen
    color: color_tup
    resp: Optional[func]
    rect: (num, num, num, num)
    border_width: num
    click_delay: num

    def __init__(self, scr: Screen, x: num, y: num, w: num, h: num, color: color_tup, resp: Optional[func]=lambda: None,
                 border_width: num=0, click_delay: num=0.3):
        ...

    def blit_func(self):
        ...

    pass
