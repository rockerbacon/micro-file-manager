"""Files router module."""

from api.converters.file import extract_content, extract_metadata
from api.responses.file import FileAlreadyExistsResponse, FileResponseMetadata
from exceptions.file import FileAlreadyExistsError
from factories.filesystem import get_filesystem
from fastapi import APIRouter, Header, Response, status, UploadFile
from typing import Annotated


fs = get_filesystem()
router = APIRouter(prefix="/files")


@router.post("")
async def post(
    file: UploadFile, x_description: Annotated[str | None, Header()] = None
) -> Response:
    """Persists file in the server's storage.

    Returns:
        Empty HTTP response containing file metadata in the headers.
    """
    metadata = extract_metadata(file, x_description)
    content = extract_content(file)

    try:
        await fs.save(metadata, content)

        return FileResponseMetadata(metadata, status_code=status.HTTP_201_CREATED)
    except FileAlreadyExistsError:
        return FileAlreadyExistsResponse()
