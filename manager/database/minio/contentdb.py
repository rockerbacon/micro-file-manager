"""MinIO database implementation."""


from domain.file import ReadableFile
from interfaces.contentdb import ContentDB


class MinIOContentDB(ContentDB):
    """Database for managing file contents in MinIO."""

    async def save(self, id: str, contents: ReadableFile) -> None:
        """Persist file contents under the specified unique identifier.

        Args:
            id: The unique file identifier.
            contents: The contents to be persisted.
        """
        raise Exception("Not implemented")
