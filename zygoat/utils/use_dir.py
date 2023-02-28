from contextlib import contextmanager
import os


@contextmanager
def use_dir(*args, **kwargs):
    """
    Wraps os.chdir() and returns to the original working directory on exit
    """
    owd = os.getcwd()

    try:
        os.chdir(*args, **kwargs)
        yield
    finally:
        os.chdir(owd)
