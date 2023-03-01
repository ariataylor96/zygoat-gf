import os
from zygoat.utils import inject_file_contents, resource_file_contents


def inject_gunicorn_conf(workdir):
    file_name = os.path.join(workdir, "gunicorn.conf.py")
    inject_file_contents(
        file_name,
        resource_file_contents(file_name),
    )
