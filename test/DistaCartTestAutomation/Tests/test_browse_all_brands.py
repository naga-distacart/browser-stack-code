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


class TestBrowseAllBrands():

    def test_browse_all_brands(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        #homepage.go_to_home_page()
        homepage.click_on_main_menu("Browse All Brands")

        helper.wait()
        print("INFO: Verifying Brands page is displayed...")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Brands"))
        brands_count = helper.get_elements_by_xpath("//div[@class='col-md-6']/h2")
        assert len(brands_count) > 0
        #browser.find_element_by_xpath("//ul/li/a[text()='Adel Homeopathy']").click()
        helper.wait()
        element = browser.find_element_by_xpath("//ul/li/a[text()='Adel Homeopathy']")
        browser.execute_script("arguments[0].scrollIntoView();", element)
        browser.execute_script("arguments[0].click();", element)
        helper.wait()
        assert helper.is_element_present_by_xpath("//li[@class='breadcrumbs__item']/a[text()='Adel Homeopathy']")
        