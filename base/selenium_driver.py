"""  Here we wrap all the methods provided  by selenium webdriver into
our custome method to use in our framework """
import logging

from selenium.webdriver.common.by import By
from traceback import print_stack
import utilities.custom_logger as cl
import logging

class SeleniumDriver():
    # make sure its not under __init__ method otherwise its not showing logs are comming from seleniumDriver
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title
    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("//The entered locator type is" + locatorType + " is not correct/supported")
        return False


    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f"//element found with locator :: " + locator + "  and locator type" + locatorType)
        except:
            self.log.info(f"// element not found with locator " + locator + "  and locator type" + locatorType)
        return element

    def elementClick(self, locator, locatorType ="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(" // clicked on element with locator ::  " + locator + "  and locatorType ::  " + locatorType)
        except:
            self.log.info(" // cannot click on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    # take care of the name, it should not be send_keys otherwise it will conflict with selenium predefice function
    def sendKeys(self,data , locator, locatorType ="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(" // send this data " + data+ "  on this locator ::  " + locator + " which has this locatorType ::  " + locatorType)
        except:
            self.log.info(" // it is not possible to send this data " + data+ " to this locator : " + locator + " which has this locatorType: " + locatorType)
            print_stack()


    def isElementPresent(self, locator , locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("element found")
                return True
            else:
                self.log.info("element not found ")
                return False
        except:
            self.log.info("element not found ")
            return False

    def isElementDisplayed(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element.is_displayed():
                self.log.info("Element is displayed")
                return True
            else:
                self.log.info("Element is not displayed")
                return False
        except:
            self.log.info("Element not found")
            return False




