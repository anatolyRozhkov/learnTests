from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    def __init__(self, driver, locator, wait_time=5):
        self.driver = driver
        self.locator = locator
        self.wait_time = wait_time

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def perform_click(self):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.click()
        return None

    def input_text(self, text):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator)
        )
        element.clear()
        element.send_keys(text)
        return None