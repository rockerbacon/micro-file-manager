"""Loads environment configuration.

Typical usage example:
    print(env.POSTGRESQL_DB)
"""


from dotenv import dotenv_values
import os


class Environment:
    """Relevant environment variables."""

    POSTGRESQL_DB: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_PORT: int
    POSTGRESQL_USER: str

    def _load_dotfile(self) -> None:
        self._dotfile = dotenv_values(".env")

    def _load_external_value(self, variable: str) -> str | None:
        if variable in os.environ:
            return os.environ[variable]

        if variable in self._dotfile:
            return self._dotfile[variable]

        return None

    def _load_str(self, variable: str, default: str) -> str:
        value = self._load_external_value(variable)

        if value is not None:
            return value

        return default

    def _load_int(self, variable: str, default: int) -> int:
        value = self._load_external_value(variable)

        if value is not None:
            return int(value)

        return default

    def __init__(self) -> None:
        """Loads environment variables.

        Variables are first read from the process environment.
        Variables not specified in the process environment will be
        read from a .env file in the current working directory.

        If a variable is not specified anywhere,
        a default value for a local environment will be used.
        """
        self._load_dotfile()

        self.POSTGRESQL_DB = self._load_str("POSTGRESQL_DB", "file_manager")
        self.POSTGRESQL_HOST = self._load_str("POSTGRESQL_HOST", "localhost")
        self.POSTGRESQL_PASSWORD = self._load_str("POSTGRESQL_PASSWORD", "postgres")
        self.POSTGRESQL_PORT = self._load_int("POSTGRESQL_PORT", 5432)
        self.POSTGRESQL_USER = self._load_str("POSTGRESQL_USER", "postgres")


env = Environment()
