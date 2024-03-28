from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import pytest

from DistaCartTestAutomation.Helpers.helper import Helper
from DistaCartTestAutomation.Locators import locators
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage


class TestGeolocation():

    @pytest.mark.sanityH
    def test_geolocation(self, browser):
        search_product = "Patanjali Gulab Jamun"
        search_product_xpath = locators.product_xpath.format("Patanjali Gulab Jamun")
        homepage = HomePage(browser)
        homepage.search_product(search_product, search_product_xpath)

        productpage = ProductPage(browser)
        print("INFO: Verify search item {} is found with title {}".format(search_product, "Patanjali Gulab Jamun"))
        #assert productpage.product_title() == "Patanjali Gulab Jamun"
        availability_text = browser.find_element_by_xpath(locators.product_not_available_xpath).text
        print("INFO: Verify that Product not available for sale in your country message is displayed")
        assert availability_text == "This product is not available for sale in your country"

    @pytest.mark.sanityH
    def test_geolocation_product_page(self, browser):
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/products/patanjali-gulab-jamun")
        # element = WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Patanjali Gulab Jamun']")))
        availability_text = browser.find_element_by_xpath(locators.product_not_available_xpath).text
        print("INFO: Verify that Product not available for sale in your country message is displayed")
        assert availability_text == "This product is not available for sale in your country"


