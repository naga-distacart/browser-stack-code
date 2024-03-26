import re

#from py._code._assertionold import Assert
from selenium import webdriver
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


class TestSubscribeEmailTextbox:

    def test_subscribe_email_textbox(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.go_to_home_page()
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.home_button_xpath))
        )
        email_textbox = browser.find_element_by_xpath(locators.email_input_box)
        browser.execute_script("arguments[0].scrollIntoView();", email_textbox)
        assert helper.is_element_present_by_xpath(locators.notify_me_via_email_button)
