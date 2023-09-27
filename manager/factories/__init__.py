"""Provides functions for initializing concrete instances.

This project mostly makes heavy use of abstract interfaces and dependency inversion.
The goal of this package is to provide functions for easy instantiation of the
concrete implementations of these abstract interfaces.

You can imagine it as a minimalist substitute for standard dependency injection.

Altough the name "factory" is used,
the underlying implementations of each function can vary and
are not necessarily exact implementations of the Factory design pattern.
"""
