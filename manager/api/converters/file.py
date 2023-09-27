"""Module for converting fastAPI file types to domain types.

Typical usage example:
    metadata = extract_metadata(upload_file)
    content = extract_content(upload_file)
"""


from domain.file import FileMetadata, ReadableFile
from fastapi import UploadFile
from typing import Optional


def _get_size(file: UploadFile) -> int:
    return file.size or 0


class ReadableUploadFileAdapter(ReadableFile):
    """Allows UploadFile to be used as a ReadableFile."""

    def __init__(self, upload_file: UploadFile):
        """Wraps the UploadFile instance."""
        self._file = upload_file

    def read(self, size: int) -> bytes:
        """Reads from the original UploadFile."""
        return self._file.file.read(size)

    def get_size(self) -> int:
        """Gets the size of the temporary file."""
        return _get_size(self._file)


def extract_metadata(
    upload_file: UploadFile, description_header: Optional[str]
) -> FileMetadata:
    """Extracts relevant metadata from a fastAPI file.

    Args:
        upload_file: a fastAPI UploadFile instance.

    Returns:
        The relevant file metadata.

    Raises:
        Exception: The file is missing the required metadata.
    """
    if not upload_file.filename:
        # TODO return proper client error response
        raise Exception("Missing filename")

    if not upload_file.content_type:
        # TODO return proper client error response
        raise Exception("Missing file content type")

    return FileMetadata(
        upload_file.filename,
        upload_file.content_type,
        _get_size(upload_file),
        description=description_header,
    )


def extract_content(upload_file: UploadFile) -> ReadableFile:
    """Converts UploadFile into a ReadableFile.

    Args:
        upload_file: a fastAPI UploadFile instance.

    Returns:
        A ReadableFile instance with the same contents
        as the original upload_file.
    """
    return ReadableUploadFileAdapter(upload_file)
