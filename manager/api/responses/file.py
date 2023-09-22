"""File response classes."""


from domain.file import FileMetadata
from fastapi import Response, status


class FileResponseMetadata(Response):
    """HTTP response containing file metadata headers."""

    def __init__(
        self, metadata: FileMetadata, status_code: int = status.HTTP_204_NO_CONTENT
    ):
        """Creates a response having file metadata headers.

        Args:
            metadata: The file metadata.
            status_code: The response's HTTP status code.
        """
        Response.__init__(self, status_code=status_code)
        self.headers["content-type"] = metadata.get_mime_type()
        self.headers[
            "content-disposition"
        ] = f'multipart/form-data; filename="{metadata.get_filename()}"'

        description = metadata.get_description()
        if description:
            self.headers["x-description"] = description
