"""Interfaces for file metadata databases."""


from abc import ABC, abstractmethod
from domain.file import FileMetadata


class MetaDB(ABC):
    """Interface describing a database for file metadata."""

    @abstractmethod
    async def save(self, id: str, metadata: FileMetadata) -> None:
        """Persists file metadata under the specified unique identifier.

        Args:
            id: The unique file identifier.
            metadata: The metadata to be persisted.

        Raises:
            FileAlreadyExistsError: Metadata for the specified id already
            exists in the database.
        """
        pass
