from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    input3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)



finally:
    time.sleep(10)
    browser.quit()