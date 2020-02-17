import logging
import pytest
from fixtures.application import Application


@pytest.fixture(scope="function")
def app(request):
    fixture = Application()

    def fin():
        if request.session.testsfailed:
            logging.info('Taking screenshot')
            driver = fixture.driver
            driver.get_screenshot_as_png()

        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

