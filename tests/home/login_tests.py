from selenium import webdriver
import unittest
from pages.home.login_page import LoginPage
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True) #class level setup
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")
        success_login = self.lp.verify_successful_login()
        assert success_login == True
        title_verified = self.lp.verify_title()
        assert title_verified == True


    #negative test case
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("romin.parvardeh@gmail.com", "RominRo4")
        sussess_login = self.lp.verify_fail_login()
        assert sussess_login == True





