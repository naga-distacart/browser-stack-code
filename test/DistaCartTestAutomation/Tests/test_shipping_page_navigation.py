from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
class TestShippingPageNavigation:

    def test_navigation_shipping_page_from_homepage(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.move_to_element(browser.find_element_by_xpath(locators.homepage_shipping_link))
        helper.click_on_element(browser.find_element_by_xpath(locators.homepage_shipping_link))

        helper.wait()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.shipping_page_title)))
        assert helper.is_element_present_by_xpath(locators.shipping_page_title)
        assert helper.is_element_present_by_xpath(locators.shipping_page_header_text)







