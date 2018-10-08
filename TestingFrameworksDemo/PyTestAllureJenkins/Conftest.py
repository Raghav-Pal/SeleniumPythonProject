import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://qa.moodle.net/", help="url")
    parser.addoption("--username", action="store", default="manager", help="username")
    parser.addoption("--password", action="store", default="test", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'chrome':
        browser = webdriver.Chrome()
        browser.get("about:blank")
        browser.implicitly_wait(10)
        browser.maximize_window()
        return browser
    else:
        print
        'only chrome is supported at the moment'


@pytest.fixture(scope="module")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")
