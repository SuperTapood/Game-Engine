class OverrideError(Exception):
    __module__: str
    method: str
    class_name: str

    def __init__(self, method: str, class_name: str):
        ...

    def __str__(self) -> str:
        ...

    pass
