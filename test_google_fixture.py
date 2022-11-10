from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------setup--------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')

    yield
    print("-------------Tear down--------------------")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title(init_driver):
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/"
