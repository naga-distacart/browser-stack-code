from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


class TestStickyAddtoCart:

    def test_sticky_add_to_cart(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url(
            "https://www.distacart.com/products/patanjali-giloy-ghan-vati-40-gm")
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
        # helper.move_to_element(browser.find_element_by_xpath("//a[text()='Got it!']"))
        # helper.click_on_element(browser.find_element_by_xpath("//a[text()='Got it!']"))
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        helper.wait()
        sticky_addtocart_section = browser.find_element_by_xpath(locators.customer_reviews_section)
        browser.execute_script("arguments[0].scrollIntoView();", sticky_addtocart_section)
        helper.wait()
       # WebDriverWait(browser, 60).until(
           # EC.presence_of_element_located(
               # (By.XPATH, "//div[@class='prod_title' and text()='Patanjali Giloy Ghanvati - Pack of 1' ]/../button/span[contains(text(),'Add to cart')]")))
       # assert helper.is_element_present_by_xpath("//div[@class='prod_title' and text()='Patanjali Giloy Ghanvati - Pack of 1' ]/../button/span[contains(text(),'Add to cart')]")










