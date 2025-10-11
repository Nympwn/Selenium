import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://example.com')
time.sleep(5)

element = driver.find_element(By.LINK_TEXT, 'Learn more')
element.click()
time.sleep(5)

driver.quit()