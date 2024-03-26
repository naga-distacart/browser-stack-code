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

#JiraID:DC-553
class TestSchemaCheck:
    def test_schema_check(self, browser):
        browser.get("https://validator.schema.org/#url=https%3A%2F%2Fwww.distacart.com%2Fen-de%2Fproducts%2Floreal-paris-x-tenso-oleoshape-smoothing-and-neutralizing-straightening-hair-cream")
        WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,locators.product_select_schema)))
        browser.find_element_by_xpath(locators.product_select_schema).click()
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, locators.product_schema_count)))
        count=browser.find_elements_by_xpath(locators.product_schema_count)
        assert len(count)==1
