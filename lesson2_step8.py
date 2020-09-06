from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # иищем список с id = dropdown
    browser.find_element_by_id("dropdown").click()

    num1 = browser.find_element_by_id('num1')
    num1_num = int(num1.text)

    num2 = browser.find_element_by_id('num2')
    num2_num = int(num2.text)
    num_answer = str(num1_num + num2_num)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(num_answer)

    # нажимаем кнопку Submit
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # ждем загрузки страницы
    time.sleep(3)

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
