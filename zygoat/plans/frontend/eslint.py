import os
from zygoat.utils import inject_resource_file

files = ["Dockerfile.local", "Dockerfile"]


def inject_eslint(workdir):
    inject_resource_file(os.path.join(workdir, ".eslintrc.js"))
