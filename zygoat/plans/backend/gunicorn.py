import os
from zygoat.utils import inject_resource_file


def inject_gunicorn_conf(workdir):
    file_name = os.path.join(workdir, "gunicorn.conf.py")
    inject_resource_file(file_name)
