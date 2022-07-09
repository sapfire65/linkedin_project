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






class LoginPage(BasePage):
    def test_button_accept_cookie_end_reject(self):
        global count

        self.is_header('Проверка кнопок ACCEPT / REJECT ')
        print(f'\n{count + 1}) Check button accept / проверяем наличие кнопки согласия')
        count += 1
        assert self.is_element_present(*LoginPageLocators.BUTTON_ACCEPT), \
            "button << accept >> is not presented"
        print(f'{count + 1}) Check clickable button accept / проверяем кликабельность кнопки согласия')
        count += 1
        assert self.is_element_present(*LoginPageLocators.BUTTON_ACCEPT), \
            "button << accept >> is not clickable"

        print(f'{count + 1}) Check button reject / проверяем наличие кнопки отмены')
        count += 1
        assert self.is_element_present(*LoginPageLocators.BUTTON_REJECT), \
            "button << reject >> is not presented"
        print(f'{count + 1}) Check clickable button reject / проверяем кликабельность кнопки отмены')
        count += 1
        assert self.is_element_present(*LoginPageLocators.BUTTON_REJECT), \
            "button << reject >> is not clickable"


    # Проверка цвета тектса кнопок ACCEPT / REJECT
    def is_element_hex_checking_the_text_color_of_a_button(self):
        global count
        self.is_header('ЦВЕТ ТЕКСТА')
        print(f'\n{count + 1}) Checking the color of the text when the button is not pressed / Проверяем цвет текста, не нажатой кнопки')
        count += 1
        assert self.is_element_hex_color(*LoginPageLocators.BUTTON_COOKIE_TEXT_COLOR), \
            'Цвет текста кнопки, отличается!'


    def is_element_hex_checking_the_background_color_of_a_button(self):
        global count
        self.is_header('ЦВЕТ ФОНА')
        print(f'\n{count + 1}) Checking the background color of the button / Проверяем фоновый цвет, не нажатой кнопки')
        count += 1
        rgb = self.is_element_hex_color(*LoginPageLocators.BUTTON_COOKIE_BACKGROUND_COLOR)
        assert rgb == True, 'Цвет фона кнопки, отличается!'

        print(f'{count + 1}) Clik button accept / клик по кнопке согласия')
        count += 1
        self.browser.find_element(*LoginPageLocators.BUTTON_ACCEPT).click()

        print(f'{count + 1}) Сheck that cookie checking is gone / проверить что сообщение про куки исчезло')
        count += 1
        assert self.is_disappeared(*LoginPageLocators.COOKIE_POLICY), \
            "Cookie message has not disappeared"


    def is_element_link_cookie_policy(self):
        global count
        self.is_header('РАБОТА С КУКИ')
        print(f'\n{count + 1}) Check that the link to the cookie policy exists / '
              'Проверяем что ссылка на политику использования файлов cookie, существует.')
        count += 1
        assert self.is_element_present(*LoginPageLocators.LINC_COOKIE_POLICY)

        print(f'{count + 1}) Check that the attribute reference is correct. / Проверяем что ссылка атрибута верная.')
        count += 1
        assert self.is_links_are_the_same(*LoginPageLocators.LINC_COOKIE_POLICY,
        LoginPageLocators.EXPECTED_RESULT_LINC_COOKIE_POLICY), \
            'links are different / ссылки отличаются'

        print(f'{count + 1}) Проверяем что ссылка в атрибуте и фактическая ссылка после перехода, одинаковые.')
        count += 1
        current_url = self.get_current_url() # записываем текущий URL
        link = self.browser.find_element(*LoginPageLocators.LINC_COOKIE_POLICY) # Находим элемент
        attribute_value = link.get_attribute('href') # Записываем значение атрибута 'href'
        print(f'Attribute value / значение атрибута: {attribute_value}')
        time.sleep(2)
        link.click()
        link_location = self.browser.current_url
        print(f'Actual result / фактический результат: {link_location}')
        time.sleep(2)
        p = BasePage(self.browser, current_url)
        p.open()













    def user_authorization(self):
        global count
        global login1
        global password1

        self.is_header('Авторизация')
        print(f'\n{count + 1}) Вводим логин / пароль')
        count += 1
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(login1)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password1)
        self.browser.find_element(By.XPATH, '//button[@class="sign-in-form__submit-button"]').click()
        print(f'{count + 1}) Checking for Successful Authorization / Проверка успешной авторизации')
        count += 1
        result = self.explicit_element_wait(*LoginPageLocators.AUTHORIZATION_CHECK)
        assert result == True, \
            "user authorization failed / Юзер не авторизован"




















#     def should_be_login_page(self):
#         self.should_be_login_url()
#         self.should_be_login_form()
#         self.should_be_password_form()
#         self.should_be_register_form()
#
#
    # def should_be_login_url(self):
    #     # находим и кликаем по ссылке логина
    #     self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
    #     time.sleep(5)
    #     current_url_login = self.browser.current_url
    #     print(current_url_login)
    #     assert "/login" in current_url_login, "login is absent in current url"
#
#
#     def should_be_login_form(self):
#         # реализуйте проверку, что есть форма логина
#         self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
#         input_login = self.browser.find_element(*LoginPageLocators.INPUT_LOGIN)
#         input_login_correct = input_login.get_attribute('name')
#         print(f'attribut | name = {input_login_correct}')
#         assert  'login-username' in input_login_correct, 'input login not found'
#
#     def should_be_password_form(self):
#         # Проверка, что есть поля ввода, на странице регистрации
#         self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
#         input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
#         input_password_correct = input_password.get_attribute('name')
#         print(f'attribut | name = {input_password_correct}')
#         assert 'login-password' in input_password_correct, 'input password not found'
#
#     def should_be_register_form(self):
#         # Проверка наличия формы регистрации
#         self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
#         reg_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
#         register_form = reg_form.get_attribute('id')
#         print(f'attribut | id = {register_form}')
#         assert 'register_form' in register_form, 'register form not found'
#
#     # Регистрация: - генерация нового пользователя с паролем
#     def register_new_user(self):
#         user_email_generator = Person(locale=Locale.EN).email()
#         user_password = Person(locale=Locale.EN).password(length=20)
#         registration_email = self.browser.find_element(*LoginPageLocators.EMAIL)
#         registration_email.send_keys(user_email_generator)
#         # first input
#         registration_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
#         registration_password1.send_keys(user_password)
#         # last input
#         registration_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
#         registration_password2.send_keys(user_password)
#         # button register
#         self.browser.find_element(*LoginPageLocators.CONFIRMATION_BUTTON_REGISTRATION).click()
#         time.sleep(1)



