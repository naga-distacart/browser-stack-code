from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
from selenium.webdriver.support.ui import Select
import time
import pytest
import random


class TestShopButton:

    def test_shop_button(self, browser):
        helper = Helper(browser)
        shop_now_list = ["https://www.distacart.com/products/indian-clothing-womens-ethnic-kurta-with-pant-and-dupatta-noz2toz","https://www.distacart.com/products/women-ethnic-kurta-with-pant-and-dupattaghanti_black?variant=42866477236383"]
        for show_now in shop_now_list:
            browser.get(show_now)
            helper.wait_small()
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
                    browser.find_element_by_xpath("//*[text()='No Thanks']").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cross-save-badge']")))
            Notification_title = browser.find_element_by_xpath("//a[@class='cross-product-title']").text
            browser.find_element_by_xpath("//span[@class='cross-save-badge']").click()
            helper.wait_small()
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.product_tile_name)))
            product_name = browser.find_element_by_xpath(locators.product_tile_name).text
            assert Notification_title == product_name
