import re

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


class TestBuyItNow:

    @pytest.mark.sanityH
    def test_buy_it_now(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        no_of_items = 1

        available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
        print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
        selected_element = random.choice(available_items)
        product = selected_element.text
        print("INFO: Randomly selected available product : ", product)
        helper.move_to_element(selected_element)
        helper.click_on_element(selected_element)
        helper.wait()
        helper.wait()
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
        print("INFO: Click on but it now button : ", product)
        product_item = browser.find_element_by_xpath(locators.buy_with_shop_pay)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        assert helper.is_element_present_by_xpath(locators.buy_with_shop_pay)
        price = browser.find_element_by_xpath(locators.product_price_xpath).text
        print("INFO: Verify price of {} is {}".format(product, price))
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait_small()
        browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='shop-pay-login-iframe']"))
        time.sleep(3)
        element = browser.find_elements_by_xpath(locators.continue_with_shop_pay)
        assert len(element) > 0

        """element = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
        )
        checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
        checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text"""

        # element = WebDriverWait(browser, 60).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[@aria-labelledby='order-total']/div/span[2]"))
        # )
        # # element = WebDriverWait(browser, 60).until(
        #     EC.presence_of_element_located((By.XPATH, locators.discounted_price_xpath))
        # )
        # checkout_total_price = browser.find_element_by_xpath("//span[@aria-labelledby='order-total']/div/span[2]").text
        # checkout_total_price = browser.find_element_by_xpath(locators.total_price_xpath).text
        # s = re.sub("[^0123456789\.]", "", checkout_total_price)
        # # checkout_total_currency = browser.find_element_by_xpath("//span[@aria-labelledby='order-total']/div/span[1]").text
        # print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
        # # assert price == checkout_total_price.strip() + " " + checkout_total_currency
        # checkout_total_currency = browser.find_element_by_xpath(locators.currency_total_price_checkout_xpath).text
        # time.sleep(3)
        # assert price == checkout_total_price + " " + checkout_total_currency
        # no_of_items += 1
        # available_items = []
        # browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='shop-pay-login-iframe']"))
        # time.sleep(3)
        # element = browser.find_elements_by_xpath(locators.continue_with_shop_pay)
        # assert len(element) > 0

    @pytest.mark.sanityH
    def test_increase_quantity_buy_it_now(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "wellness"
        no_of_items = 1
        while no_of_items <= 1:
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            """selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)"""
            helper.wait()
            #increase_quantity = browser.find_element_by_xpath(locators.quantity_plus_button_xpath)
            assert 0 == len(browser.find_elements_by_xpath(locators.quantity_plus_button_xpath))
            no_of_items += 1
            """helper.move_to_element(increase_quantity)
            helper.click_on_element(increase_quantity)
            #browser.find_element_by_xpath(locators.quantity_plus_button_xpath).click()
            print("INFO: Click on buy it now button : ", product)
            product_item = browser.find_element_by_xpath(locators.buy_it_now_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.buy_it_now_button_xpath)
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()

            items_in_checkout_page = browser.find_element_by_xpath(locators.checkout_item_count_xpath).text
            print("INFO: Total items displayed in checkout page : ", items_in_checkout_page)
            assert '2' == items_in_checkout_page
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price != checkout_total_price.strip()
            no_of_items += 1
            available_items = []"""
