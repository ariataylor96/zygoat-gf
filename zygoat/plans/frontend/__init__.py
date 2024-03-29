from loguru import logger as log
import os
import shutil

from zygoat.executors import DockerExecutor
from zygoat.utils import use_dir
from .docker import inject_dockerfiles
from .prettier import inject_prettier
from .eslint import inject_eslint

FRONTEND = "frontend"
_boilerplate_paths = ["public", "styles", "pages/api", "pages/index.js", "pages/_app.js"]
_pnpm_setup = ["npm install -g npm@latest", "npm install -g pnpm"]


def entrypoint(*args, attach=False, **kwargs):
    log.info("Initializing the frontend project")
    os.makedirs(FRONTEND)

    # TODO: Take these values from params/config
    node = DockerExecutor(
        "node:latest",
        workdir=".",
        pull=True,
        attach=attach,
    )
    node.exec_all(
        *_pnpm_setup,
        """pnpm create next-app --no-tailwind --js --use-pnpm --eslint --no-app --no-src-dir --import-alias "@/*" frontend""",
        "rm -rf .pnpm-store",
    )

    # Explicitly fix permissions in advance of the GC sweep
    node.clean_perms()

    # Now that the project is generated, get a proper node executor spun up
    node = DockerExecutor(
        "node:latest",
        workdir="frontend",
        pull=True,
    )

    node.exec_all(*_pnpm_setup)

    with use_dir(FRONTEND):
        log.info("Deleting NextJS boilerplate")
        for path in _boilerplate_paths:
            if not os.path.exists(path):
                log.critical(
                    f"Couldn't locate {path}! create-next-app likely failed, try rerunning with --attach"
                )
                exit(1)

            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

        # Restore the public directory, since that's actually useful
        os.makedirs("public")

    inject_dockerfiles(FRONTEND)
    inject_prettier(node, FRONTEND)
    inject_eslint(node, FRONTEND)
