from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from DistaCartTestAutomation.Locators.locators import Locators


class ProductPage():

    def __init__(self, driver):
        locators = Locators()
        self.driver = driver
        self.product_title_xpath = locators.product_title_xpath
        self.product_vendor_xpath = locators.product_vendor_xpath

    def product_title(self):
        self.driver.implicitly_wait(60)
        self.driver.switch_to.default_content()
        return self.driver.find_element_by_xpath(self.product_title_xpath).text

    def product_vendor(self):
        return self.driver.find_element_by_xpath(self.product_vendor_xpath).text

