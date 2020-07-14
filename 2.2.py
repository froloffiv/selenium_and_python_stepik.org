import pyperclip as pyperclip
from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Ilya")
    browser.find_element_by_name("lastname").send_keys("Frolov")
    browser.find_element_by_name("email").send_keys("email@email.com")
    browser.find_element_by_id("file").send_keys(file_path)
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
