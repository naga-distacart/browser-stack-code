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


class TestTollFreeLegalAndCopyrightpolicy:

    def test_tollfree_number(self,browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.toll_free_text)))
        assert helper.is_element_present_by_xpath(locators.toll_free_text)



    def test_copyright_link_and_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.move_to_element(browser.find_element_by_xpath(locators.copyright_policy_element))
        helper.click_on_element(browser.find_element_by_xpath(locators.copyright_policy_element))
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.copyright_page_title)))
        assert helper.is_element_present_by_xpath(locators.copyright_page_title)
        assert helper.is_element_present_by_xpath(locators.copyright_page_text)

    def test_legal_policy_link_and_page(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.move_to_element(browser.find_element_by_xpath(locators.legal_policy_text))
        helper.click_on_element(browser.find_element_by_xpath(locators.legal_policy_text))
        helper.wait()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.report_infringement_title)))
        assert helper.is_element_present_by_xpath(locators.report_infringement_title)
        assert helper.is_element_present_by_xpath(locators.send_message_button)










