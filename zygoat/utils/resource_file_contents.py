import os
import pkgutil


def resource_file_contents(file_name: str):
    return pkgutil.get_data("zygoat", os.path.join("resources", file_name))
