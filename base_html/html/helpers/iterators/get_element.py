from selenium.webdriver.support.wait import WebDriverWait

#
# def f(self, locators, quantity=1, time=10):
#     # el = len(self.find_elmnts(c))
#     for i in range(quantity):
#         elm = WebDriverWait(self.driver, time).until(
#             lambda x: x.find_elements(*locators))
#         yield elm[i]


class F():
    def __init__(self, driver, locators, quantity=1, time=10):
        self.__driver = driver
        self.__locators = locators
        self.__quantity = quantity
        self.__time = time

    def it(self):
        for i in range(self.__quantity):
            elm = WebDriverWait(self.__driver, self.__time).until(
                lambda x: x.find_elements(*self.__locators))
            yield elm[i]
