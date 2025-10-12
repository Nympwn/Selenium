import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_example(driver):
    driver.get('http://example.com')
    time.sleep(5)

    button = driver.find_element(By.LINK_TEXT, 'Learn more')
    time.sleep(5)

    assert 'Learn more' in button.text

    button.click()
    time.sleep(5)

    assert 'example-domains' in driver.current_url