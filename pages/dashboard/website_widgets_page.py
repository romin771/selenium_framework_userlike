from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By

class Website_widget(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _channels_button = "//*[text()='Channels']"
    _website_widgets = "//a[text()='Website widgets']"
    _close_new_widget_popup = "close"
    _delete_button = "btn-danger"

    def get_channels_button(self):
        element = self.getElement("//*[text()='Channels']", locatorType="xpath")
        if element is not None:
            element.click()
        else:
            self.log.error("Element not found, could not click on it.")


    def goto_website_widget(self):
        self.elementClick(self._website_widgets, locatorType="xpath")

    def website_widget_appeared_successfully(self):
        add_widget_button_presense = self.isElementPresent("//div[@class='modal-header']/h2[contains(text(), 'Your new Widget')]",
                                        locatorType="xpath")
        assert add_widget_button_presense == True

    def close_widget(self):
        self.elementClick(self._close_new_widget_popup, locatorType="classname")

    def delete_last_created_widget(self):
        widget_row = self.driver.find_element(By.TAG_NAME, "tbody")
        widget_rows = widget_row.find_elements(By.TAG_NAME, "tr")

        if len(widget_rows) >= 2:
            delete_icon = self.driver.find_elements(By.CLASS_NAME, "btn-mini.widgetDelete")[0]
            delete_icon.click()
            self.elementClick("btn-danger", locatorType="classname")
        elif len(widget_rows) == 1:
            print("The default widget cannot be deleted.")
        else:
            # Handle other cases if needed
            print("Unexpected number of child <tr> elements.")















