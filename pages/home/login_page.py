from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_button = '[data-test-id="button-to-login"]'
    _email_field = "username"
    _password_field = "password"
    _login_submitt_button = "[data-test-id='button-to-submit-login-form']"
    _dashboard_navbar = ".navbar.navbar-fixed-top.navbar-inverse"


    def click_login_button(self):
        self.elementClick(self._login_button, "css")
    def insert_username(self, email):
        self.elementClick(self._email_field, "name")
        if self.getElement(self._email_field, "name").get_attribute("value"):
            self.getElement(self._email_field, "name").clear()
        self.sendKeys(email, self._email_field, 'name', )
    def inser_password(self, password):
        self.elementClick(self._password_field, "name")
        self.sendKeys(password, self._password_field, "name")
    def submit_login_button(self):
        self.elementClick(self._login_submitt_button, "css")


    def login(self, username, password):
        self.click_login_button()
        self.insert_username(username)
        self.inser_password(password)
        time.sleep(1)
        self.submit_login_button()


