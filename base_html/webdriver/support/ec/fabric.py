"""Factory Methods for expected conditions from external sources."""

from selenium.webdriver.support import expected_conditions as EC_
from base_html.webdriver.support.ec.custom import ExecScriptReturnZero
from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class ECFabric():
    """Factory Method for expected conditions from Selenium.

    Custom methods added.
    """

    EC_SELENIUM = EC_
    EXEC_SCRIPT_RETURN_ZERO = ExecScriptReturnZero
