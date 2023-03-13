from loguru import logger as log

from zygoat.executors import DockerExecutor

from .ignore import inject_gitignores


def entrypoint(*args, **kwargs):
    log.info("Initializing git repository")

    git = DockerExecutor("bitnami/git:latest", pull=True)
    git.exec("git init")
    git.clean_perms()
    inject_gitignores()
