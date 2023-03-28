import json
import os
from typing import Union
from loguru import logger as log
from zygoat.utils import find_nearest


def add_package_script(
    name: str,
    cmd: str,
    file_name: Union[str, os.PathLike] = "package.json",
) -> None:
    """
    Adds a package script to the nearest package.json file.

    :param name: Name of the script to add (key)
    :param cmd: Command associated with the script (value)
    :param file_name: Name of file to look for
    """

    package_path = find_nearest(file_name)
    if package_path is None:
        e = FileNotFoundError(f"Unable to find {file_name} in {os.getcwd()} or ancestors")
        log.critical(e)
        raise e

    with open(package_path) as f:
        package_data = json.load(f)

    package_data["scripts"][name] = cmd

    with open(package_path, "w") as f:
        json.dump(package_data, f, indent=2)
