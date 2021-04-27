class NonKillableObjectError(Exception):
    __module__: str
    obj: object

    def __init__(self, obj: object):
        ...

    def __str__(self) -> str:
        ...
