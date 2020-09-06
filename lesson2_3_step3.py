from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # принимаем аллерт (ОК)
    confirm = browser.switch_to.alert
    confirm.accept()

    # считываем значение x = 760
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # вставляем значение функции в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # нажимаем кнопку Submit
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
