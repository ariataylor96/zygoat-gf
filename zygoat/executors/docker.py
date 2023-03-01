import os
from pathlib import Path

import docker
from docker.models.containers import Container

from loguru import logger as log

_client = docker.from_env()
_client.containers


class DockerExecutor:
    """Maintains a docker container for command execution."""

    client: docker.DockerClient
    container: Container = None

    # Stored parameters
    image: str
    workdir: str
    attach: bool = False
    clean_perms_on_exit: bool

    def __init__(
        self,
        image: str,
        workdir: str = os.getcwd(),
        client=_client,
        pull: bool = False,
        auto_start: bool = True,
        attach: bool = False,
        clean_perms_on_exit: bool = True,
    ):
        """
        Spawn an executor.

        :param image: Image tag or URI to launch
        :param workdir: Host directory to mount into the container, defaults to `os.getcwd()`
        :param client: The docker connection to use, defaults to `docker.from_env()`
        :param force_pull: Pull the image first before launching
        :param auto_start: Start the container automatically"
        :param attach: Print container logs when executing
        :param clean_perms_on_exit: Fix project directory permissions when pruning containers
        """
        self.client = client

        self.image = image
        self.workdir = workdir
        self.attach = attach
        self.clean_perms_on_exit = clean_perms_on_exit

        if pull:
            self.pull_image()

        if auto_start:
            self.start()

    @property
    def absolute_workdir(self):
        return Path(self.workdir).absolute()

    def pull_image(self, **kwargs):
        """Manually trigger an image pull."""

        return self.client.images.pull(self.image, **kwargs)

    def start(self, cmd: str = "sleep 30d", *args, **kwargs):
        """Starts the service."""

        if self.container is not None:
            log.info("Attempted to start an already-running container, which is a no-op")
            return

        abs_path = str(self.absolute_workdir)
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

        if self.attach:
            self.container.logs(stream=True, follow=True)

    def exec_all(self, *args, **kwargs):
        """Runs a series of commands in sequence, each receiving the same kwargs."""

        for arg in args:
            self.exec(arg, **kwargs)

    run = exec

    def clean_perms(self):
        """Resets the permissions of the working directory to the current UID:GID."""
        self.exec(f"chown -R {os.getuid()}:{os.getgid()} .")

    def __del__(self):
        """Ensure that the container is properly pruned when we're done with it."""
        if self.clean_perms_on_exit:
            self.clean_perms()

        self.container.stop(timeout=0)
        self.container.wait()
        self.container.remove()
