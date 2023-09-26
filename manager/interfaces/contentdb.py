"""Interfaces for file content databases."""


from abc import ABC, abstractmethod
from domain.file import ReadableFile


class ContentDB(ABC):
    """Interface describing a database for file content."""

    @abstractmethod
    async def save(self, id: str, contents: ReadableFile) -> None:
        """Persists file contents under the specified unique identifier.

        Args:
            id: The unique file identifier.
            contents: The contents to be persisted.
        """
        pass
