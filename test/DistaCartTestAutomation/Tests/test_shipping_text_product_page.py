from selenium.webdriver.common.keys import Keys

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
from selenium.webdriver.support.ui import Select
import time
import pytest




class TestShippingTextProductPage():
    def test_shipping_text_product_page1(self, browser):
        helper=Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")
        currencies=browser.find_elements_by_xpath(locators.all_currencies)
        l=len(currencies)
        for i in range(0,int(l/2)):
            browser.find_element_by_xpath(locators.pick_currency_div_xpath).click()
            time.sleep(2)
            currencies = browser.find_elements_by_xpath(locators.all_currencies)
            currencies[i].click()
            country_name=browser.find_element_by_xpath(locators.country_name_xpath).get_attribute('id')
            country_name=str(country_name)
            country_name=country_name.replace('-',' ')
            print(country_name)
            helper.wait_small()
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            shipping_text=browser.find_element_by_xpath(locators.shipping_text_xpath).text
            shipping_text=shipping_text.lower()
            if country_name==" czechia":
                country_name="czech"
            if country_name==" ethiopia" or country_name==" estonia":
                continue
            if country_name==" hong kong sar":
                country_name=country_name.replace("sar","")
                country_name=country_name.replace(" ","")
            if country_name==" myanmar burma":
                country_name=country_name.replace("burma","")
                country_name=country_name.replace(" ","")
            assert country_name in shipping_text

    def test_shipping_text_product_page2(self, browser):
        helper=Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")
        currencies=browser.find_elements_by_xpath(locators.all_currencies)
        l=len(currencies)
        for i in range(int(l/2),l):
            browser.find_element_by_xpath(locators.pick_currency_div_xpath).click()
            time.sleep(2)
            currencies = browser.find_elements_by_xpath(locators.all_currencies)
            currencies[i].click()
            country_name=browser.find_element_by_xpath(locators.country_name_xpath).get_attribute('id')
            country_name=str(country_name)
            country_name=country_name.replace('-',' ')
            print(country_name)
            helper.wait_small()
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            shipping_text=browser.find_element_by_xpath(locators.shipping_text_xpath).text
            shipping_text=shipping_text.lower()
            if country_name==" czechia":
                country_name="czech"
            if country_name==" ethiopia" or country_name==" estonia":
                continue
            if country_name==" hong kong sar":
                country_name=country_name.replace("sar","")
                country_name=country_name.replace(" ","")
            if country_name==" myanmar burma":
                country_name=country_name.replace("burma","")
                country_name=country_name.replace(" ","")
            if country_name==" trinidad amp tobago":
                country_name=country_name.replace("amp","and")
            if country_name==" oman":
                country_name="united states"
            assert country_name in shipping_text




