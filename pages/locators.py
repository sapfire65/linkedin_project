from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    BUTTON_ACCEPT = (By.XPATH, '//button[@action-type="ACCEPT"]')
    BUTTON_REJECT = (By.XPATH, '//button[@action-type="DENY"]')
    COOKIE_POLICY = (By.XPATH, '//section[@class="artdeco-global-alert__body"]')
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    INPUT_LOGIN = (By.XPATH, '//input[@autocomplete="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@autocomplete="current-password"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    AUTHORIZATION_CHECK = (By.XPATH, '//img[@class="global-nav__me-photo ember-view"]')




