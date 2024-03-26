# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
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


class TestShippingInfo:

    def test_general_order_shipping_info(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        search_product = "Patanjali Divya Lavangadi Vati"
        search_product_xpath = locators.product_xpath.format("Patanjali Divya Lavangadi Vati")
        print("INFO: Searching for product {}".format(search_product))
        homepage.search_product(search_product, search_product_xpath)
        element = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, locators.shipping_info_xpath))
        )
        shipping_info = browser.find_element_by_xpath(locators.shipping_info_xpath).text
        print("INFO: Shipping info displayed for {} is {}".format(search_product, shipping_info))
        assert shipping_info == 'Ready to dispatch in 3 - 5 business days'

    def test_online_order_shipping_info(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        search_product = "Dr. Reckeweg Nux Vomica Dilution"
        search_product_xpath = locators.product_xpath.format("Dr. Reckeweg Nux Vomica Dilution")
        print("INFO: Searching for product {}".format(search_product))
        homepage.search_product(search_product, search_product_xpath)
        element = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, locators.shipping_info_xpath))
        )
        shipping_info = browser.find_element_by_xpath(locators.shipping_info_xpath).text
        print("INFO: Shipping info displayed for {} is {}".format(search_product, shipping_info))
        assert shipping_info == 'Ready to dispatch in 3 - 5 business days'

    def test_shipping_info_in_cart_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        search_product = ["Patanjali Divya Lavangadi Vati", "Dr. Reckeweg Nux Vomica Dilution"]
        for product in search_product:
            print("INFO: Searching for product {}".format(product))
            search_product_xpath = locators.product_xpath.format(product)
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
            homepage.search_product(product, search_product_xpath)
            element = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, locators.shipping_info_xpath))
            )
            shipping_info = browser.find_element_by_xpath(locators.shipping_info_xpath).text
            print("INFO: Shipping info displayed for {} is {}".format(product, shipping_info))
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            browser.refresh()
            helper.wait()
        # click on cart link to navigate to cart page
        #browser.find_element_by_xpath(locators.cart_link_xpath).click()
        helper.navigate_to_url("https://www.distacart.com/cart")
        element = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, locators.cart_item_price))
        )
        total_shipping_info = browser.find_element_by_xpath(locators.cart_total_shipping_info_xpath).text
        #total_shipping_info = total_shipping_info.encode("utf-8")
        print("INFO: Shipping info displayed in cart page is {}".format(total_shipping_info))
        assert "Your order is ready to dispatch in 3 - 5 business days" in total_shipping_info
