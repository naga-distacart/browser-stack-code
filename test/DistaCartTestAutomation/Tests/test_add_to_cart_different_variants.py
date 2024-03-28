import re

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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


class TestAddToCartDifferentVariants:

    @pytest.mark.sanityH
    def test_add_to_cart_different_variants(self, browser):
        helper = Helper(browser)
        helper.set_currency("USD")
        link=browser.current_url
        product = 'sbl-homeopathy-nux-vomica-dilution'
        helper.get_correct_link(link)
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        helper.navigate_to_url(link+"/collections/sbl-homeopathy/products/"+product)
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
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
        time.sleep(3)
        browser.find_element_by_xpath("//div[text()='Potency']/../div[@value='30 CH']/label").click()
        browser.find_element_by_xpath("//div[text()='Size']/../div[@value='30 ml']/label").click()
        ActionChains(browser).move_to_element(browser.find_element_by_xpath("//div[text()='Packs']/../div[@value='Pack of 1']/label")).click().perform()

        print("INFO: Click on add to cart button")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        #assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        price = browser.find_element_by_xpath(locators.product_price_xpath).text
        print("INFO: Verify product price of {} is {}".format(product, price))
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        assert helper.is_element_present_by_xpath(
            "//a[text()='SBL Homeopathy Nux Vomica Dilution - 30 CH / 30 ml / Pack of 1']")
        browser.find_element_by_xpath("//img[@class='close_mini_cart ls-is-cached lazyloaded']").click()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
        browser.find_element_by_xpath("//div[text()='Potency']/../div[@value='30 CH']/label").click()
        browser.find_element_by_xpath("//div[text()='Size']/../div[@value='30 ml']/label").click()
        browser.find_element_by_xpath("//div[text()='Packs']/../div[@value='Pack of 3']/label").click()

        print("INFO: Click on add to cart button")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        #assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        price = browser.find_element_by_xpath(locators.product_price_xpath).text
        print("INFO: Verify product price of {} is {}".format(product, price))
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        assert helper.is_element_present_by_xpath("//a[text()='SBL Homeopathy Nux Vomica Dilution - 30 CH / 30 ml / Pack of 3']")

        browser.switch_to.default_content()
        browser.find_element_by_xpath("//img[@class='close_mini_cart ls-is-cached lazyloaded']").click()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
        browser.find_element_by_xpath("//div[text()='Potency']/../div[@value='200 CH']/label").click()
        browser.find_element_by_xpath("//div[text()='Size']/../div[@value='30 ml']/label").click()
        browser.find_element_by_xpath("//div[text()='Packs']/../div[@value='Pack of 1']/label").click()
        print("INFO: Click on add to cart button")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        #assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        price = browser.find_element_by_xpath(locators.product_price_xpath).text
        print("INFO: Verify product price of {} is {}".format(product, price))
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        assert helper.is_element_present_by_xpath(
            "//a[text()='SBL Homeopathy Nux Vomica Dilution - 200 CH / 30 ml / Pack of 1']")
        helper.wait_small()

        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print("INFO: Subtotal displayed in cart after increasing the product quantity for first time : ", subtotal)
        assert '$23.37 USD' == subtotal
        browser.find_element_by_xpath("//img[@class='close_mini_cart ls-is-cached lazyloaded']").click()
        cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
        print("INFO: Total items displayed in cart : ", cart_count)
        assert '3' == cart_count
