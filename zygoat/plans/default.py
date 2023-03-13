from zygoat.plans import frontend, backend, git
from zygoat.utils import inject_resource_file

from loguru import logger as log


_plans = [
    frontend,
    backend,
    git,
]

_injected_files = [
    "docker-compose.yml",
    "Caddyfile",
]


def entrypoint(*args, **kwargs):
    for plan in _plans:
        plan.entrypoint(*args, **kwargs)

    for file_name in _injected_files:
        log.info(f"Injecting {file_name}")
        inject_resource_file(file_name)
