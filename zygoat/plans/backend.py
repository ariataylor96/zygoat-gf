from loguru import logger as log
import os

from zygoat.executors import DockerExecutor

BACKEND = "backend"
executor = None


def entrypoint():
    log.info("Initializing the backend project")
    os.makedirs(BACKEND)

    # TODO: Take these values from params/config
    python = DockerExecutor("python:latest", pull=True, workdir=BACKEND)
    python.exec_all(
        "pip install --upgrade pip poetry",
        "poetry init -n --name=backend",
        "poetry add Django",
        "poetry run django-admin startproject backend .",
    )

    log.info("Changing project ownership to match current user")
    python.clean_perms()
