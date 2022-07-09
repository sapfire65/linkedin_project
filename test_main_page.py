import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


class TestLoginFromMainPage():
    # Проверка страницы логина
    def test_guest_should_see_login_page(self, browser):
        link = "https://www.linkedin.com/"
        page = BasePage(browser, link)
        page.open()
        # перемещаемся в новый класс .pages.login_page
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_element_link_cookie_policy()
        login_page.test_button_accept_cookie_end_reject()
        login_page.is_element_hex_checking_the_text_color_of_a_button()
        login_page.is_element_hex_checking_the_background_color_of_a_button()




        login_page.user_authorization()
        time.sleep(0)



















