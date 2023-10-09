"""  Here we wrap all the methods provided  by selenium webdriver into
our custome method to use in our framework """


from selenium.webdriver.common.by import By
from traceback import print_stack

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

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
            print("// The enteres locator type " + locatorType + " is not correct/supported")
        return False


    def getElement(self,locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print(f"// element found with locator :: " + locator + "and locator type" + locatorType)
        except:
            print(f"// element not found with locator " + locator + "and locator type" + locatorType)
        return element

    def elementClick(self,locator, locatorType ="id" ):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print(" // clicked on element with locator ::  " + locator + " and locatorType ::  " + locatorType)
        except:
            print(" // cannot click on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    # take care of the name, it should not be send_keys otherwise it will conflict with selenium predefice function
    def sendKeys(self,data , locator, locatorType ="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(" // send thisdata " + data+ "on this ::  " + locator + " which has this locatorType ::  " + locatorType)
        except:
            print(" // it is not possible to send this data " + data+ " to this locator : " + locator + " which has this locatorType: " + locatorType)
            print_stack()


    def isElementPresent(self, locator , locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("element found")
                return True
            else:
                print("element not found ")
                return False
        except:
            print("element not found ")
            return False

    def isElementDisplayed(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element.is_displayed():
                print("Element is displayed")
                return True
            else:
                print("Element is not displayed")
                return False
        except:
            print("Element not found")
            return False




