from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
from selenium.common.exceptions import NoSuchElementException




class LoginTests():
    def test_valid_login(self):
        base_url = "https://www.userlike.com/en/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)


        login_button = driver.find_element(By.CSS_SELECTOR, "[data-test-id='button-to-login']")
        login_button.click()

        email_field = driver.find_element(By.NAME, "username")
        email_field.click()
        if email_field.get_attribute("value"):
            # Clear the email field
            email_field.clear()
        email_field.send_keys("romin.parvardeh@gmail.com")

        password_field = driver.find_element(By.NAME,"password")
        password_field.click()
        password_field.send_keys("RominRomin!234!2345")

        time.sleep(1)
        login_submit_button = driver.find_element(By.CSS_SELECTOR, "[data-test-id='button-to-submit-login-form']")
        login_submit_button.click()

        # dashboard_navbar = driver.find_element(By.CSS_SELECTOR, ".navbar.navbar-fixed-top.navbar-inverse")
        # if dashboard_navbar is not None:
        #     print("log in successfull")
        # else:
        #     print("log in Nooooot successful ")
        try:
            # Try to find the element
            # dashboard_navbar = driver.find_element(dashboard_navbar)
            dashboard_navbar = driver.find_element(By.CSS_SELECTOR, ".navbar.navbar-fixed-top.navbar-inverse")
            # Check if the element is displayed
            if dashboard_navbar.is_displayed():
                print("Element is visible")
            else:
                print("Element is not visible")

        except NoSuchElementException:
            print("Element not found")





start = LoginTests()
start.test_valid_login()