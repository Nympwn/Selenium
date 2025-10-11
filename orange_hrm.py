import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_as_admin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(3)

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.click()
    username_input.send_keys('Admin')
    password_input.click()
    password_input.send_keys('admin123')

    login_button = driver.find_element(By.TAG_NAME, 'button')
    login_button.click()
    time.sleep(3)

    admin_link = driver.find_element(By.LINK_TEXT, 'Admin')
    admin_link.click()
    time.sleep(1)
    driver.save_screenshot('screen_admin_page.png')

    time.sleep(15)

    driver.quit()