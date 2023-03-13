import os
from zygoat.plans.git import inject_gitignores
from zygoat.utils import use_dir


def test_inject_gitignores(tmp_path):
    with use_dir(tmp_path):
        assert not os.path.exists(".gitignore")
        inject_gitignores()
        assert os.path.exists(".gitignore")
