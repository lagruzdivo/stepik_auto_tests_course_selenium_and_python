import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def browser(request, user_language=None):
    options = Options()
    options.add_experimental_option("prefs", {'intl.accept_languages' : user_language})
    browser = webdriver.Chrome(options=options)




