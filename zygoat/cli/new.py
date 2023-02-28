import click

from loguru import logger as log


@click.argument("project_name")
def new(project_name):
    log.info(f"Creating {project_name}")
    print(project_name)
