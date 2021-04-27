class UnsupportedExtensionError(Exception):
    __module__: str
    file: str
    loc: str
    type: str

    def __init__(self, file: str, loc: str, typ: str):
        ...

    def __str__(self) -> str:
        ...
