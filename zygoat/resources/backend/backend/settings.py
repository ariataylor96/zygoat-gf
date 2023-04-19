import environ
from typing import Optional

env = environ.Env()

PRODUCTION = env.bool("DJANGO_PRODUCTION", default=False)
DEBUG = False if PRODUCTION else env.bool("DJANGO_DEBUG", default=True)


def prod_required_env(key: str, default: any, method: str = "str") -> Optional[any]:
    if PRODUCTION:
        raise KeyError(f"Missing required prod configuration key {key}")

    return getattr(env, method)(key, default)
