"""Provides a base model for defining other models."""


from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    """Base model class.

    All other model classes should inherit this one.
    """

    pass
