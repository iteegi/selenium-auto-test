"""Interface for iterators."""

from abc import ABC, abstractmethod


class IIterator(ABC):
    """Interface for custom iterators."""

    @abstractmethod
    def get_item(self):
        """Return one web element per call."""
        pass
