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


# Automation script for shipping page navigation from link on home page
class TestShippingDaysProductPage:

    def test_shipping_time_in_product_page(self, browser):
        #comments
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url(
            "https://www.distacart.com/collections/dista-pick/products/mamaearth-onion-shampoo-for-hair-fall-control")
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.product_patanjali_title)))
        assert helper.is_element_present_by_xpath(locators.ready_to_ship_element_xpath)









