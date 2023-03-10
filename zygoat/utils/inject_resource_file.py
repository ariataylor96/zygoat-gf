from typing import Union
import os

from .inject_file_contents import inject_file_contents
from .resource_file_contents import resource_file_contents


def inject_resource_file(name: Union[str, os.PathLike]) -> None:
    inject_file_contents(name, resource_file_contents(name))
