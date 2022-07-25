import time
import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.sign_in_page import SignIn
from .pages.locators import SignInLocators

class TestLoginFromMainPage():
    def test_guest_should_see_login_page(self, support_browser, open_location_home_page):
        # перемещаемся в новый класс .pages.login_page
        login_page = LoginPage(support_browser, support_browser.current_url)

        login_page.is_element_link_cookie_policy_1()
        login_page.is_element_link_cookie_policy_2()
        login_page.test_button_accept_cookie_end_reject()
        login_page.is_element_hex_checking_the_text_color_of_a_button()
        login_page.is_element_hex_checking_the_background_color_of_a_button()
        login_page.user_authorization()




























