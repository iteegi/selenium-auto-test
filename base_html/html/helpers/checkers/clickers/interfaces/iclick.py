"""List interfaces for clickers."""

from abc import ABC, abstractmethod


class IClick(ABC):
    """Interface for clikers."""

    @abstractmethod
    def run(self) -> bool:
        """To run the test."""
        pass
