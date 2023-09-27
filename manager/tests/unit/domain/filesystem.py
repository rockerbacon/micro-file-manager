from domain.file import FileMetadata, ReadableFile
from domain.filesystem import MixedFilesystem
from interfaces.contentdb import ContentDB
from interfaces.metadb import MetaDB
from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import MagicMock
from typing import cast


class ContentDBMock(ContentDB):
    def __init__(self) -> None:
        self.save_mock = MagicMock()

    async def save(self, id: str, contents: ReadableFile) -> None:
        self.save_mock(id, contents)


class MetaDBMock(MetaDB):
    def __init__(self) -> None:
        self.save_mock = MagicMock()

    async def save(self, id: str, metadata: FileMetadata) -> None:
        self.save_mock(id, metadata)


class FileContentsMock(ReadableFile):
    def __init__(self) -> None:
        self.read_mock = MagicMock()

    def read(self, size: int) -> bytes:
        return cast(bytes, self.read_mock(size))

    def get_size(self) -> int:
        return 42


class TestMixedFilesystem_Save(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.file_contents = FileContentsMock()
        self.file_metadata = FileMetadata(
            "test_file.txt",
            "text/plain",
            self.file_contents.get_size(),
            description="My test file",
        )
        self.contentDB = ContentDBMock()
        self.metaDB = MetaDBMock()
        self.fs = MixedFilesystem(self.metaDB, self.contentDB)

    async def test_should_save_when_file_does_not_exist(self) -> None:
        await self.fs.save(self.file_metadata, self.file_contents)
        self.metaDB.save_mock.assert_called_with("test_file.txt", self.file_metadata)
        self.contentDB.save_mock.assert_called_with("test_file.txt", self.file_contents)


if __name__ == "__main__":
    main()
