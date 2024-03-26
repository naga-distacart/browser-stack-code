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

#Automation script for Req 132:Shipping Text box on product page
# from Tests.conftest import browser


class TestShippingBox:

    def test_shipping_box_text_US(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        element = WebDriverWait(browser, 80).until(
           EC.presence_of_element_located((By.XPATH, locators.shipping_box_title)))
        shipping_box = browser.find_element_by_xpath(locators.shipping_box_title)
        browser.execute_script("arguments[0].scrollIntoView();", shipping_box)
        helper.wait()
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
        l = browser.find_elements_by_xpath(locators.shipping_rates_table_xpath)
        print (len(l))
        for i in l:
            print(i.text)
        assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab1)
        assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab2)
        assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab3)
        assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab4)
        # assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab5)
        # assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab6)
        # assert helper.is_element_present_by_xpath(locators.shipping_rate_US_slab7)

        # #Assurance Icons
        # assert helper.is_element_present_by_xpath(locators.product_authentic_xpath)
        # assert helper.is_element_present_by_xpath(locators.product_secure_xpath)
        # assert helper.is_element_present_by_xpath(locators.product_guaranteed_xpath)
        # assert helper.is_element_present_by_xpath(locators.product_easy_returns_xpath)

    # def test_shipping_box_text_GB(self, browser):
    #     homepage = HomePage(browser)
    #     helper = Helper(browser)
    #     helper.navigate_to_url("https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
    #     browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
    #     #element = WebDriverWait(browser, 45).until(
    #      #   EC.presence_of_element_located((By.XPATH, locators.shipping_box_title)))
    #    # shipping_box = browser.find_element_by_xpath(locators.shipping_box_title)
    #     #browser.execute_script("arguments[0].scrollIntoView();", shipping_box)
    #     #helper.wait()
    #     l = browser.find_elements_by_xpath(locators.shipping_rates_table_xpath)
    #     print (len(l))
    #     for i in l:
    #         print(i.text)
