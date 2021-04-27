class PlaceholderBlitError(Exception):
    __module__: str
    x: int
    y: int

    def __init__(self, x: int, y: int):
        ...

    def __str__(self) -> str:
        ...
