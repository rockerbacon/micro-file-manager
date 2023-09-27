"""Factory for instantiating ContentDB.

Typical usage example:
    contentdb = get_contentdb()
"""


from database.minio.contentdb import MinIOContentDB
from interfaces.contentdb import ContentDB
from .singleton import Singleton


def _init_contentdb() -> ContentDB:
    return MinIOContentDB()


_singleton = Singleton[ContentDB](_init_contentdb)


def get_contentdb() -> ContentDB:
    """Gets the default ContentDB implementation.

    Only a single instance of ContentDB will ever be created,
    even if this function is called multiple times.

    Returns:
        A singleton ContentDB instance.
    """
    return _singleton.get()
