from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    STATUS_BROWSER_TEXT = (By.XPATH, '//span[@class="badge bg-green"]')
    LINC_SERVICE_STATUS_BROWSER = 'https://sitedozor.ru/what-is-my-browser'
    HOME_PAGE_LOCATION = 'https://www.linkedin.com/'

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    BUTTON_ACCEPT = (By.XPATH, '//button[@action-type="ACCEPT"]')
    BUTTON_REJECT = (By.XPATH, '//button[@action-type="DENY"]')
    COOKIE_POLICY = (By.XPATH, '//section[@class="artdeco-global-alert__body"]')
    INPUT_LOGIN = (By.XPATH, '//input[@autocomplete="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@autocomplete="current-password"]')
    AUTHORIZATION_CHECK = (By.XPATH, '//img[@class="global-nav__me-photo ember-view"]')
    BUTTON_COOKIE_BACKGROUND_COLOR = (By.CLASS_NAME, "artdeco-button", "background-color", '#ffffff')
    BUTTON_COOKIE_TEXT_COLOR = (By.XPATH, '//button[@action-type="DENY"]', "color", '#5c6f7c')
    LINC_COOKIE_POLICY = (By.XPATH, '(//a[@data-tracking-control-name="global-alerts-alert-link-cta"])[1]')
    EXPECTED_RESULT_LINC_COOKIE_POLICY = 'https://www.linkedin.com/legal/cookie-policy'
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')

class SignInLocators():
    SIGN_IN_BUTTON = (By.XPATH, '//a[@data-tracking-control-name="guest_homepage-basic_nav-header-join"]')
    LINC_LOCATION_SIGN_IN_PAGE = 'https://www.linkedin.com/signup/cold-join?trk=guest_homepage-basic_nav-header-join'
    INPUT_EMAIL = (By.XPATH, '//input[@id="email-address"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="join-form__form-body-submit-button"]')
    FEEDBACK_MESSAGE =  (By.XPATH, '(//p[@class="artdeco-inline-feedback__message"])')

class HomePageLocators():
    REACTION = (By.XPATH, '//img[@data-test-reactions-icon-type="LIKE"]')
    HIDE_CHAT_BUTTON = (By.XPATH, '(//div[@class="msg-overlay-bubble-header__controls display-flex"]/button)[2]')
    WINDOW_LIKE_OK = (By.XPATH, '//h2[@class="t-20 t-black--light t-normal"]')
    COUNT_USSER_LIKE = (By.XPATH, '(//span[@class="mr1"])[2]')
    STATUS_USER = (By.XPATH, '//div[@class="artdeco-entity-lockup__caption ember-view"]')
    COUNT_LEVEL = (By.XPATH, '//span[@class="artdeco-entity-lockup__degree"]')
    ELEM_PLUS_BUTTON_FROM_USER = (By.XPATH, '//div[@class="pvs-profile-actions "]//button[@data-control-name="topcard_primary_follow"]//li-icon[@type="plus-icon"]')
    ELEM_PLUS_BUTTON_FROM_USER_2 = (By.XPATH, '//div[@class="pvs-profile-actions "]//button[@type="button"]//li-icon[@type="check"]')

    ELEM_BUTTON_SETUP_CONTACT = (By.XPATH, '(//button[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"])[2]')
    SEND_REGUEST_BUTTON = (By.XPATH, '(//span[@class="artdeco-button__text"])[3]')
    LATER_RESULT = (By.XPATH, '(//button[@class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"])[1]')
    BUTTON_EXIT = (By.XPATH, '//button[@class="artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]')
    BUTON_MORE_POSTS = (By.XPATH, '//div[@class="display-flex p5"]//button[@class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"]')
    USER_REACTIONS = (By.XPATH, '//span[@class="social-details-social-counts__social-proof-fallback-number"]')






