import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_experimental_option('prefs', {
        'profile.password_manager_leak_detection': False
    })
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_as_admin(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)

# Авторизация

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.click()
    username_input.send_keys('Admin')
    password_input.click()
    password_input.send_keys('admin123')

    login_button = driver.find_element(By.TAG_NAME, 'button')
    login_button.click()
    driver.implicitly_wait(5)

    admin_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Admin'))
    )

    assert 'dashboard' in driver.current_url, 'Не удалось войти в систему'
    assert admin_link.is_displayed(), 'Ссылка Admin не отображается на странице или не найдена'

    admin_link.click()
    driver.implicitly_wait(5)
    driver.save_screenshot('screen_admin_page.png')