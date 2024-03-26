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

#Automation script for [Req 122] Collection page should have an in stock check box
class TestAnchorTextLink:

    def test_anchor_text_personal_info(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        footer_header_user = browser.find_element_by_xpath(locators.footer_user_text)
        browser.execute_script("arguments[0].scrollIntoView();", footer_header_user)
        assert helper.is_element_present_by_xpath(locators.personal_info_footer_text)
        assert helper.is_element_present_by_xpath(locators.orders_footer_text)
        assert helper.is_element_present_by_xpath(locators.addresses_footer_text)
        helper.move_to_element(browser.find_element_by_xpath(locators.personal_info_footer_text))
        helper.click_on_element(browser.find_element_by_xpath(locators.personal_info_footer_text))
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.personal_info_page_element)))
        assert helper.is_element_present_by_xpath(locators.customer_login_element)

    def test_anchor_text_orders(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        footer_header_user = browser.find_element_by_xpath(locators.footer_user_text)
        browser.execute_script("arguments[0].scrollIntoView();", footer_header_user)
        assert helper.is_element_present_by_xpath(locators.personal_info_footer_text)
        assert helper.is_element_present_by_xpath(locators.orders_footer_text)
        assert helper.is_element_present_by_xpath(locators.addresses_footer_text)
        helper.move_to_element(browser.find_element_by_xpath(locators.orders_footer_text))
        helper.click_on_element(browser.find_element_by_xpath(locators.orders_footer_text))
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.personal_info_page_element)))
        assert helper.is_element_present_by_xpath(locators.customer_login_element)


    def test_anchor_text_addresses(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        footer_header_user = browser.find_element_by_xpath(locators.footer_user_text)
        browser.execute_script("arguments[0].scrollIntoView();", footer_header_user)
        assert helper.is_element_present_by_xpath(locators.personal_info_footer_text)
        assert helper.is_element_present_by_xpath(locators.orders_footer_text)
        assert helper.is_element_present_by_xpath(locators.addresses_footer_text)
        helper.move_to_element(browser.find_element_by_xpath(locators.addresses_footer_text))
        helper.click_on_element(browser.find_element_by_xpath(locators.addresses_footer_text))
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.personal_info_page_element)))
        assert helper.is_element_present_by_xpath(locators.customer_login_element)








