from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Helpers.helper import Helper

import time
import pytest

from DistaCartTestAutomation.Locators import locators


class TestAfterPayGeolocation():

    @pytest.mark.sanityH
    def test_geolocation_afterpay_product_page(self, browser):
        helper = Helper(browser)
        # link=browser.current_url
        helper.set_currency("GBP")
        helper.navigate_to_url("https://www.distacart.com/en-gb"+"/products/amit-pharma-dehshuddi-tablets")
        element = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Amit Pharma Dehshuddi Tablets')]"))
        )
        """WebDriverWait(browser, 120).until(
            EC.element_to_be_clickable(
                (By.XPATH, locators.after_pay_price))
        )"""
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
        time.sleep(5)
        # item = browser.execute_script("return document.querySelector('afterpay-placement').shadowRoot.querySelector('p.afterpay-paragraph span strong')")
        item=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath)
        print(item.text)
        after_pay_text = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
        print("INFO: Verify that afterpay amount displayed in Product page is as per geolocation")
        assert 'GBP' in after_pay_text

    @pytest.mark.sanityH
    def test_geolocation_coupons(self, browser):
        helper = Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        helper.navigate_to_url(link+"/pages/coupons")
        element = WebDriverWait(browser, 45).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.email_offer_item))
        )
        sms_offer_left_text = browser.find_element_by_xpath(locators.sms_offer_left_item).text
        sms_offer_right_text = browser.find_element_by_xpath(locators.sms_offer_right_item).text
        email_offer_text = browser.find_element_by_xpath(locators.email_offer_item).text
        print("INFO: Verify that currency displayed in Coupons page is as per geolocation")
        assert 'GBP' in sms_offer_left_text
        assert 'Text DISTA to +1 (855) 492-1730' in sms_offer_right_text
        assert 'GBP' in email_offer_text
