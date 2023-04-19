import os

from redbaron import RedBaron
from zygoat.types import PathLike
from zygoat.utils import resource_file_contents, inject_file_contents

_SETTINGS_PATH = os.path.join("backend", "backend", "settings.py")


def inject_env_configuration(workdir: PathLike) -> None:
    settings_data = None

    with open(_SETTINGS_PATH) as f:
        settings_data = RedBaron(f.read())

    to_inject = resource_file_contents(_SETTINGS_PATH).decode()

    import_node = settings_data.find("from_import")
    import_node.insert_before(to_inject)

    inject_file_contents(
        _SETTINGS_PATH,
        contents=settings_data.dumps().encode(),
        overwrite=True,
    )
