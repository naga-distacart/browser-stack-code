import re

from selenium import webdriver
from selenium.webdriver.support.select import Select
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

class TestSubscriptionProduct:
    def test_subscription_us_customers(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/collections/isha-life/products/isha-life-neem-and-turmeric-capsules")
        helper.wait()
        subscription_section = browser.find_element_by_xpath(locators.subscription_purchase_option)
        browser.execute_script("arguments[0].scrollIntoView();", subscription_section)
        helper.wait()
        assert helper.is_element_present_by_xpath(locators.onetime_purchase_text)
        #assert helper.is_element_present_by_xpath(locators.subscribe_and_save_radio_button)
        assert helper.is_element_present_by_xpath(locators.subscribe_and_save_text)

        #radio_button = browser.find_element_by_xpath(locators.subscribe_and_save_radio_button)
        #radio_button.click()
        # WebDriverWait(browser, 60).until(
        #     EC.presence_of_element_located((By.XPATH, locators.subscribe_and_save_selected_text))
        # )
        # assert helper.is_element_present_by_xpath(locators.deliver_frequency_text)

