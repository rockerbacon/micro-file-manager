"""Interfaces for file metadata databases."""


from domain.file import FileMetadata


class MetaDB:
    """Interface describing a database for file metadata."""

    async def save(self, id: str, metadata: FileMetadata) -> None:
        """Persists file metadata under the specified unique identifier.

        Args:
            id: The unique file identifier.
            metadata: The metadata to be persisted.
        """
        pass
