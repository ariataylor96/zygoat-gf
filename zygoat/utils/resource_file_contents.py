import os
import pkgutil
from typing import Optional


def resource_file_contents(file_name: os.PathLike) -> Optional[bytes]:
    return pkgutil.get_data("zygoat", os.path.join("resources", file_name))
