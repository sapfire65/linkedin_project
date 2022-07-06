import math
from selenium import webdriver
from .locators import BasePageLocators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url


    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.get(self.url)


    # Если элемент найден, возвращаем True,
    # иначе - перехватываем ошибку 'NoSuchElementException'
    # и присваиваем False
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

        # Если элемент кликабельный, возвращаем True,
        # иначе - перехватываем ошибку 'NoSuchElementException'
        # и присваиваем False
    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self, 10).until(EC.element_to_be_clickable((how, what)))
        except (NoSuchElementException):
            return False
        return True

        # Метод ПРОВЕРКИ что какой-то элемент исчезает.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    # Кликаем по ссылке логин / регистрация
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    # Проверка того, что пользователь залогинен.
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    # Если элемент кликабельный, возвращаем True,
        # иначе - перехватываем ошибку 'NoSuchElementException'
        # и присваиваем False
    def is_element_hex_color(self, how, what, css_property_name, expected_result):
        try:
            import ast
            color_hex = self.browser.find_element(how, what).value_of_css_property(css_property_name)
            r, g, b = ast.literal_eval(color_hex.strip("rgb"))
            print(color_hex)
            hex_value = '#%02x%02x%02x' % (r, g, b)
            print(f'HEX format: {hex_value}\n')
            if hex_value == expected_result:
                return True
            return False
        except (NoSuchElementException):
            return False




