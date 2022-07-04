import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

# Пример использования:
#
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "https://www.linkedin.com/"
        page = MainPage(browser, link)
        page.open()
        # перемещаемся в новый класс .pages.login_page
        time.sleep(0)
        login_page = LoginPage(browser, browser.current_url)
        login_page.test_button_accept_cookie_end_reject()



#
#     # Комбинирование обращений к разным страницам.
#     def test_guest_can_go_to_login_page(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/"
#         page = MainPage(browser, link)   # Открываем Page Object - 'MainPage', передаем в конструктор экземпляр драйвера и url адрес
#         page.open()                      # открываем link
#         page.go_to_login_page()          # переходим на страницу логина
#         login_page = LoginPage(browser, browser.current_url) # Открываем Page Object - 'LoginPage', передаем в конструктор экземпляр драйвера и url адрес
#         login_page.should_be_login_page() # Выполняем ряд тестов не уходя со страницы















