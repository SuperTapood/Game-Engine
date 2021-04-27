class GroupAddError(Exception):
    __module__: str
    type: str
    inst: str

    def __init__(self, inst, class_type):
        ...

    def __str__(self) -> str:
        ...
