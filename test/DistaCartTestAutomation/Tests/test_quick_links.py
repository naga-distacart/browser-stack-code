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



class TestQuickLinks:
    def test_quick_links(self, browser):
        helper = Helper(browser)
        quick_links = ["https://www.distacart.com/pages/taste-of-bharat", "https://www.distacart.com/pages/thebeautyspot", "https://www.distacart.com/pages/baby-kids", "https://www.distacart.com/pages/indian-fashion"]
        for quick_link in quick_links:
            browser.get(quick_link)
            helper.wait_small()
            page_name = browser.find_element_by_xpath("//li[@class='breadcrumbs__item']//a[contains(@href, '/pages/')]").text
            all_elements = browser.find_elements_by_xpath(locators.all_elements_presented_on_collection_page_xpath)
            len_all_elements = len(all_elements)
            if len_all_elements > 1:
                print("the sub categories are presented in the  collection page of ", format(page_name))
                assert len_all_elements > 1


            else:
                print("the sub categories are not presented in the  collection page of", format(page_name))
                assert len_all_elements > 1



