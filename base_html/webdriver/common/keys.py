"""Factory method for By class."""

from enum import Enum
from selenium.webdriver.common.keys import Keys


class KeysFabric():
    """KeysFabric class."""

    @staticmethod
    def key(os):
        """Get key."""
        return os.value()

    class OS(Enum):
        """Keyboard keys collection."""

        KEYS = Keys
