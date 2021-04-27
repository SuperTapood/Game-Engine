class InvalidBorderButtonError(Exception):
    __module__: str
    rect1_dim: (int, int)
    rect2_dim: (int, int)

    def __init__(self, w1: int, h1: int, w2: int, h2: int):
        ...

    def __str__(self) -> str:
        ...

    pass
