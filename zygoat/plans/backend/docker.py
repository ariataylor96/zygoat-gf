import os
from zygoat.utils import inject_resource_file

files = ["Dockerfile.local", "Dockerfile"]


def inject_dockerfiles(workdir):
    for base_name in files:
        file_name = os.path.join(workdir, base_name)
        inject_resource_file(file_name)
