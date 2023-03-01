import os
from zygoat.utils import use_dir


def test_use_dir(tmp_path, fake):
    new_path = os.path.join(tmp_path, fake.file_name(extension=""))
    os.makedirs(new_path)

    with use_dir(new_path):
        assert os.getcwd() == new_path
