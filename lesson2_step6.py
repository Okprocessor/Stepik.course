from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение x = 760
    treasure = browser.find_element_by_id("treasure")
    treasure_value = treasure.get_attribute("valuex")
    x = treasure_value
    y = calc(x)

    # вставляем значение функции в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # checkbox 'I'm the robot'
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()

    # radiobutton 'Robots Rule'
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()

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
