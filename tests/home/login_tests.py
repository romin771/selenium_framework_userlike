from selenium import webdriver
import unittest
from pages.home.login_page import LoginPage
import pytest




class LoginTests(unittest.TestCase ):

    base_url = "https://www.userlike.com/en/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get(base_url)
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")
        sussess_login = self.lp.verify_successful_login()
        assert sussess_login == True
        self.driver.quit()

    #negative test case
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.base_url)

        self.lp.login("romin.parvardeh@gmail.com", "RominRo4")
        sussess_login = self.lp.verify_fail_login()
        assert sussess_login == True




