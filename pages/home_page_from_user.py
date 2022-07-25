import time
import pytest
from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageFromUser(BasePage):
    # Явное ожидание элемента после авторизации. Свернуть чат.
    def hide_chat(self):
        button_chat = WebDriverWait(self, 120).until(EC.element_to_be_clickable(
                (By.XPATH, '(//div[@class="msg-overlay-bubble-header__controls display-flex"]/button)[2]')))
        button_chat.click()

