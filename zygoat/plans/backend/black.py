import os
import toml

from zygoat.utils import resource_file_contents
from zygoat.executors import DockerExecutor


def inject_black_config(workdir: os.PathLike) -> None:
    file_name = os.path.join(workdir, "pyproject.toml")

    project_config = toml.load(file_name)
    black_config = toml.loads(resource_file_contents(file_name).decode())

    project_config["tool"].update(black_config["tool"])

    with open(file_name, "w") as f:
        toml.dump(project_config, f)


def reformat_project(python: DockerExecutor) -> None:
    python.exec_all(
        ["poetry", "add", "--group", "dev", "black"],
        ["poetry", "run", "black", "."],
    )
