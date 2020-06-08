from enum import Enum
from selenium.webdriver.support import expected_conditions as EC_
from base_html.webdriver.support.ec.custom import ExecScript


class ECFabric():
    """ECFabric class."""

    @staticmethod
    def ec(choice):
        """Get EC class."""
        return choice.value

    class Choice(Enum):
        """EC collection."""

        EC = EC_
        EX = ExecScript
