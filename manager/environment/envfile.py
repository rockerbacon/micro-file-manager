"""Module for reading environment files."""


from dotenv import dotenv_values
from .reader import EnvironmentReader
from typing import cast


class DotenvReader(EnvironmentReader):
    """Reads the .env file."""

    def __init__(self) -> None:
        """Instantiates the reader.

        The .env file will be read immediately upon instantiation.
        """
        self._variables = dotenv_values(".env")

    def has(self, variable: str) -> bool:
        """Checks whether or not variable is defined in the .env file.

        Args:
            variable: The variable to check.

        Returns:
            True if variable is defined and False otherwise.
        """
        return variable in self._variables

    def get(self, variable: str) -> str:
        """Gets value of an environment variable from the .env file.

        The caller can check whether the variable is set
        or not with has() before attempting to get its value.

        Args:
            variable: The variable for which to get a value.

        Returns:
            A string representing the variable's value.

        Raises:
            Exception: variable is not defined in the .env file.
        """
        if not self.has(variable):
            raise Exception(f"Variable '{variable}' not defined in .env")

        return cast(str, self._variables[variable])
