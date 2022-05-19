from selenium.webdriver.common.by import By
from base_element import BaseElement as BE
import base_page
from locator import Locator


class PageElements(base_page.BasePage):
    @property
    def installation_button(self):
        return BE(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value="ul.current > li:nth-child(1)"))

    @property
    def email_input_field(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//input[@name='Email']"))