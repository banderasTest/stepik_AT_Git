from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем кнопку-алерт
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    time.sleep(1)

    # принимаем кнопку конфирм
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    # находим элемент, содержащий текст
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    time.sleep(1)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    time.sleep(1)


finally:
    # выводим результат выполнения задания на консоль1
    print(browser.switch_to.alert.text)
    # или так
    print(browser.switch_to.alert.text.split(': ')[-1])
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()