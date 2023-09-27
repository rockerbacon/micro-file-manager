from api.converters.file import extract_metadata, extract_content
from fastapi import UploadFile
from unittest import expectedFailure, TestCase, main
from unittest.mock import MagicMock
from typing import cast, Optional


class MockTemporaryFile:
    read: MagicMock
    size: Optional[int]

    def __init__(self) -> None:
        self._data = bytes("Hello World!", "utf8")
        self.read = MagicMock(return_value=self._data)
        self.size = len(self._data)


class MockUploadFile:
    content_type: Optional[str]
    file: MockTemporaryFile
    filename: Optional[str]
    size: Optional[int]

    def __init__(self) -> None:
        self.file = MockTemporaryFile()
        self.filename = "my_test_file.txt"
        self.content_type = "text/plain"
        self.size = self.file.size


class TestFileConversion(TestCase):
    file: UploadFile

    def setUp(self) -> None:
        self.file = cast(UploadFile, MockUploadFile())

    def test_should_extract_metadata_from_fastapi_file_without_description(
        self,
    ) -> None:
        metadata = extract_metadata(self.file, None)
        self.assertEqual(metadata.get_filename(), self.file.filename)
        self.assertEqual(metadata.get_mime_type(), self.file.content_type)
        self.assertEqual(metadata.get_size(), self.file.size)
        self.assertEqual(metadata.get_description(), None)

    def test_should_extract_metadata_from_fastapi_file_with_description(self) -> None:
        metadata = extract_metadata(self.file, "Just a test file")
        self.assertEqual(metadata.get_filename(), self.file.filename)
        self.assertEqual(metadata.get_mime_type(), self.file.content_type)
        self.assertEqual(metadata.get_size(), self.file.size)
        self.assertEqual(metadata.get_description(), "Just a test file")

    @expectedFailure
    def test_should_fail_extracting_metadata_when_fastapi_file_is_missing_filename(
        self,
    ) -> None:
        cast(MockUploadFile, self.file).filename = None
        extract_metadata(self.file, None)

    @expectedFailure
    def test_should_fail_extracting_metadata_when_fastapi_file_is_missing_mime_type(
        self,
    ) -> None:
        cast(MockUploadFile, self.file).content_type = None
        extract_metadata(self.file, None)

    def test_should_extract_contents_from_fastapi_file(self) -> None:
        content = extract_content(self.file)
        self.assertEqual(content.get_size(), cast(MockUploadFile, self.file).file.size)
        file_bytes = content.read(12)
        self.assertEquals(file_bytes, bytes("Hello World!", "utf8"))
        cast(MockUploadFile, self.file).file.read.assert_called_with(12)


if __name__ == "__main__":
    main()
