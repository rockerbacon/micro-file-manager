"""File metadata ORM."""


from .base import BaseModel
from sqlalchemy import DateTime, String
from sqlalchemy.orm import mapped_column


class FileMetadataModel(BaseModel):
    """file_metadata table mappings."""

    __tablename__ = "file_metadata"
    created_at = mapped_column(DateTime, nullable=False)
    description = mapped_column(String, nullable=True)
    mime_type = mapped_column(String, nullable=False)
    name = mapped_column(String, primary_key=True)
