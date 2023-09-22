"""File data and metadata interfaces."""


from abc import ABC, abstractmethod


class ReadableFile(ABC):
    """File whose contents may be read."""

    @abstractmethod
    async def read(self, size: int) -> bytes:
        """Reads bytes from the file.

        Args:
            size: number of bytes to read.

        Returns:
            A bytes object with the file's contents.
        """
        pass


class FileMetadata:
    """Data about a file."""

    def __init__(self, name: str, mime_type: str, description: str | None = None):
        """Constructs a new instance with the provided information.

        Args:
            name: The name of the file.
            mime_type: String specifying the file's IANA MIME type.
            description: Optional file description.
        """
        self._name = name
        self._mime_type = mime_type
        self._description = description

    def get_description(self) -> str | None:
        """Returns the file's description.

        Returns:
            The file's description.
            "None" if the file does not have a description.
        """
        return self._description

    def get_filename(self) -> str:
        """Returns the file's name.

        Returns:
            A string containing the name of the file.
            The string will include the file extension,
            if it was originally named with one.
        """
        return self._name

    def get_mime_type(self) -> str:
        """Returns the file's MIME type.

        Returns:
            A string specifying the file's IANA MIME type.
        """
        return self._mime_type
