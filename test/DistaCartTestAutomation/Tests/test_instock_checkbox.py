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
class TestInStockCheckbox:
    def sort_by_check(self,browser,link):
        helper=Helper(browser)
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=best-selling"
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, locators.sort_by_collections_page)))
        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_featured).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=manual"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_best_selling).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=best-selling"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_Alpha_A_Z).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=title-ascending"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_Alpha_Z_A).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=title-descending"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_price_L_H).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=price-ascending"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_price_H_L).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=price-descending"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_Date_N_O).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=created-descending"

        browser.find_element_by_xpath(locators.sort_by_collections_page).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.sort_by_Date_O_N).click()
        helper.wait_small()
        helper.get_correct_link(link)
        assert browser.current_url == link + "/?sort_by=created-ascending"

    # def test_instock_checkbox(self, browser):
    #     homepage = HomePage(browser)
    #     helper = Helper(browser)
    #     currencies = ["AED", "AUD", "CAD", "CHF", "CZK", "DKK", "HKD", "GBP"]
    #     for currency in currencies:
    #         browser.get("https://www.distacart.com/en-{}/collections/dista-pick".format((currency[:2].lower())))
    #         helper.wait()
    #         element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Dista Pick"))))
    #         assert helper.is_element_present_by_xpath(locators.product_category_title.format("Dista Pick"))
    #         link=browser.current_url
    #         assert helper.is_element_present_by_xpath(locators.in_stock_checkbox_xpath)
    #         helper.wait()
    #         popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
    #         if (len(popup) > 0):
    #             browser.switch_to.frame("cmessage_form_iframe")
    #             # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
    #             try:
    #                 No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
    #             except:
    #                 helper.wait()
    #                 No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
    #             if (len(No_thanks) > 0):
    #                 # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
    #                 browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
    #                 browser.switch_to.default_content()
    #         browser.switch_to.default_content()
    #         browser.find_element_by_xpath(locators.in_stock_checkbox_xpath).click()
    #         helper.wait_small()
    #         TestInStockCheckbox.sort_by_check(self,browser,link)
    # 
    # 
    #     eur_links = ["nl", "eu", "de", "ie"]
    #     for eur_link in eur_links:
    #         browser.get("https://www.distacart.com/en-{}/collections/dista-pick".format(eur_link))
    #         element = WebDriverWait(browser, 60).until(
    #             EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Dista Pick"))))
    #         assert helper.is_element_present_by_xpath(locators.product_category_title.format("Dista Pick"))
    #         link = browser.current_url
    #         assert helper.is_element_present_by_xpath(locators.in_stock_checkbox_xpath)
    #         browser.find_element_by_xpath(locators.in_stock_checkbox_xpath).click()
    #         helper.wait_small()
    #         assert browser.current_url == link + "/?sort_by=best-selling"
    #         TestInStockCheckbox.sort_by_check(self, browser, link)
