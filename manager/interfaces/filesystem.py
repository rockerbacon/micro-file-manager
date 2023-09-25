"""Interfaces for filesystem entities.

A filesystem entity is responsible for managing
file contents and metadata within the system.
"""


from abc import ABC, abstractmethod
from domain.file import FileMetadata, ReadableFile


class Filesystem(ABC):
    """Interface describing filesystem operations."""

    @abstractmethod
    async def save(self, metadata: FileMetadata, contents: ReadableFile) -> None:
        """Persists file in the filesystem.

        Args:
            metadata: The file metadata.
            contents: The file contents themselves.
        """
        pass
