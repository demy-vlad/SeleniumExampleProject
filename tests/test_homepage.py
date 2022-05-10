import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homapage(self):
        driver = webdriver.Chrome()
        driver.get('https://ek.ua/')
        wait = WebDriverWait(driver, 15, 0.2)

        logo = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div.s-catalog-subcat > a')))
        logo.click()
        print(driver.title)
