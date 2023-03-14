from loguru import logger as log
import os
import shutil

from zygoat.executors import DockerExecutor
from zygoat.utils import use_dir, inject_resource_file
from .docker import inject_dockerfiles

FRONTEND = "frontend"
_boilerplate_paths = ["public", "styles", "pages/api", "pages/index.js"]


def entrypoint(*args, name=None, **kwargs):
    log.info("Initializing the frontend project")
    os.makedirs(FRONTEND)

    # TODO: Take these values from params/config
    node = DockerExecutor(
        "node:latest",
        workdir=".",
        pull=True,
    )
    node.exec_all(
        "npm install -g npm@latest",
        "npm install -g pnpm",
        """pnpm create next-app --js --use-pnpm --eslint --no-experimental-app --no-src-dir --import-alias "@/*" frontend""",
        "rm -rf .pnpm-store",
    )

    # Fix permissions in advance of the GC sweep
    node.clean_perms()

    with use_dir(FRONTEND):
        log.info("Deleting NextJS boilerplate")
        for path in _boilerplate_paths:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

        # Restore the public directory, since that's actually useful
        os.makedirs("public")

    inject_dockerfiles(FRONTEND)
    inject_resource_file(os.path.join(FRONTEND, ".eslintrc.js"))
