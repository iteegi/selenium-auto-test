"""List interfaces for chekers text."""

from abc import ABC, abstractmethod


class ICheckText(ABC):
    """Interface for Chekers Text."""

    @abstractmethod
    def check_text(self) -> bool:
        """Check for specific text in a web element."""
        pass
