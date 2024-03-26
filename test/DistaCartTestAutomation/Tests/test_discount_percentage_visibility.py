import datetime
import json

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
import DistaCartTestAutomation.Tests.conftest as c


class TestDiscountPercentageVisibility:

    def test_discount_percentage_visibility(self, browser):
        helper = Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/collections/noz2toz-kids-clothing")
        helper=Helper(browser)
        helper.wait()
        discount_text=browser.find_element_by_xpath(locators.discount_visibility).text
        assert "% off" in discount_text
        discounted_price=browser.find_element_by_xpath(locators.collection_page_discounted_price).text
        assert discounted_price is not None
        text=browser.find_element_by_xpath(locators.collection_page_discounted_price).value_of_css_property('text-decoration')
        assert text=="line-through solid rgb(148, 148, 148)"


