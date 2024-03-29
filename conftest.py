import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.base_page import BasePage
from .pages.locators import SignInLocators
from .pages.locators import BasePageLocators

# парсинг аргументов из консоли
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: 'ru' or 'en'")
    parser.addoption('--headless', action='store', default='None',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture(scope="function")
def support_browser(request):
    # Значения переменных user_language / browser_name / headless принимаются из консоли.
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')


    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()

        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Скрывать окно браузера - 'Chrome'
        if headless == 'true':
            options.add_argument('headless')

        # // Отключение сообщений в консоли типа: USB: usb_device_handle...
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # // Выбор языка страницы
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10) # Не явное ожидание элементов 20 сек.

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # Скрывать окно браузера -  'Firefox', через импорт библиотеки 'os'
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'



        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Для Firefox  браузера
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(10)  # Не явное ожидание элементов 20 сек.

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def open_location_sign_in_page(support_browser):
    link = SignInLocators.LINC_LOCATION_SIGN_IN_PAGE
    page = BasePage(support_browser, link)
    page.open()
    time.sleep(2)

@pytest.fixture()
def open_location_home_page(support_browser):
    link = BasePageLocators.HOME_PAGE_LOCATION
    page = BasePage(support_browser, link)
    page.open()
    time.sleep(2)



# Supports console options (pytest):
# --browser_name= (firefox or chrome)
# --language=ru (default='en')
# --headless=true (default='None')

# pytest -v -s  --tb=line --reruns 1  --browser_name=chrome --language=ru --headless=true   test_main_page.py
