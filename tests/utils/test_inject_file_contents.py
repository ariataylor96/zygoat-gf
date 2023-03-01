import os
from zygoat.utils import inject_file_contents


def test_inject_file_contents(tmp_path, fake):
    data = fake.paragraph()
    file_name = os.path.join(tmp_path, fake.file_name())

    inject_file_contents(file_name, data)

    with open(file_name, "r") as f:
        assert f.read() == data
