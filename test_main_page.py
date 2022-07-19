import time
import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.sign_in_page import SignIn

class TestLoginFromMainPage():

    # def test_guest_should_see_login_page(self, support_browser, ):
    #     link = "https://www.linkedin.com/"
    #     page = BasePage(support_browser, link)
    #     page.open()
    #     time.sleep(5)

        # перемещаемся в новый класс .pages.login_page
        # login_page = LoginPage(support_browser, support_browser.current_url)
        # login_page.is_element_link_cookie_policy_1()
        # login_page.is_element_link_cookie_policy_2()
        # login_page.test_button_accept_cookie_end_reject()
        # login_page.is_element_hex_checking_the_text_color_of_a_button()
        # login_page.is_element_hex_checking_the_background_color_of_a_button()
        # login_page.user_authorization()

    def test_guest_should_se_sign_in_page(self, support_browser):
        link = "https://www.linkedin.com/"
        page = BasePage(support_browser, link)
        page.open()
        time.sleep(3)

        # перемещаемся в новый класс .pages.sign_in_page
        sign_in_page = SignIn(support_browser, support_browser.current_url)
        sign_in_page.click_button_sign_in()
        time.sleep(500)





















