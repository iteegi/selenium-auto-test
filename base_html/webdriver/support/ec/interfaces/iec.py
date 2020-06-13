"""Interface for expected conditions."""

from abc import ABC, abstractmethod


class IExpectedConditions(ABC):
    """Interface for expected conditions."""

    @abstractmethod
    def __iter__(self):
        """Object initializer."""
        pass

    @abstractmethod
    def __call__(self):
        """Call when the instance is “called” as a function."""
        pass
