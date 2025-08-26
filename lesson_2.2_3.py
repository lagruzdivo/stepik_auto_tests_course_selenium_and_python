from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

# def sum(x, y):
#     return str(x + y)


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1) # что бы успела прогрузиться страница

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    total = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(sum(x, y))
    select.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()


