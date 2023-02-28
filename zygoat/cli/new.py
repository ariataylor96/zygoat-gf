import os
import click

from loguru import logger as log

from zygoat.plans import backend
from zygoat.utils import use_dir

modules = [
    backend,
]


@click.argument("name")
def new(name):
    log.info(f"Creating {name}")
    os.makedirs(name)

    # TODO: load these at runtime with importlib
    with use_dir(name):
        for module in modules:
            module.entrypoint()
