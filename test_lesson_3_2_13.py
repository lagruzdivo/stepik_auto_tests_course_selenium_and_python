from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self): # вызывается перед каждым тестом
        self.browser = webdriver.Chrome()
    def tearDown(self): # вызывается после каждого теста
        self.browser.quit()

    def test_registration1(self): # тест для регистрации по ссылке 1
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        # заполняем поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Iva")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Ivan@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # проверяем совпадает ли ожидаемый текст с текстом на странице
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self): # тест для регистрации по ссылке 2
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")

        # заполняем поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Iva")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Ivan@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # проверяем совпадает ли ожидаемый текст с текстом на странице
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == '__main__':
    unittest.main()