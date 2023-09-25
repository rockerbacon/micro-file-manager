"""Factory for instantiating Filesystem.

Typical usage example:
    fs = get_filesystem()
"""


from .contentdb import get_contentdb
from domain.filesystem import MixedFilesystem
from interfaces.filesystem import Filesystem
from .metadb import get_metadb
from .singleton import Singleton


def _init_filesystem() -> Filesystem:
    return MixedFilesystem(get_metadb(), get_contentdb())


_singleton = Singleton[Filesystem](_init_filesystem)


def get_filesystem() -> Filesystem:
    """Gets the default Filesystem implementation.

    Only a single instance of Filesystem will ever be created,
    even if this function is called multiple times.

    Returns:
        A singleton Filesystem instance.
    """
    return _singleton.get()
