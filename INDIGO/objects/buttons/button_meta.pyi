from INDIGO.engine_types import *


class ButtonMeta(EngineObject):
    last_click: num

    def check_click(self):
        ...

    def blit(self):
        ...
