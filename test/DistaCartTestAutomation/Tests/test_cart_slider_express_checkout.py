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


class TestCartSliderExpressCheckout:
    @pytest.mark.sanityH
    def test_cart_slider_express_checkout(self, browser, get_user_name, get_password):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm")
        helper.wait()
        print("INFO: Click on add to cart button : ")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        helper.wait_small()
        # element = WebDriverWait(browser, 45).until(
        #     EC.presence_of_element_located((By.XPATH, locators.cart_popup_order_notes_xpath))
        # )
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
        element1 = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located((By.XPATH, locators.shoppay_element))
        )

        assert helper.is_element_present_by_xpath(locators.googlepay_element)
        assert helper.is_element_present_by_xpath(locators.shoppay_element)
        browser.find_element_by_xpath(locators.shoppay_element).click()
        helper.wait()
        """element2 = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located((By.XPATH, locators.shoppay_checkout_page_element))
        )
        assert helper.is_element_present_by_xpath(locators.quick_checkout_element)"""
        shop_pay_items = helper.get_elements_by_xpath("//*[@id='shop-pay-logo']")
        assert 0 == len(shop_pay_items)
