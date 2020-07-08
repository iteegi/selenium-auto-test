"""Factory method for ActionChains class."""

from selenium.webdriver.common.action_chains import ActionChains as AC
from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class ActionChains():
    """Factory Method for base class ActionChains."""

    ACTIONCHAINS_SELENIUM = AC
