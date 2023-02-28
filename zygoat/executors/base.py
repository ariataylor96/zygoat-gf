import os
from pathlib import Path

import docker
from docker.models.containers import Container

from loguru import logger as log

_client = docker.from_env()
_client.containers


class Executor:
    """Maintains a docker container for command execution."""

    client: docker.DockerClient
    container: Container = None

    # Stored parameters
    image: str
    workdir: str

    def __init__(
        self,
        image: str,
        workdir: str = os.getcwd(),
        client=_client,
        pull: bool = False,
        auto_start: bool = True,
    ):
        """
        Spawn an executor.

        :param image: Image tag or URI to launch
        :param workdir: Host directory to mount into the container
        :param client: The docker connection to use, defaults to `docker.from_env()`
        :param force_pull: Pull the image first before launching
        :param auto_start: Start the container automatically"
        """
        self.client = client

        self.image = image
        self.workdir = workdir

        if pull:
            self.pull_image()

        if auto_start:
            self.start()

    def pull_image(self, **kwargs):
        """Manually trigger an image pull."""

        return self.client.images.pull(self.image, **kwargs)

    def start(self, cmd: str = "sleep 30d", *args, **kwargs):
        """Starts the service."""

        if self.container is not None:
            log.warning("Attempted to start an already-running container, which is a no-op")
            return

        abs_path = str(Path(self.workdir).absolute())
        internal_wd = "/zygoat"

        self.container = self.client.containers.run(
            self.image,
            cmd,
            *args,
            detach=True,
            volumes=[f"{abs_path}/:{internal_wd}"],
            working_dir=f"{internal_wd}",
            **kwargs,
        )

        return self.container

    def exec(self, *args, **kwargs):
        """Runs a command inside the container."""

        self.container.exec_run(*args, **kwargs)

    def __del__(self):
        """Destructor to ensure that the container is properly pruned when we're done with it."""
        self.container.stop(timeout=0)
        self.container.wait()
        self.container.remove()

    @property
    def running(self):
        return self.container is not None and self.container.status == "running"
