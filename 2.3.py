import math

import pyperclip as pyperclip
from selenium import webdriver
import os
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    submit = browser.find_element_by_css_selector('button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    alert = browser.switch_to.alert
    alert.accept()

    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))

    submit = browser.find_element_by_css_selector('button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл
