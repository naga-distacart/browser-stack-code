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


# Automation script for displaying product recommendation sections on product page
class TestProductRecommendationOnProductPage:

    def test_product_recommendations_product_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url(
            "https://www.distacart.com/products/patanjali-divya-coronil-kit-coronil-tablet-anu-taila-swasari-vati")
        helper.wait()
        helper.navigate_to_url(
            "https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
        time.sleep(7)
        for i in range(0, 4):
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(4)
        similar_products = browser.find_element_by_xpath(locators.similar_products_title)
        browser.execute_script("arguments[0].scrollIntoView();", similar_products)
        element = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, locators.similar_products_title))
        )
        product_recommendations_section = browser.find_element_by_xpath(locators.frequently_bought_together)
        browser.execute_script("arguments[0].scrollIntoView();", product_recommendations_section)
        assert helper.is_element_present_by_xpath(locators.frequently_bought_together)
        #assert helper.is_element_present_by_xpath(locators.similar_products_title)
        assert helper.is_element_present_by_xpath(locators.similar_products_title)
        #assert helper.is_element_present_by_xpath(locators.recently_viewed_products_title)








