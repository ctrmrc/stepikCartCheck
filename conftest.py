import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ar, ca, cs, da, de, en-gb, el, es," \
                          "fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

@pytest.fixture(scope="function")
def browser(request):
    languageChoose = request.config.getoption("language")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    link = f"https://selenium1py.pythonanywhere.com/{languageChoose}/catalogue/coders-at-work_207/"
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()






