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

class TestAddToCartCurrencies:

    def test_cart_currency_symbol(self, browser):
        supported_currencies1 = {"USD": "$", "CAD": "$", "AUD": "$"}
        #supported_currencies1 = {"USD": "$", "GBP": "£", "JPY": "¥","CHF": "CHF","EUR": "€","AUD": "$"}
        #supported_currencies = {"EUR": "€"}
        with open("./../Data/currencies.json") as jsonFile:
            # supported_currencies = json.load(jsonFile)
            """jsonData = data["emp_details"]
            for x in jsonData:
                keys = x.keys()
                print(keys)
                values = x.values()
                print(values)"""

        # currencies = json.dumps(supported_currencies)
        # currencies_symbol = json.loads(currencies)
        category = "Ayurveda"
        link=browser.current_url
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        helper.wait()
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Ayurveda"
        no_of_items = 1
        while no_of_items <= 1:
            # available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            # print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            # selected_element = random.choice(available_items)
            product = "Isha Life Neem and Turmeric"
            # print("INFO: Randomly selected available product : ", product)
            # helper.move_to_element(selected_element)
            # helper.click_on_element(selected_element)
            helper.get_correct_link(link)
            browser.get(link+"/products/isha-life-neem-and-turmeric-capsules")
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
            )
            for currency in supported_currencies1.keys():
                # money_symbol = currencies_symbol.get(currency)
                money_symbol = supported_currencies1[currency]
                print(money_symbol)
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
                helper.wait_small()
                helper.set_currency(currency)
                element = WebDriverWait(browser, 60).until(
                    EC.visibility_of_element_located((By.XPATH, locators.product_page_price_xpath))
                )
                product_page_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
                print("INFO: Currency symbol displayed in product page : ", product_page_price)
                assert money_symbol in product_page_price
                assert currency in product_page_price
                helper.wait()
                print("INFO: Click on add to cart button : ", product)
                product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", product_item)
                assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
                price = browser.find_element_by_xpath(locators.product_price_xpath).text
                # print("INFO: Verify price of {} is {}".format(product, price))
                browser.execute_script("arguments[0].click();", product_item)
                helper.wait()
                #browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
                helper.wait_small()
                subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                print("INFO: Subtotal displayed in cart is : ", subtotal)
                assert money_symbol in subtotal
                assert currency in subtotal
                free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
                print("INFO: Free shipping message displayed after adding {} in cart is {}".format(product,
                                                                                                   free_shipping_msg))
                assert money_symbol in free_shipping_msg
                assert currency in free_shipping_msg
                time.sleep(6)
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
                browser.switch_to.default_content()
                browser.find_element_by_xpath(locators.cart_minus_button_xpath).click()
                helper.wait_small()
            no_of_items += 1
    def test_cart_currency_symbol2(self, browser):
        supported_currencies1 = { "SGD": "$", "CHF": "CHF"}
        #supported_currencies1 = {"USD": "$", "GBP": "£", "JPY": "¥","CHF": "CHF","EUR": "€","AUD": "$"}
        #supported_currencies = {"EUR": "€"}
        with open("./../Data/currencies.json") as jsonFile:
            # supported_currencies = json.load(jsonFile)
            """jsonData = data["emp_details"]
            for x in jsonData:
                keys = x.keys()
                print(keys)
                values = x.values()
                print(values)"""

        # currencies = json.dumps(supported_currencies)
        # currencies_symbol = json.loads(currencies)
        link=browser.current_url
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        helper.wait()
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Ayurveda"
        no_of_items = 1
        while no_of_items <= 1:
            # available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            # print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            # selected_element = random.choice(available_items)
            product = "Isha Life Neem and Turmeric"
            # print("INFO: Randomly selected available product : ", product)
            # helper.move_to_element(selected_element)
            # helper.click_on_element(selected_element)
            helper.get_correct_link(link)
            browser.get(link+"/products/isha-life-neem-and-turmeric-capsules")
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
            )
            for currency in supported_currencies1.keys():
                # money_symbol = currencies_symbol.get(currency)
                money_symbol = supported_currencies1[currency]
                print(money_symbol)
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
                helper.wait_small()
                helper.set_currency(currency)
                element = WebDriverWait(browser, 60).until(
                    EC.visibility_of_element_located((By.XPATH, locators.product_page_price_xpath))
                )
                product_page_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
                print("INFO: Currency symbol displayed in product page : ", product_page_price)
                assert money_symbol in product_page_price
                assert currency in product_page_price
                helper.wait()
                # print("INFO: Click on add to cart button : ", product)
                product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", product_item)
                assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
                price = browser.find_element_by_xpath(locators.product_price_xpath).text
                # print("INFO: Verify price of {} is {}".format(product, price))
                browser.execute_script("arguments[0].click();", product_item)
                helper.wait()
                #browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
                helper.wait_small()
                subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                print("INFO: Subtotal displayed in cart is : ", subtotal)
                assert money_symbol in subtotal
                assert currency in subtotal
                free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
                print("INFO: Free shipping message displayed after adding {} in cart is {}".format(product,
                                                                                                   free_shipping_msg))
                assert money_symbol in free_shipping_msg
                assert currency in free_shipping_msg
                time.sleep(6)
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
                browser.switch_to.default_content()
                browser.find_element_by_xpath(locators.cart_minus_button_xpath).click()
                helper.wait_small()
            no_of_items += 1
