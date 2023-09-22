"""Module for managing file storage."""


import asyncio
from .file import FileMetadata, ReadableFile
from interfaces.contentdb import ContentDB
from interfaces.filesystem import Filesystem
from interfaces.metadb import MetaDB


class MixedFilesystem(Filesystem):
    """Filesystem utilizing multiple databases.

    This filesystem utilizes one database for storing metadata and
    another for storing the file contents themselves.
    """

    def __init__(self, metaDB: MetaDB, contentDB: ContentDB):
        """Initializes a filesystem.

        Args:
            metaDB: Database to utilize for file metadata.
            contentDB: Database to utilize for file contents.
        """
        self._metaDB = metaDB
        self._contentDB = contentDB

    async def save(self, metadata: FileMetadata, contents: ReadableFile) -> None:
        """Persists a file in the filesystem.

        Metadata will be stored in the metaDB specified during initialization,
        and the file contents will be stored in the fileDB.

        Args:
            metadata: The file metadata.
            contents: The file contents themselves.
        """
        id = metadata.get_filename()
        # TODO check existing metadata before moving to the file upload
        await asyncio.gather(
            self._metaDB.save(id, metadata), self._contentDB.save(id, contents)
        )
