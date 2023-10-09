from selenium.webdriver.common.by import By
import time


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        # locators
    _login_button = '[data-test-id="button-to-login"]'
    _email_field = "username"
    _password_field = "password"
    _login_submitt_button = "[data-test-id='button-to-submit-login-form']"
    _dashboard_navbar = ".navbar.navbar-fixed-top.navbar-inverse"



    # expose locator to web elements -methods to expose locators as elemens
    def get_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_button)
    def get_username_field(self):
        return self.driver.find_element(By.NAME, self._email_field)
    def get_password_field(self):
        return self.driver.find_element(By.NAME, self._password_field)
    def get_login_submitt_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_submitt_button)


    # Perform Action on Elements
    def click_login_button(self):
        self.get_login_button().click()
    def insert_username(self, email):
        self.get_username_field().click()
        if self.get_username_field().get_attribute("value"):
            self.get_username_field().clear()
        self.get_username_field().send_keys(email)
    def inser_password(self, password):
        self.get_password_field().click()
        self.get_password_field().send_keys(password)
    def submit_login_button(self):
        self.get_login_submitt_button().click()


    def login(self, username, password):
        self.click_login_button()
        self.insert_username(username)
        self.inser_password(password)
        time.sleep(1)
        self.submit_login_button()


