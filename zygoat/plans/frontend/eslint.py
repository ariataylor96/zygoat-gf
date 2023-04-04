import os
from zygoat.utils import inject_resource_file
from zygoat.executors import DockerExecutor
from zygoat.types import PathLike

files = ["Dockerfile.local", "Dockerfile"]


def inject_eslint(node: DockerExecutor, workdir: PathLike):
    node.exec("pnpm add -D eslint-config-airbnb")
    inject_resource_file(os.path.join(workdir, ".eslintrc.js"))
