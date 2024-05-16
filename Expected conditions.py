from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
	 
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser = webdriver.Chrome()
    
    # говорим Selenium проверять в течение 15 секунд, пока цена объекта не станет равной $100
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button = browser.find_element(By.ID, "book").click()

    # находим элемент, содержащий текст
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной 4
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()

    print(browser.switch_to.alert.text.split(': ')[-1])