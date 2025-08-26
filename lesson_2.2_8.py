from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.NAME, "firstname")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.NAME, "lastname")
    input_last_name.send_keys("Ivanov")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("odin@mail.com")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, "file.txt")
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    input_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()





