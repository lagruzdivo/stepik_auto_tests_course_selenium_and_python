from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5) # неявное ожидание
browser.get("http://suninjuly.github.io/wait1.html")

# time.sleep(1) # ожидание
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text