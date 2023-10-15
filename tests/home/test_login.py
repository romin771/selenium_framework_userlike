import unittest
from pages.home.login_page import LoginPage
import pytest
from utilities.teststatus import TestStatus
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True) #class level setup
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")
        success_login = self.lp.verify_successful_login()
        self.ts.mark(success_login, "login was not successfull")
        title_verified = self.lp.verify_login_title()
        self.ts.markFinal("test_valid_login", title_verified, "logig wasn not successful")


    #negative test case
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("romin.parvardeh@gmail.com", "RominRo4")
        sussess_login = self.lp.verify_fail_login()
        assert sussess_login == True





