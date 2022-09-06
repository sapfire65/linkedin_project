import requests
import math
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from colorama import init
from  colorama  import  Fore ,  Back ,  Style
import time

login1 = 'blablaa@gmail.com'
password1 = 'password'


# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.delete_all_cookies() # Удоляем все куки
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
            WebDriverWait(self, 50).until(EC.element_to_be_clickable((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def explicit_element_wait(self, how, wat):
        try:
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((how, wat)))
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


    # ПОЛУЧАЮ НАЗВАНИЕ БРАУЗЕРА
    def status_browser(self):
        name_browser = self.browser.execute_script("return navigator.userAgent;")
        if 'Firefox' in name_browser:
            name_browser = 'firefox'
        elif 'Chrome' in name_browser:
            name_browser = 'chrome'
        return name_browser

    # def amoun_elem(self, el):
    #     amount_elements = len(self.browser.find_elements(el))

        # Старый вариант на стороннем серисе
        # linc = BasePageLocators.LINC_SERVICE_STATUS_BROWSER
        # self.browser.execute_script("window.open('about:blank', 'tab2');") # Открывает новую пустую вкладку
        # # new_window = self.browser.window_handles[1] # переключается на новую (вторую) вкладку
        # self.browser.switch_to.window('tab2')
        # self.browser.get(linc)
        # text = WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((BasePageLocators.STATUS_BROWSER_TEXT)))
        # text = text.text
        # self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
        # first_window = self.browser.window_handles[0] # переключается на первую вкладку
        # self.browser.switch_to.window(first_window)
        # text = str(text).lower()
        # if 'chrome' in text:
        #     status = 'chrome'
        #     # print(status)
        #     return status
        # elif 'firefox' in text:
        #     status = 'firefox'
        #     # print(status)
        #     return status


    # Если HEX цвета одинаковые то True, иначе False,
    # Также - перехватываем ошибку 'NoSuchElementException'
    # и присваиваем False
    def is_element_hex_color(self, how, what, css_property_name, expected_result):
        name_browser = self.status_browser()
        # name_browser = self.browser.execute_script("return navigator.userAgent;")
        if name_browser == 'chrome':
            try:
                import ast
                color_hex = self.browser.find_element(how, what).value_of_css_property(css_property_name)
                r, g, b, alpha = ast.literal_eval(color_hex.strip("rgba"))
                print(color_hex)
                hex_value = '#%02x%02x%02x' % (r, g, b)
                print(f'HEX format: {hex_value}\n')
                if hex_value == expected_result:
                    return True
                return False
            except (NoSuchElementException):
                return False

        elif name_browser == 'firefox':
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


    # Сравнение значений атрибутов
    def is_links_are_the_same(self, how, what, link_name):
        link_location = self.browser.find_element(how, what)
        found_link = link_location.get_attribute('href')
        print(f'Attribute value / Значение атрибута: {found_link}')
        print(f'Expected result / Ожидаемый результат: {link_name}')
        if found_link == link_name:
            return True
        else:
            return False

        # Получение текущего URL
    def get_current_url(self):
        return self.browser.current_url

    # Цвет - информационный заголовок в консоли
    def is_header(self, text):
        print()
        print()
        for i in range(10):
            print(Fore.YELLOW + '*', end='')
        print(f' {text} ',  end='')
        for j in range(10):
            print(Fore.YELLOW + '*', Style.RESET_ALL, sep='', end='')

        # Информационный заголовок в консоли для позитивных проверок
    def messege_positive_check(self, text):
            print()
            print()
            for i in range(10):
                print(Fore.LIGHTBLUE_EX+ '*', end='')
            print(f' {text} ', end='')
            for j in range(10):
                print(Fore.LIGHTBLUE_EX + '*', Style.RESET_ALL, sep='', end='')

    # Информационный заголовок в консоли для негативных проверок
    def messege_negative_check(self, text):
            print()
            print()
            for i in range(10):
                print(Fore.MAGENTA + '*', end='')
            print(f' {text} ', end='')
            for j in range(10):
                print(Fore.MAGENTA + '*', Style.RESET_ALL, sep='', end='')

    def user_authorization(self):
        global login1
        global password1

        self.is_header('Авторизация')
        print()
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(login1)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password1)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//button[@class="sign-in-form__submit-button"]').click()
        result = self.explicit_element_wait(*LoginPageLocators.AUTHORIZATION_CHECK)
        assert result == True, \
            "user authorization failed / Юзер не авторизован"


