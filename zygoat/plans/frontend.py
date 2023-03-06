from loguru import logger as log
import os

from zygoat.executors import DockerExecutor

FRONTEND = "frontend"
executor = None


def entrypoint(*args, name=None, **kwargs):
    log.info("Initializing the frontend project")
    os.makedirs(FRONTEND)

    # TODO: Take these values from params/config
    # TODO: Remove attach parameter when finished debugging
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
