from zygoat.plans import frontend, backend
from zygoat.utils import inject_file_contents, resource_file_contents
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
        inject_file_contents(file_name, resource_file_contents(file_name))

    git = DockerExecutor("bitnami/git:latest", pull=True)
    git.exec("git init")
