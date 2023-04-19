from watchfiles import run_process


def watch() -> None:
    run_process(".", target="poetry run pytest -rA -m 'not slow'")
