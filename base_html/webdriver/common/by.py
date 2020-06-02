"""Factory method for By class."""

from enum import Enum
from selenium.webdriver.common.by import By


class ByFabric():
    """ByFabric class."""

    @staticmethod
    def by(os):
        """Get By class."""
        return os.value()

    class OS(Enum):
        """BY collection."""

        BY = By
