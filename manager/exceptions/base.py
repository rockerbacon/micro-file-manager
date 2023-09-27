"""Base exceptions.

All domain exceptions should inherit from one of the classes contained here.
"""


class DomainException(Exception):
    """Base domain exception.

    All domain errors extend this class,
    either directly or indirectly.
    """

    pass
