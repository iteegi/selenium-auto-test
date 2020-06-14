"""Interface for expected conditions."""

from abc import ABC, abstractmethod


class IExpectedConditions(ABC):
    """Interface for expected conditions."""

    @abstractmethod
    def __init__(self):
        """Object initializer."""
        pass

    @abstractmethod
    def __call__(self):
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        pass
