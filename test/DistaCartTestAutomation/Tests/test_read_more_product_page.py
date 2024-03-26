from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest

import random


# Automation script for read more link in product page
class TestReadMoreProductPage:

    def test_read_more_text_in_product_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url(
            "https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
        helper.wait()
        #assert "False" == str(helper.is_element_present_by_xpath(locators.read_more_text))
        read_more_section = browser.find_element_by_xpath("//h2[text()='Customer Reviews']")
        browser.execute_script("arguments[0].scrollIntoView();", read_more_section)
        assert not len(browser.find_elements_by_xpath(locators.read_more_text))









