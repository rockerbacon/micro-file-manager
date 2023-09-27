"""Interface for reading enviroment variables."""


from abc import ABC, abstractmethod


class EnvironmentReader(ABC):
    """Reads environment variables."""

    @abstractmethod
    def has(self, variable: str) -> bool:
        """Checks whether or not variable is defined.

        Args:
            variable: The variable to check.

        Returns:
            True if variable is defined and False otherwise.
        """
        pass

    @abstractmethod
    def get(self, variable: str) -> str:
        """Gets value of an environment variable.

        The caller can check whether the variable is set
        or not with has() before attempting to get its value.

        Args:
            variable: The variable for which to get a value.

        Returns:
            A string representing the variable's value.

        Raises:
            Exception: variable is not defined in this environment.
        """
        pass
