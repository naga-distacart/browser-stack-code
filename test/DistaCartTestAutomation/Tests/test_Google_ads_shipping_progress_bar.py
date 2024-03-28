from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random


class TestGoogleAdsShippingProgressBar():

    @pytest.mark.sanityH
    def test_google_ads_shipping_progress_bar_US(self, browser):
        helper=Helper(browser)
        browser.get("https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031&currency=USD&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping&gclid=EAIaIQobChMIh9SW1POK_wIV-PPjBx3QmQw6EAQYASABEgI14PD_BwE")
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
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        add_to_cart=browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        time.sleep(3)
        ActionChains(browser).move_to_element(add_to_cart).click().perform()
        helper.wait_small()
        shipping_msg=browser.find_element(By.XPATH,locators.shipping_msg_mini_cart_xpath).text
        assert "200 $" not in shipping_msg

    @pytest.mark.sanityH
    def test_google_ads_shipping_progress_bar_CA(self, browser):
        helper=Helper(browser)
        browser.get("https://www.distacart.com/en-ca/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping&srsltid=AR57-fAbqwK_ixuYBfRzyzcm5i-ZGbJzYvLBuX-FFHmmIGxwsNhk_Mo-CjM")
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
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        add_to_cart=browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        time.sleep(3)
        ActionChains(browser).move_to_element(add_to_cart).click().perform()
        helper.wait_small()
        shipping_msg=browser.find_element(By.XPATH,locators.shipping_msg_mini_cart_xpath).text
        assert "200 $" not in shipping_msg

    @pytest.mark.sanityH
    def test_google_ads_shipping_progress_bar_AU(self, browser):
        helper=Helper(browser)
        browser.get("https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031&currency=AUD&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping&gclid=EAIaIQobChMIh9SW1POK_wIV-PPjBx3QmQw6EAQYASABEgI14PD_BwE")
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
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        add_to_cart=browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        time.sleep(3)
        ActionChains(browser).move_to_element(add_to_cart).click().perform()
        helper.wait_small()
        shipping_msg=browser.find_element(By.XPATH,locators.shipping_msg_mini_cart_xpath).text
        assert "200 $" not in shipping_msg


