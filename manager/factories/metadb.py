"""Factory for instantiating MetaDB.

Typical usage example:
    metadb = get_metadb()
"""


from database.postgresql.metadb import PostgreSQLMetaDB
from interfaces.metadb import MetaDB
from .singleton import Singleton


def _init_metadb() -> MetaDB:
    return PostgreSQLMetaDB()


_singleton = Singleton[MetaDB](_init_metadb)


def get_metadb() -> MetaDB:
    """Gets the default MetaDB implementation.

    Only a single instance of MetaDB will ever be created,
    even if this function is called multiple times.

    Returns:
        A singleton MetaDB instance.
    """
    return _singleton.get()
