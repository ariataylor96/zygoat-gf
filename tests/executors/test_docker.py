import os
from zygoat.utils import use_dir

exists = os.path.isfile


def test_creation(py_executor):
    container = py_executor.container
    assert container.status == "created"


def test_fs_mount(py_executor, fake, tmp_path):
    with use_dir(tmp_path):
        file_name = fake.file_name()
        assert not exists(file_name)

        py_executor.exec(["touch", file_name])
        assert exists(file_name)
