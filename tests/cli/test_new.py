import pytest
from zygoat.cli import cli


@pytest.mark.slow
def test_new(click_runner, tmp_path, fake):
    """Create a new project in a temporary directory."""
    name = fake.domain_word()

    with click_runner.isolated_filesystem(temp_dir=tmp_path):
        result = click_runner.invoke(
            cli,
            ["new", name],
        )

        assert result.exit_code == 0
