from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import conftest
import logging


class Application:

    def get_webdriver(self):

        if conftest.remote():
            if conftest.browser() == 'chrome':
                capabilities = {
                    "browserName": "chrome",
                    "version": "73.0",
                    "enableVNC": True,
                    "enableVideo": False,
                    "screenResolution": "1980x1024x24"
                }
            else:
                logging.error('WebDriver for browser ' + str(conftest.browser()).upper() + " not found")
                raise FileNotFoundError()
            command_executor = 'http://%s:%s/%s' % (conftest.remote_ip(), conftest.remote_port(), "wd/hub")
            driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities)
            session_url = 'http://%s:8080/#/sessions/%s' % (conftest.remote_ip(), driver.session_id)
            logging.info(f'Remote session id: {session_url}')
            driver.set_window_size(1980, 1024)
            return driver
        else:
            if conftest.browser() == 'chrome':
                driver = webdriver.Chrome(executable_path=ChromeDriverManager("2.43").install())
                driver.fullscreen_window()
                return driver
            else:
                return webdriver.Firefox()

    def __init__(self):
        self.driver = self.get_webdriver()
        self.driver.implicitly_wait(conftest.IMPLICITLY_WAIT)
        self.window_staff = None
        self.window_client = None

    def destroy(self):
        self.driver.quit()

    def switch_to_staff(self):
        if self.window_staff is None:
            raise Exception('Staff is not initialised')
        self.driver.switch_to.window(self.window_staff)

    def switch_to_client(self):
        if self.window_client is None:
            raise Exception('Client is not initialised')
        self.driver.switch_to.window(self.window_client)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def open_new_tab(self):
        self.driver.execute_script('''window.open("about:blank", "_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles) - 1])

    def save_staff_tab(self):
        self.window_staff = self.driver.current_window_handle

    def save_client_tab(self):
        self.window_client = self.driver.current_window_handle

    def remove_implicitly_wait(self):
        self.driver.implicitly_wait(0)

    def restore_implicitly_wait(self):
        self.driver.implicitly_wait(conftest.IMPLICITLY_WAIT)

    def wait_for_dom_ready(self):
        self.driver.execute_script('return document.readyState;')


class TokenNotProvidedException(Exception):
    def __init__(self, text):
        self.txt = text
