"""MinIO database implementation."""


import asyncio
from .client import minio_client
from domain.file import ReadableFile
from env import env
from interfaces.contentdb import ContentDB
from minio import Minio


class MinIOContentDB(ContentDB):
    """Database for managing file contents in MinIO."""

    def __init__(self, bucket: str = env.MINIO_BUCKET, client: Minio = minio_client):
        """Initializes a ContentDB for managing file contents in MinIO.

        Args:
            bucket: The MinIO bucket where file contents should be stored.
            Will be automatically created if it does not already exist.

            client: The Minio instance to use when communicating with
            the MinIO server.
        """
        self._bucket = bucket
        self._client = client

        self._bucket_assertion = asyncio.create_task(self._assert_bucket())

    async def _assert_bucket(self) -> None:
        if not self._client.bucket_exists(self._bucket):
            self._client.make_bucket(self._bucket)
            # TODO configure bucket policy

    async def save(self, id: str, contents: ReadableFile) -> None:
        """Persist file contents under the specified unique identifier.

        Args:
            id: The unique file identifier.
            contents: The contents to be persisted.
        """
        await self._bucket_assertion
        self._client.put_object(self._bucket, id, contents, contents.get_size())
