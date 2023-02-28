import click

from .new import new


@click.group()
def cli():
    """
    Base command group under which all others are mounted
    """


_sub_commands = [new]

# Register all sub commands to the group
for c in _sub_commands:
    cli.command()(c)
