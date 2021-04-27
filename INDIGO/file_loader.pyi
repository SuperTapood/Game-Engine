from INDIGO.engine_types import *

sound_extensions: [str]
video_extensions: [str]
image_extension: [str]


def load_image(loc: str) -> Any:
    ...


def load_file(path: str, file: str) -> Any:
    ...


def load_all(path) -> [Any]:
    ...


def load_type(path: str, ext: str) -> [Any]:
    ...


def load_prefix(path: str, prefix: str) -> [Any]:
    ...


def load_type_prefix(path, prefix, ext) -> [Any]:
    ...
