import re

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


class TestBabyKidsMenu:

    def test_baby_kids_menu(self, browser):
        category = "Baby & Kids"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_main_menu(category)
        print("INFO: Verifying category page title...Baby and Kids")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Baby and Kids")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Baby and Kids"))
