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

class TestFolderStructureCartPrice:
    @pytest.mark.sanityH
    def test_add_to_cart(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/en-sg")
        helper.wait()
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.XPATH, locators.most_popular_section_xpath))
             )
        limespot_collection = browser.find_element_by_xpath(locators.most_popular_section_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", limespot_collection)
        WebDriverWait(browser,180).until(EC.element_to_be_clickable((By.XPATH,locators.first_popular_product_price)))
        # product_name = browser.find_element_by_xpath(locators.first_popular_product_title_xpath ).text
        product_price = browser.find_element_by_xpath(locators.first_popular_product_price).text
        helper.wait()
        browser.find_element_by_xpath(locators.first_popular_product_add_to_cart).click()
        variant=browser.find_elements_by_xpath(locators.first_popular_product_add_to_cart_popup_xpath)
        if(len(variant)>0):
            browser.find_element_by_xpath(locators.first_popular_product_add_to_cart_popup_xpath).click()
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.minicart_slider))
        )
        product_price_slider = browser.find_element_by_xpath(locators.minicart_price).text
        assert product_price == product_price_slider
