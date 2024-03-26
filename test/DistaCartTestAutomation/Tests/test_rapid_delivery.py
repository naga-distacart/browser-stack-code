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
import random


class TestRapidDelivery:

    def test_rapid_delivery_info(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        #product = 'isha-life-neem-and-turmeric-capsules'
        product = 'himalaya-speman-tablets-60-tablets'
        helper.navigate_to_url("https://www.distacart.com/products/" + product)
        helper.wait()
        assert helper.is_element_present_by_xpath("//div[@class='rapiddelivery-div']")
        assert helper.is_element_present_by_xpath("//div[@class='rapiddelivery-div']/b[@class='rapiddelivery']")
        assert helper.is_element_present_by_xpath("//div[@class='rapiddelivery-div']/span[@class='rapid_delivery_info']")
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
        browser.find_element_by_xpath("//div[@class='rapiddelivery-div']/span[@class='rapid_delivery_info']").click()

        assert helper.is_element_present_by_xpath("//div[@class='rapid_delivery-popup']")
        browser.find_element_by_xpath("//a[@class='rapid_delivery-popup-closeBtn']").click()
        shipping_info = browser.find_element_by_xpath(locators.rapid_shipping_info_xpath).text
        print("INFO: Shipping info displayed is {}".format(shipping_info))
        assert shipping_info == 'Ready to dispatch in 1 business day'
        print("INFO: Click on add to cart button")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        browser.execute_script("arguments[0].click();", product_item)
        time.sleep(6)
        shipping_text_cart = browser.find_element_by_xpath("//div[@class='cart_popup_final_delivery_info_txt']/span[@class='delivery_desc']").text
        print("INFO: Verify shipping info in cart popup for rapid delivery product")
        assert shipping_text_cart == 'Your order is ready to dispatch in 1 business day'
        assert helper.is_element_present_by_xpath("//p[@class='mini-rapiddelivery-txt']/b[text()='rapid delivery']")
        browser.find_element_by_xpath("//a[text()='View Full Cart']").click()
        helper.wait()
        shipping_text = browser.find_element_by_xpath("//span[@class='pdp-page__text']").text
        assert shipping_text == 'Ready to dispatch in 1 business day'
        assert helper.is_element_present_by_xpath("//p[@class='cart-rapiddelivery-txt']/b[text()='rapid delivery']")
        total_shipping_info = browser.find_element_by_xpath("//span[@class='delivery_desc cart-rapid-delivery-info']").text
        print("INFO: Shipping info displayed in cart page is {}".format(total_shipping_info))
        assert "Your order is ready to dispatch in 1 business day." in total_shipping_info

    def test_rapid_delivery_shipping_info_in_cart_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        search_product = ["Patanjali Divya Lavangadi Vati", "Isha Life Neem and Turmeric Capsules"]

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
            # print("INFO: Verify price of {} is {}".format(product, price))
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
