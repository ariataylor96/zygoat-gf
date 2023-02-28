import os
import shlex


def docs():
    os.execvp("pdoc", shlex.split("pdoc -n zygoat"))
