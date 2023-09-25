"""Interfaces for file content databases."""


from domain.file import ReadableFile


class ContentDB:
    """Interface describing a database for file content."""

    async def save(self, id: str, contents: ReadableFile) -> None:
        """Persists file contents under the specified unique identifier.

        Args:
            id: The unique file identifier.
            contents: The contents to be persisted.
        """
        pass
