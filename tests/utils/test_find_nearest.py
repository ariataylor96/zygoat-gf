import os
from pathlib import Path
from zygoat.utils import find_nearest, use_dir


def test_find_nearest(tmp_path, fake):
    bad_path = fake.file_path()
    good_path = Path(os.path.join(tmp_path, fake.file_name()))

    assert find_nearest(bad_path) is None

    good_path.mkdir()
    good_path.touch()

    assert good_path.parent.exists()
    assert good_path.exists()

    with use_dir(good_path.parent):
        result = find_nearest(good_path.name)
        assert good_path.absolute() == result.absolute()
