"""Base singleton implementation.

Typical usage example:

def init_instance():
    return MyClass()

singleton = Singleton(init_instance)
instance1 = singleton.get()
instance2 = singleton.get()
"""


from typing import Callable, Generic, Optional, TypeVar


T = TypeVar("T")


class Singleton(Generic[T]):
    """Base singleton pattern implementation."""

    _init_instance: Callable[[], T]
    _instance: Optional[T]

    def __init__(self, init_instance: Callable[[], T]) -> None:
        """Creates a new singleton.

        Args:
            init_instance: The function which initializes the
            singleton object.
        """
        self._init_instance = init_instance
        self._instance = None

    def get(self) -> T:
        """Gets the singleton instance.

        When first called, this method will execute the function
        provided to the constructor and cache its return.
        Subsequent calls will simply return the cached value.
        """
        if self._instance is None:
            self._instance = self._init_instance()

        return self._instance
