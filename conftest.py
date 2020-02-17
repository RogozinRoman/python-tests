import logging
import sys
import pytest


settings = {}


def pytest_addoption(parser):
    parser.addoption("--browser",
                     dest="browser",
                     metavar='browser',
                     default="chrome",
                     help="Browser. Default option is chrome")
    parser.addoption("--ip",
                     help="A way to override the DEFAULT_IP for your tests.",
                     dest="id",
                     metavar='ip',
                     default="192.168.1.1")
    parser.addoption("--remote",
                     help="(boolean) Make the tests only run tests remotely",
                     dest="remote",
                     metavar='remote',
                     default=False)
    parser.addoption("--remote_ip",
                     help="A way to set remote url of selenoid",
                     dest="remote_ip",
                     metavar='remote_ip',
                     default='192.168.1.1')
    parser.addoption("--remote_port",
                     help="A way to set remote url of selenoid",
                     dest="remote_port",
                     metavar='remote_port',
                     default='4444')


def pytest_configure(config):
    settings['browser'] = config.getoption('--browser')
    settings['ip'] = config.getoption('--ip')
    settings['remote'] = config.getoption('--remote')
    settings['remote_ip'] = config.getoption('--remote_ip')
    settings['remote_port'] = config.getoption('--remote_port')


@pytest.fixture(scope="function")
def new_client(request):
    pass


@pytest.fixture(scope="function")
def conditions_fixture(request):
    pass


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    handlers=[
                        logging.FileHandler("autotests.log", mode='w', encoding='utf-8'),
                        logging.StreamHandler(stream=sys.stdout)
                    ])


def browser():
    return settings['browser']


def ip():
    return settings['ip']


def host():
    return "http://%s" % ip()


def base_url():
    return host()


def remote():
    return settings['remote']


def remote_ip():
    return settings['remote_ip']


def remote_port():
    return settings['remote_port']


IMPLICITLY_WAIT = 1
