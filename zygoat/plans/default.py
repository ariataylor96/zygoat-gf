from zygoat.plans import frontend, backend
from zygoat.utils import inject_resource_file
from zygoat.executors import DockerExecutor

from loguru import logger as log


_plans = [
    frontend,
    backend,
]

_injected_files = [
    "docker-compose.yml",
    "Caddyfile",
]


def entrypoint(*args, **kwargs):
    for plan in _plans:
        plan.entrypoint(*args, **kwargs)

    for file_name in _injected_files:
        log.debug(f"Injecting {file_name}")
        inject_resource_file(file_name)

    git = DockerExecutor("bitnami/git:latest", pull=True)
    git.exec("git init")
