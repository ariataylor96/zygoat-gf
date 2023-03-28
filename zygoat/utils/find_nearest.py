import os
from typing import Optional
from pathlib import Path
from .use_dir import use_dir


def find_nearest(file_name: str) -> Optional[Path]:
    """
    Locates the nearest instance of a file, in the current or parent directory.

    :param file_name: The file_name to search for
    :return: pathlib.Path on a match, or None
    """

    match = None
    cwd = os.path.abspath(os.getcwd())

    while cwd != "/":
        with use_dir(cwd):
            files = os.listdir()
            if file_name in files:
                match = Path(os.path.join(cwd), file_name)
                break

            cwd = os.path.abspath(os.path.join(cwd, ".."))

    return match
