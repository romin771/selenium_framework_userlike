import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import pytest
from pages.home.login_page import LoginPage
from base.selenium_driver import SeleniumDriver
from pages.dashboard.website_widgets_page import Website_widget


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class widget_create(unittest.TestCase):

    @pytest.fixture(autouse=True)  # class level setup
    def classSetup(self, oneTimeSetUp):
        self.driver = self.driver
        self.login = LoginPage(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.ww = Website_widget(self.driver)


    @pytest.mark.run(order=1)
    def test_creating_web_widget(self):
        self.login.login("romin5954@gmail.com", "RominRomin!234!234")
        time.sleep(2)
        self.driver.find_element(By.XPATH,  "//*[text()='Channels']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Website widgets']").click()
        self.sd.isElementPresent("//div[@class='modal-header']/h2[contains(text(), 'Your new Widget')]",locatorType="xpath") == True
        self.sd.elementClick("widgetWizard", locatorType="id")
        self.sd.elementClick("btn-success", locatorType="classname")
        self.ww.close_widget()
        time.sleep(2)

    @pytest.mark.run(order=2)
    def test_deleting_web_widget(self):
        time.sleep(2)
        self.ww.delete_last_created_widget()
        self.driver.quit()







