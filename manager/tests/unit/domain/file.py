from domain.file import FileMetadata
from unittest import TestCase


class TestFileMetadata(TestCase):
    def setUp(self) -> None:
        self.metadata = FileMetadata(
            "my_test_file.txt", "text/plain", 64, description="Hello World!"
        )

    def test_should_make_description_available(self) -> None:
        self.assertEqual(self.metadata.get_description(), "Hello World!")

    def test_should_make_filname_available(self) -> None:
        self.assertEqual(self.metadata.get_filename(), "my_test_file.txt")

    def test_should_make_mime_type_available(self) -> None:
        self.assertEqual(self.metadata.get_mime_type(), "text/plain")

    def test_should_make_size_available(self) -> None:
        self.assertEqual(self.metadata.get_size(), 64)
