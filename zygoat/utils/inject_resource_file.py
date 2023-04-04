from zygoat.types import PathLike

from .inject_file_contents import inject_file_contents
from .resource_file_contents import resource_file_contents


def inject_resource_file(name: PathLike) -> None:
    """
    Places a file from the resource directory at its corresponding path in the project.

    :param name: Path to the file to copy
    """

    inject_file_contents(name, resource_file_contents(name))
