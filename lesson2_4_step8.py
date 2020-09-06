import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button01 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button02 = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button02.click()

    # считываем значение x = 760
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    button03 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button03)
    button03.send_keys(y)
    button03.click()

    # вставляем значение функции в поле
    # input1 = browser.find_element_by_id("answer")


    # нажимаем кнопку Submit
    button04 = browser.find_element_by_css_selector("[type='submit']")
    button04.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
