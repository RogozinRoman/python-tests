import logging

from pages_and_components.user.page.main_page import MainPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_success(self, app):
        logging.info('app loaded')
        main_page = MainPage(app)
        main_page.open()

    def test_login_fail(self, app):
        pass
