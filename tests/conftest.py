import pytest
from faker import Faker

from click.testing import CliRunner


@pytest.fixture
def click_runner():
    return CliRunner()


@pytest.fixture
def fake():
    return Faker()
