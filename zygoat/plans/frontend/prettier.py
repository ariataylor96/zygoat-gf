import os
from zygoat.executors import DockerExecutor
from loguru import logger as log
from zygoat.utils import inject_resource_file, use_dir
from .utils import add_package_script

from zygoat.types import PathLike


def inject_prettier(node: DockerExecutor, workdir: PathLike) -> None:
    log.info("Adding prettier dependencies")
    node.exec("pnpm add -D prettier @trivago/prettier-plugin-sort-imports")

    log.info("Injecting prettier config")
    inject_resource_file(os.path.join(workdir, ".prettierrc.js"))

    log.info("Adding prettier package script")
    with use_dir(workdir):
        add_package_script("pretty", 'prettier --write "pages/**/*.js"')
