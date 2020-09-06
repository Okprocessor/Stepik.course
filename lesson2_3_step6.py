from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    # проходим по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # переходим на новую страницу
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # считываем значение x = 760
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # вставляем значение функции в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

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


finally:
    # Проверяем, что смогли зарегистрироваться
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
