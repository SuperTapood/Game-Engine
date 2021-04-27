from INDIGO.engine_types import Image as i
from INDIGO.engine_types import *

class Image:
    image: i
    def __init__(self, path: str):
        ...

    def load_image(self, path: str) -> i:
        ...

    def get_img(self) -> i:
        ...

    def get_dims(self) -> str:
        ...

    def rescale(self, new_scale: num):
        ...

    def resize(self, x: num, y: num):
        ...

    def match_size(self, image: i):
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def rotate(self, ang: num):
        ...

    def get_rect(self) -> (num, num, num, num):
        ...
