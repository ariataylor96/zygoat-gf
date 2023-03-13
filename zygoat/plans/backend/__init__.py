from loguru import logger as log
import os

from zygoat.executors import DockerExecutor

from .docker import inject_dockerfiles
from .gunicorn import inject_gunicorn_conf
from .black import inject_black_config, reformat_project


BACKEND = "backend"


def entrypoint(*args, **kwargs):
    log.info("Initializing the backend project")
    os.makedirs(BACKEND)

    # TODO: Take these values from params/config
    python = DockerExecutor("python:latest", pull=True, workdir=BACKEND)
    python.exec_all(
        "pip install --upgrade pip poetry",
        "poetry init -n --name=backend",
        "poetry add Django gunicorn",
        "poetry run django-admin startproject backend .",
    )

    inject_dockerfiles(BACKEND)
    inject_gunicorn_conf(BACKEND)

    # Fix permissions in advance of the GC sweep
    python.clean_perms()
    inject_black_config(BACKEND)
    reformat_project(python)
