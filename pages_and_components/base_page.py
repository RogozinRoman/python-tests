from selenium.webdriver.support.wait import WebDriverWait
from properties.PropertiesLoader import PropertiesLoader


class BasePage:

    def __init__(self, app):
        self.app = app
        self._properties = PropertiesLoader()
        self._port = self._properties.users_port
        self._base_url = self._properties.host
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, self._properties.wait_delay)

    def open(self):
        self.driver.get(self._base_url)
