import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.headless = False  # Using a headless browser version
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1024,768')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    # url = 'https://ek.ua/'
    # if request.cls is not None:
    #     request.cls.driver = driver
    # driver.get(url)
    # yield driver
    driver.quit()