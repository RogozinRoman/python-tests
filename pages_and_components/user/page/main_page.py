import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages_and_components.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, app):
        super().__init__(app)
        self.driver = app.driver
        self._banner = (By.XPATH, ".//*[@class='banner__container']")

    def wait_for_loading(self):
        logging.info(f'Waiting for {self.__class__.__name__} loading')
        self.wait.until(ec.visibility_of_element_located(self._banner))

