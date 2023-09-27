"""PostgreSQL database implementation."""


from datetime import datetime
from domain.file import FileMetadata
from .engine import Session
from exceptions.file import FileAlreadyExistsError
from interfaces.metadb import MetaDB
from .models.file_metadata import FileMetadataModel
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from typing import Any


class PostgreSQLMetaDB(MetaDB):
    """Database for managing file metadata in PostgreSQL."""

    def __init__(self, session_maker: sessionmaker[Any] = Session):
        """Instantiates a new PostgresMetaDB.

        Args:
            session_maker: SQL Alchemy session maker.
        """
        self._sessionmaker = Session

    async def save(self, id: str, metadata: FileMetadata) -> None:
        """Persists file metadata under the specified unique identifier.

        Args:
            id: The unique file identifier.
            metadata: The metadata to be persisted.

        Raises:
            FileAlreadyExistsError: Metadata for the specified id already
            exists in the database.
        """
        try:
            with self._sessionmaker.begin() as session:
                session.add(
                    FileMetadataModel(
                        created_at=datetime.now(),
                        description=metadata.get_description(),
                        mime_type=metadata.get_mime_type(),
                        name=metadata.get_filename(),
                    )
                )
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                raise FileAlreadyExistsError()
            else:
                raise e
