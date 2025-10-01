import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()  # Загружает переменные из .env

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_url(browser, url):
    answer = str(math.log(int(time.time())))

    browser.get(url)
    browser.implicitly_wait(10)
    # login
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.NAME, "login").send_keys(os.getenv('STEPIK_EMAIL'))
    browser.find_element(By.NAME, "password").send_keys(os.getenv('STEPIK_PASSWORD'))
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    time.sleep(3) # ждем загрузки после логина

    # находим окно для ввода
    textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
    textarea.clear()
    textarea.send_keys(answer) # вставляем значение
    # нажимаем кнопку Отправить
    WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
    # ждем появления результата
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))

    # ищем ответ в появившемся блоке и записываем его в переменную
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    # ПРИНТ ДЛЯ ОТЛАДКИ - всегда покажет текст
    print(f"=== ТЕКСТ ОШИБКИ ДЛЯ {url}: '{result}' ===")

    # сравниваем с Correct!
    assert result == "Correct!", f"Expected 'Correct!', got '{result}'"

