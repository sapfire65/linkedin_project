import time
import pytest
from mimesis import Person
from mimesis.locales import Locale
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0


class SignIn(BasePage):

# Тестирование полей ввода login / pass
    def click_button_sign_in(self):
        global count
        self.is_header('Проверка клика по кнопке SignIn')
        button = self.browser.find_element(By.XPATH, '//a[@data-tracking-control-name="guest_homepage-basic_nav-header-join"]')
        button.click()
        url_sign_in_page = self.browser.current_url

        print(f'\n{count + 1}) Проверка URL страницы SignIn после клика')
        count += 1
        assert 'https://www.linkedin.com/signup/cold-join?trk=guest_homepage-basic_nav-header-join' == url_sign_in_page, 'Это не страница авторизации'


    def input_email(self):
        pass