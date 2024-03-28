# -*- coding: utf-8 -*-
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
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


class TestCurrencyCode:
    # supported_currencies = {"USD": "$", "CAD": "$", "AUD": "$", "GBP": "£", "EUR": "€", "JPY": "¥", "SGD": "$", "CHF": "SFr.", "SEK": "Kr"}
    supported_currencies = {"CAD": "$"}

    @pytest.mark.sanityH
    def test_currency_cart_page(self, browser, get_user_name, get_password):

        currencies = json.dumps(TestCurrencyCode.supported_currencies)
        currencies_symbol = json.loads(currencies)
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.set_currency("CAD")
        link=browser.current_url
        homepage.login(get_user_name, get_password)
        helper.get_correct_link(link)
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        helper.navigate_to_url(link+"/cart")
        element = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located((By.XPATH, locators.cart_page_heading))
        )
        #remove_elements = helper.get_elements_by_xpath(locators.cart_page_remove_button_xpath)
        cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
        print("Info: Items count displayed in cart page :", cart_count)
        while cart_count != '0':
            delete_product = browser.find_element_by_xpath(locators.cart_page_remove_button_xpath)
            delete_product.click()
            helper.wait()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("Info: Items count after deleting items in cart page :", cart_count)

        helper.wait_small()
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        no_of_items = 1
        for currency in TestCurrencyCode.supported_currencies.keys():
            money_symbol = currencies_symbol.get(currency)
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
            helper.set_currency(currency)
            while no_of_items <= 1:
                available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
                print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
                selected_element = random.choice(available_items)
                product = selected_element.text
                print("INFO: Randomly selected available product : ", product)
                helper.move_to_element(selected_element)
                helper.click_on_element(selected_element)
                helper.wait()
                element = WebDriverWait(browser, 120).until(
                    EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
                )
                print("INFO: Click on add to cart button : ", product)
                product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", product_item)
                assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
                browser.execute_script("arguments[0].click();", product_item)
                helper.wait()

                # click on cart link to navigate to cart page
                #browser.find_element_by_xpath(locators.cart_link_xpath).click()
                helper.get_correct_link(link)
                helper.navigate_to_url(link+"/cart")
                element = WebDriverWait(browser, 45).until(
                    EC.presence_of_element_located((By.NAME, locators.checkout_button_id))
                )
                helper.wait()
                cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
                cart_item_price = browser.find_element_by_xpath(locators.cart_item_price_currency_code_xpath).text
                cart_page_total_price = browser.find_element_by_xpath(locators.cart_page_total_currency_code_xpath).text
                print("INFO: Total items displayed in cart : ", cart_count)
                assert '1' == cart_count
                print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
                assert money_symbol in cart_item_price
                assert money_symbol in cart_page_total_price

                browser.find_element_by_xpath(locators.cart_quantity_plus_button_xpath).click()
                helper.wait_small()
                cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
                assert '2' == cart_count

                browser.find_element_by_xpath(locators.cart_quantity_minus_button_xpath).click()
                helper.wait_small()
                cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
                assert '1' == cart_count

                # Navigating to View full cart
                print(link)
                helper.get_correct_link(link)
                helper.navigate_to_url(link+"/cart")
                print("INFO: Navigating to View full cart")
                element = WebDriverWait(browser, 60).until(
                    EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
                )
                items_in_checkout_page = browser.find_element_by_xpath(locators.checkout_item_count_xpath1).text
                print("INFO: Total items displayed in checkout page : ", items_in_checkout_page)
                assert '1' == items_in_checkout_page
                checkout_total_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
                print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
                assert money_symbol in checkout_total_price
                assert cart_item_price == checkout_total_price.strip()
                no_of_items += 1
                available_items = []
                browser.back()
        homepage.logout()

    @pytest.mark.sanityH
    def test_currency_cart_popup(self, browser, get_user_name, get_password):
        currencies = json.dumps(TestCurrencyCode.supported_currencies)
        currencies_symbol = json.loads(currencies)
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.wait_small()
        homepage.login(get_user_name, get_password)
        helper.wait_small()
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        for currency in TestCurrencyCode.supported_currencies.keys():
            money_symbol = currencies_symbol.get(currency)
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
            helper.set_currency(currency)
            no_of_items = 1
            while no_of_items <= 1:
                available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
                print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
                selected_element = random.choice(available_items)
                product = selected_element.text
                print("INFO: Randomly selected available product : ", product)
                helper.move_to_element(selected_element)
                helper.click_on_element(selected_element)
                helper.wait()
                element = WebDriverWait(browser, 120).until(
                    EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
                )
                print("INFO: Click on add to cart button : ", product)
                product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
                browser.execute_script("arguments[0].scrollIntoView();", product_item)
                assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
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

                # mouse hover on cart link to open the cart popup
                #cart_link = browser.find_element_by_xpath(locators.cart_link_xpath)
                #ActionChains(browser).move_to_element(cart_link).perform()

                # element = WebDriverWait(browser, 45).until(
                #     EC.presence_of_element_located((By.XPATH, locators.cart_popup_order_notes_xpath))
                # )
                # browser.find_element_by_xpath(locators.cart_popup_order_notes_xpath).click()
                cart_popup_total_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                cart_popup_item_price = browser.find_element_by_xpath(locators.cart_popup_item_price_xpath).text
                print("INFO: Total price displayed in cart popup is: ", cart_popup_total_price)
                print("INFO: Product price displayed in cart popup is: ", cart_popup_item_price)
                assert money_symbol in cart_popup_total_price
                assert money_symbol in cart_popup_item_price
                no_of_items += 1
                available_items = []
                browser.back()
        #homepage.logout()
