"""Factory for instantiating the app's environment.

Typical usage example:
    env = get_env()
"""


from environment.app import AppEnvironment
from environment.envfile import DotenvReader
from environment.process import ProcessEnvReader
from .singleton import Singleton


def _init_env() -> AppEnvironment:
    return AppEnvironment(
        ProcessEnvReader(),
        DotenvReader(),
    )


_singleton = Singleton[AppEnvironment](_init_env)


def get_env() -> AppEnvironment:
    """Gets the application environment configuration.

    Only a single instance of AppEnvironment will ever be created,
    even if this function is called multiple times.

    Returns:
        A singleton AppEnvironment instance.
    """
    return _singleton.get()
