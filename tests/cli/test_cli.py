from zygoat.cli import cli


def test_cli(click_runner):
    """
    Ensure that the CLI can be invoked
    """
    click_runner.invoke(cli)
