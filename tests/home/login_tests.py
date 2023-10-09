from selenium import webdriver
from selenium.webdriver.common.by import  By
import unittest
from selenium.common.exceptions import NoSuchElementException
from pages.home.login_page import LoginPage




class LoginTests(unittest.TestCase ):
    def test_valid_login(self):
        base_url = "https://www.userlike.com/en/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        #create object of LoginPage
        lp = LoginPage(driver)
        lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")
        assert lp.isElementDisplayed(".navbar.navbar-fixed-top.navbar-inverse", "css") == True



