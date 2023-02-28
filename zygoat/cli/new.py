import click


@click.argument("project_name")
def new(project_name):
    print(project_name)
