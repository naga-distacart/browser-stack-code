from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random


class TestPageLoad:

    def test_page_load(self, browser):
        helper = Helper(browser)
        about_us_link = "//p/a[text()='About us']"
       # browser.delete_all_cookies()
        print("INFO: Loading home page")
        helper.navigate_to_url("https://www.distacart.com")
        try:
            WebDriverWait(browser, 40).until(
                EC.element_to_be_clickable(
                    (By.XPATH, about_us_link))
            )
        except TimeoutException:
            print("INFO: Home page is not loaded within expected time of 40 secs")

        print("INFO: Loading collections page")
        collections = ['Homeopathy', 'Ayurveda', 'Unani']
        shop_by_categories_link = "//div[@class='main-nav__wrapper']/div/div/ul/div/li/a[@data-dropdown-rel='shop-by-categories']"
       # category_link = "//div[@class='main-nav__wrapper']/div/div[@data-dropdown='shop-by-categories']/div/div/div/div[@class='dropdown_column__menu']/ul/li/a[text()='{}']"
        category_link="//div[@class='main-nav__wrapper']/div/div[@data-dropdown='shop-by-categories']/div/div/div/div//*[text()='{}']"
        browser.find_element_by_xpath(shop_by_categories_link).click()
        random_link = category_link.format(random.choice(collections))
        browser.find_element_by_xpath(random_link).click()
        load_more_button_xpath = "//span/a[contains(@class,'load-more__btn action_button continue-button')]"
        try:
            WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, load_more_button_xpath))
            )
        except TimeoutException:
            print("INFO: Collections page is not loaded within expected time of 20 secs")
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

        print("INFO: Loading product page")
        available_items = helper.get_elements_by_xpath("//*[@class='snize-title']")
        print("INFO: Available items found in 1st page of : ", len(available_items))
        selected_element = random.choice(available_items)
        product = selected_element.text
        print("INFO: Randomly selected available product : ", product)
        helper.move_to_element(selected_element)
        helper.click_on_element(selected_element)

        buy_it_now_button = "//button[text()='Buy it now']"
        try:
            WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, buy_it_now_button))
            )
        except TimeoutException:
            print("INFO: Product page is not loaded within expected time of 20 secs")
