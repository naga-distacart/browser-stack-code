from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random

class Test_DC_189_DC_146ProductToggleIssue:

    def test_DC_189_DC_146_product_toggle_issue_Collection_page(self, browser):
        link=browser.current_url
        browser.get(link+"/collections/dista-pick")
        product_card=browser.find_element_by_xpath(locators.single_product_select_in_collection_page.format("Mamaearth Onion Shampoo For Hair Fall Care"))
        ActionChains(browser).move_to_element(product_card).perform()
        Add_to_cart=browser.find_element_by_xpath(locators.single_product_add_tocart.format("Mamaearth Onion Shampoo For Hair Fall Care"))
        time.sleep(6)
        ActionChains(browser).move_to_element(Add_to_cart).click().perform()
        time.sleep(6)
        browser.find_element_by_xpath(locators.option_select_collection_page.format("Mamaearth Onion Shampoo For Hair Fall Care","25 ml")).click()
        time.sleep(6)
        text=browser.find_elements_by_xpath(locators.please_select_other_variant_text_xpath)
        assert text[0].text=="Please select another variant"
        text1=browser.find_elements_by_xpath(locators.selected_varaint_is_sold_text_xpath)
        assert text1[0].text=="Selected Variant is Sold out"
        browser.find_element_by_xpath(locators.dista_pick_text_xpath).click()
        time.sleep(3)
        text = browser.find_elements_by_xpath(locators.please_select_other_variant_text_xpath)
        time.sleep(2)
        text1 = browser.find_elements_by_xpath(locators.selected_varaint_is_sold_text_xpath)
        assert len(text)==0
        assert len(text1)==0
    def test_DC_189_DC_146_product_toggle_issue_Product_page(self, browser):
        link=browser.current_url
        browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
        WebDriverWait(browser,60).until(EC.presence_of_element_located((By.XPATH,locators.add_to_cart_product_page)))
        add_to_cart=browser.find_elements_by_xpath(locators.add_to_cart_product_page)
        assert len(add_to_cart)==1
        browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
        time.sleep(4)
        add_to_cart = browser.find_elements_by_xpath(locators.add_to_cart_not_available)
        time.sleep(4)
        assert len(add_to_cart)==1
        browser.find_element_by_xpath(locators.product_variant_of_pack_of_n_xpath.format("Pack of 1")).click()
        add_to_cart = browser.find_elements_by_xpath(locators.add_to_cart_product_page)
        time.sleep(3)
        assert len(add_to_cart) == 1










