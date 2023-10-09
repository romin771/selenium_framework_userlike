from selenium.webdriver.common.by import By
import time


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        login_button = self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='button-to-login']")
        login_button.click()

        email_field = self.driver.find_element(By.NAME, "username")
        email_field.click()
        if email_field.get_attribute("value"):
            # Clear the email field
            email_field.clear()
        email_field.send_keys(username)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.click()
        password_field.send_keys(password)

        time.sleep(1)
        login_submit_button = self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='button-to-submit-login-form']")
        login_submit_button.click()
