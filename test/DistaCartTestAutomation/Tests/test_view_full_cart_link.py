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



class TestViewFullCartLink:
    def test_view_full_cart_link(self, browser):
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
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        helper.wait_small()
        # element = WebDriverWait(browser, 45).until(
        #     EC.presence_of_element_located((By.XPATH, locators.cart_popup_order_notes_xpath))
        # )
        assert helper.is_element_present_by_xpath(locators.view_full_cart_link)
        browser.find_element_by_xpath(locators.view_full_cart_link).click()
        helper.wait()
        element = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located((By.XPATH, locators.cart_page_breadcrumb_title))
        )
        assert helper.is_element_present_by_xpath(locators.cart_page_breadcrumb_title)
        assert helper.is_element_present_by_xpath(locators.fullcart_variant_xpath)

