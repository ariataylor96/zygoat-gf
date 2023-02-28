import click

from .new import new


@click.group()
def cli():
    """Base command group to mount subcommands under."""


_sub_commands = [new]

# Register all sub commands to the group
for c in _sub_commands:
    cli.command()(c)
