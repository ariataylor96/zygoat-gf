from zygoat.plans import frontend, backend

_plans = [
    frontend,
    backend,
]


def entrypoint(*args, **kwargs):
    return [p.entrypoint(*args, **kwargs) for p in _plans]
