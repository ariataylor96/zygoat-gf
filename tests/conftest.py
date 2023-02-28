import pytest
from faker import Faker

from zygoat.executors import Executor

from click.testing import CliRunner


@pytest.fixture
def click_runner():
    return CliRunner()


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def py_executor(tmp_path):
    return Executor("python", pull=True, workdir=tmp_path)
