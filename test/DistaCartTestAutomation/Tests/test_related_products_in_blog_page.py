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

#Automation script for [Req 442] Problogger app
class TestRelatedProductsInBlogPage:

    def test_related_products_in_blog_page(self, browser):

        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/blogs/learn/patanjali-aloe-vera-juice-with-fiber-ingredients-composition-properties-health-benefits-usage")
        helper.wait()
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Patanjali Aloe vera Juice with Fiber - Ingredients, Composition, Properties, Health Benefits, Usage"))
        related_products_section = browser.find_element_by_xpath(locators.related_products_blog)
        browser.execute_script("arguments[0].scrollIntoView();", related_products_section)
        helper.wait()
        browser.switch_to_frame("lsChannel")
        browser.find_elements_by_xpath(locators.related_products_tile)



