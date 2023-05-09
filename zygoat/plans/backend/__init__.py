from loguru import logger as log
import os

from zygoat.executors import DockerExecutor

from .docker import inject_dockerfiles
from .gunicorn import inject_gunicorn_conf
from .black import inject_black_config, reformat_project
from .settings import inject_env_configuration

import shlex


BACKEND = "backend"

PROD_DEPS = [
    "Django",
    "gunicorn",
    "django-environ",
    "zygoat-django",
    "djangorestframework",
    "djangorestframework-camel-case",
]

DEV_DEPS = [
    "flake8",
    "black",
    "flake8-black",
    "pytest",
    "bandit",
    "flake8-mock",
    "flake8-commas",
    "flake8-quotes",
    "flake8-debugger",
    "flake8-builtins",
    "flake8-deprecated",
    "flake8-comprehensions",
    "pytest-django",
    "pytest-cov",
]


def entrypoint(*args, attach=False, **kwargs) -> None:
    log.info("Initializing the backend project")
    os.makedirs(BACKEND)

    # TODO: Take these values from params/config
    python = DockerExecutor("python:latest", pull=True, workdir=BACKEND, attach=attach)
    python.exec_all(
        "pip install --upgrade pip poetry",
        "poetry init -n --name=backend",
        "poetry add {}".format(shlex.join(PROD_DEPS)),
        "poetry add --group dev {}".format(shlex.join(DEV_DEPS)),
        "poetry run django-admin startproject backend .",
    )

    inject_dockerfiles(BACKEND)
    inject_gunicorn_conf(BACKEND)

    # Fix permissions in advance of the GC sweep
    python.clean_perms()
    inject_black_config(BACKEND)
    reformat_project(python)
    inject_env_configuration(BACKEND)
