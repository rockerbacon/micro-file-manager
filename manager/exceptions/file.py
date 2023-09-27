"""File related exceptions."""


from .base import DomainException


class FileAlreadyExistsError(DomainException):
    """File of the same name already exists."""

    pass
