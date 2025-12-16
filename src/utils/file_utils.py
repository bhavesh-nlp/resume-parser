import os

def file_exists(path: str) -> bool:
    return os.path.exists(path)


def get_file_extension(path: str) -> str:
    return os.path.splitext(path)[-1].lower()

