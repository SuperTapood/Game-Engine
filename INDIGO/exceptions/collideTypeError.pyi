class CollideTypeError(Exception):
    __module__: str
    non_group_type: str

    def __init__(self, non_group_type: str):
        ...

    def __str__(self) -> str:
        ...
