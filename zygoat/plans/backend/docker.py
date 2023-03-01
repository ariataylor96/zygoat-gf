import os
from zygoat.utils import inject_file_contents, resource_file_contents

files = ["Dockerfile.local", "Dockerfile"]


def inject_dockerfiles(workdir):
    for base_name in files:
        file_name = os.path.join(workdir, base_name)
        inject_file_contents(file_name, resource_file_contents(file_name))
