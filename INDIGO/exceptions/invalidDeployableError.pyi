class InvalidDeployableError(Exception):
    __module__: str
    class_name: str

    def __init__(self, class_name: str):
        ...

    def __str__(self) -> str:
        ...
