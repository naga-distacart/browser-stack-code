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

class TestSupportedCurrencies:

    def test_supported_currencies(self, browser):
        supported_currencies = ["Angola (AOA)", "Argentina (ARS)", "Australia (AUD)", "Bahamas (BSD)",
                                "Canada (CAD)",
                                "Costa Rica (CRC)", "Czechia (CZK)", "Denmark (DKK)", "Estonia (EUR)",
                                "Ethiopia (ETB)",
                                "Finland (EUR)", "France (EUR)", "Germany (EUR)", "Greece (EUR)",
                                "Hong Kong SAR (HKD)",
                                "Hungary (HUF)", "India (INR)", "Indonesia (IDR)", "Ireland (EUR)", "Israel (ILS)",
                                "Japan (JPY)", "Malaysia (MYR)", "Malta (EUR)", "Mauritius (MUR)", "Monaco (EUR)",
                                "Myanmar (Burma) (MMK)", "Netherlands (EUR)", "New Zealand (NZD)",
                                "Nigeria (NGN)",
                                "Norway (NOK)", "Oman (USD)", "Peru (PEN)", "Philippines (PHP)", "Poland (PLN)",
                                "Portugal (EUR)", "Qatar (QAR)", "Romania (RON)", "Saudi Arabia (SAR)",
                                "Singapore (SGD)",
                                "South Africa (ZAR)", "South Korea (KRW)", "Switzerland (CHF)", "Taiwan (TWD)",
                                "Trinidad & Tobago (TTD)", "United Arab Emirates (AED)", "United Kingdom (GBP)",
                                "United States (USD)", "Vietnam (VND)"," " ]
        helper = Helper(browser)
        list_currencies = helper.get_elements_by_xpath(locators.Currency_select)
        print()
        assert 55 == len(list_currencies)

        for currency in list_currencies:
            text1=currency.text
            if text1.__contains__("("):
                print(currency.text)
                if currency.text in supported_currencies:
                    print("INFO: Currency {} is supported".format(currency.text))
                else:
                    print("INFO: Currency {} is not supported".format(currency.text))
                    assert 1 == 0
            else:
                continue

    def test_currency_symbol(self, browser):
        #supported_currencies = {"USD": "$", "CAD": "$", "AUD": "$", "GBP": "£", "EUR": "€", "JPY": "¥", "SGD": "$", "CHF": "SFr.", "SEK": "Kr"}
        supported_currencies = {"EUR": "€"}
        currencies = json.dumps(supported_currencies)
        currencies_symbol = json.loads(currencies)
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        helper.wait()
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
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        no_of_items = 1
        while no_of_items <= 1:
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
            )
            for currency in supported_currencies.keys():
                money_symbol = currencies_symbol.get(currency)
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
                helper.set_currency(currency)
                element = WebDriverWait(browser, 60).until(
                    EC.visibility_of_element_located((By.XPATH, locators.product_page_price_xpath))
                )
                product_page_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
                print("INFO: Currency symbol displayed in product page : ", product_page_price)
                assert money_symbol in product_page_price
                assert currency in product_page_price

                # Validate currency in customers who bought this item also bought
                cbb_product_item = browser.find_element_by_xpath(locators.cbb_product_image_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", cbb_product_item)
                cbb_product_price = browser.find_element_by_xpath(locators.cbb_product_price_xpath).text
                print("INFO: Currency symbol displayed in customers who bought products list : ", cbb_product_price)
                assert money_symbol in cbb_product_price

                # Validate currency in recommended products list
                """rec_product_item = browser.find_element_by_xpath(locators.rec_product_image_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", rec_product_item)
                rec_product_price = browser.find_element_by_xpath(locators.rec_product_current_price_xpath).text
                print("INFO: Currency symbol displayed in recommended products list : ", rec_product_price)
                assert money_symbol in rec_product_price"""

                # Validate currency in related items
                related_product_item = browser.find_element_by_xpath(locators.related_product_thumbnail_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", related_product_item)
                related_product_price = browser.find_element_by_xpath(locators.related_product_price_xpath).text
                print("INFO: Currency symbol displayed in related products list : ", related_product_price)
                assert money_symbol in related_product_price
                assert currency in related_product_price

                # Validate currency in recently viewed items
                search_product = "kaju rolls"
                search_product_xpath = locators.product_xpath.format("Vellanki Foods - Kaju Rolls")
                homepage = HomePage(browser)
                homepage.search_product(search_product, search_product_xpath)
                helper.wait()
                """recent_product_item = browser.find_element_by_xpath(locators.recent_product_thumbnail_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", recent_product_item)
                helper.wait_small()"""
                recent_product_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
                print("INFO: Currency symbol displayed in recent products list : ", recent_product_price)
                assert money_symbol in recent_product_price
                assert currency in recent_product_price
            no_of_items += 1
