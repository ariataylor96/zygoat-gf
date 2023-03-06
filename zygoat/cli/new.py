import os
import click
from importlib import import_module
from typing import Callable

from loguru import logger as log

from zygoat.utils import use_dir


@click.argument("name")
@click.option(
    "--plan",
    default="zygoat.plans:default",
    help="Import path to the default plan module to execute - e.g. zygoat.plans:default",
)
def new(name, plan):
    log.info(f"Creating {name}")
    os.makedirs(name)

    plan = _get_plan(plan)

    with use_dir(name):
        plan(name=name)

    # Get a vertical break first
    for _ in range(2):
        print()

    log.info(f"Your project {name} is ready! Happy hacking!")


def _get_plan(import_path: str) -> Callable:
    module, attr = import_path.split(":")
    imported = getattr(import_module(module), attr)

    if callable(imported):
        return imported

    log.debug(f"{import_path} is not callable, checking for .entrypoint()")
    imported = getattr(imported, "entrypoint")

    if imported is None or not callable(imported):
        raise ImportError(
            f"Neither {import_path} nor {import_path}.entrypoint are callable functions, exiting"
        )

    return imported
