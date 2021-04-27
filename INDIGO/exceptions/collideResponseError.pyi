class CollideResponseError(Exception):
    __module__: str
    func_name: str

    def __init__(self, func_name: str):
        ...

    def __str__(self) -> str:
        ...