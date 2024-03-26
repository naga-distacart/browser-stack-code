# -*- coding: utf-8 -*-
import json

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


class TestSellerProfile:

    def test_seller_profile(self, browser):
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/collections/anarkali-dresses/products/aniyah-rayon-block-printed-anarkali-blue-kurta")
        helper.wait()
        helper.wait()
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            try:
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            except:
                helper.wait()
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            if (len(No_thanks) > 0):
                # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        element = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.product_vendor_xpath))
        )
        browser.find_element_by_xpath(locators.product_vendor_xpath).click()
        helper.wait()
        print("INFO: Verify that seller profile name is displayed")
        assert "True" == str(helper.is_element_present_by_xpath(locators.seller_profile_xpath))
        seller_profile = browser.find_element_by_xpath(locators.seller_profile_xpath).text
        assert seller_profile == "Aniyah"

    def test_fulfiller_profile(self, browser):
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/collections/ayurvedic-products-online/products/patanjali-giloy-ghan-vati-40-gm")
        helper.wait()
        browser.find_element_by_xpath(locators.product_fulfilled_xpath).click()
        helper.wait()
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            try:
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            except:
                helper.wait()
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            if (len(No_thanks) > 0):
                # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        print("INFO: Verify that fulfiller profile name is displayed")
        assert "True" == str(helper.is_element_present_by_xpath("//span[text()='Genie India ']"))
        fulfiller_profile = browser.find_element_by_xpath("//span[text()='Genie India ']").text
        assert fulfiller_profile == "Genie India"

    def test_shipping_info_link(self, browser):
        helper = Helper(browser)
        helper.wait()
        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, locators.free_shipping_link_xpath))
        )
        print("INFO: Verify that free shipping link is redirected to free shipping page")
        #browser.find_element_by_xpath(locators.free_shipping_link_xpath).click()
        helper.move_to_element(browser.find_element_by_xpath(locators.free_shipping_link_xpath))
        helper.click_on_element(browser.find_element_by_xpath(locators.free_shipping_link_xpath))
        element = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Express Shipping To: ']"))
        )
        assert "True" == str(helper.is_element_present_by_xpath("//p[text()='Express Shipping To: ']"))

    def test_returns_policy_link(self, browser):
        helper = Helper(browser)
        helper.wait_small()
        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, locators.returns_policy_link_xpath))
        )
        print("INFO: Verify that returns policy link is redirected to returns policy page")
        #browser.find_element_by_xpath(locators.returns_policy_link_xpath).click()
        helper.move_to_element(browser.find_element_by_xpath(locators.returns_policy_link_xpath))
        helper.click_on_element(browser.find_element_by_xpath(locators.returns_policy_link_xpath))
        element = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//p/span/strong[contains(text(),'Return Policy')]"))
        )
        assert "True" == str(helper.is_element_present_by_xpath("//p/span/strong[contains(text(),'Return Policy')]"))
