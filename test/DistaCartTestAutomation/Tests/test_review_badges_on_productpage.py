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


# Automation script for review badges in product page
class TestReviewBadgesOnProductPage:

    def test_review_badges_on_productpage(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url(
            "https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
        helper.wait()

        review_badge_section = browser.find_element_by_xpath(locators.judgme_badge_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", review_badge_section)
        assert helper.is_element_present_by_xpath(locators.product_detail_star_badges_xpath)
        assert helper.is_element_present_by_xpath(locators.product_detail_stars_xpath)
        assert helper.is_element_present_by_xpath("//span[@class='jdgm-qa-badge__icon']")










