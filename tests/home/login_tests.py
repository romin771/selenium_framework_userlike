from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
from selenium.common.exceptions import NoSuchElementException
from pages.home.login_page import LoginPage




class LoginTests():
    def test_valid_login(self):
        base_url = "https://www.userlike.com/en/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        #create object of LoginPage
        lp = LoginPage(driver)
        lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")



        try:
            # Try to find the element
            dashboard_navbar = driver.find_element(By.CSS_SELECTOR, ".navbar.navbar-fixed-top.navbar-inverse")
            # Check if the element is displayed
            if dashboard_navbar.is_displayed():
                print("login is successfull")
            else:
                print("login is not successful")
        except NoSuchElementException:
            print("Element not found and login is not successful")





start = LoginTests()
start.test_valid_login()