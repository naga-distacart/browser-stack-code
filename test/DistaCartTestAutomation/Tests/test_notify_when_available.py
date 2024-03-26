from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random


class TestNotifyWhenAvailable:

    def test_notify_when_available(self, browser):
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/en-mm/products/Siridhanya-Foxtail-Millet")
        WebDriverWait(browser, 120).until(
            EC.visibility_of_element_located(
                (By.XPATH, locators.product_sold_out_xpath))
        )

        print("INFO: Verify notify me when available button is displayed")
        WebDriverWait(browser, 120).until(
            EC.element_to_be_clickable(
                (By.XPATH, locators.product_notify_button_xpath))
        )
        print("INFO: Select product variant color")
        #browser.find_element_by_xpath(locators.product_variant_xpath.format("Purple")).click()
        print("INFO: Select product variant size")
       # browser.find_element_by_xpath(locators.product_variant_xpath.format("42")).click()
        print("INFO: Click on notify me when available button")
        helper.wait()
        action = ActionChains(browser)
        #notify_button = browser.find_element_by_xpath(locators.product_notify_button_xpath)
       # browser.execute_script("arguments[0].scrollIntoView();", notify_button)
        notify_button = browser.find_element_by_xpath(locators.product_notify_button_xpath)
        time.sleep(4)
        action.move_to_element(notify_button).click().perform()
        time.sleep(4)
        # browser.execute_script("arguments[0].click();", notify_button)
        notify_button.click()
        time.sleep(6)
        print("INFO: Verify the selected variant is auto selected in notify me when available popup")
        browser.switch_to.frame("cmessage_bis_iframe")
        #browser.switch_to.active_element
        #sel = Select(browser.find_element_by_xpath(locators.product_notify_variant_xpath))
        sel = browser.find_element_by_xpath("//p[text()='Register to receive a notification when this item comes back in stock.']")
        time.sleep(5)
        assert "True" == str(helper.is_element_present_by_xpath("//p[text()='Register to receive a notification when this item comes back in stock.']"))
        helper.wait()

        #selected_variant = browser.execute_script("return arguments[0].selectedOptions[0].innerText", sel)

        #assert 'Black / 38' == selected_variant
        #assert "True" == str(helper.is_element_present_by_xpath(locators.product_notify_email_xpath))
        #assert "True" == str(helper.is_element_present_by_xpath(locators.product_notify_me_button_xpath))
