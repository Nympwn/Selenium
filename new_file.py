from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Информация о драйвере
print('Driver path (service.path):', service.path)
print('Driver path (via driver):', driver.service.path)

# Информация о браузере
caps = driver.capabilitiesa

driver = webdriver.Chrome() # запуск браузера
driver.get('https://www.google.com/') # открытие ресурса
element = driver.find_element(By.NAME, 'q') # находим элемент с локатором name='q'
element.click() # клик на элемент
element.send_keys('Кошка') # введение значения в строку
element.send_keys(Keys.ENTER)

time.sleep(30)
element = driver.find_element(By.NAME, 'q')
element.clear() # очистка поля ввода
element.send_keys('Собака')
element.send_keys(Keys.ENTER)
time.sleep(30)

driver.quit() # закрытие браузера

driver.back() # перейти назад по истории браузера (прошлая страница)
driver.forward() # перейти вперед по истории браузера
# должна быть прошлая/будущая страница, иначе переход не сработает
driver.refresh() # обновить страницу