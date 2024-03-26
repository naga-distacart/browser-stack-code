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


class TestHomePageSoldOut:

    def test_home_page_sold_out(self, browser):
        helper = Helper(browser)
        sold_out_items = helper.get_elements_by_xpath("//button[contains(@class,'disabled add-to-cart-btn')]")
        print(len(sold_out_items))
        assert len(sold_out_items) == 0