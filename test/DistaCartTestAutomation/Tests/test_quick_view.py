import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
from selenium.webdriver.support.ui import Select
import time
import pytest
import random


class TestQuickView:

    def test_quick_view(self, browser):
        helper = Helper(browser)
        helper.wait()
        #browser.find_element_by_xpath("//li[@class='snacks-menu-item']//a[normalize-space()='Snacks']").click()
        browser.find_element_by_xpath("//li[@class='wellness-menu-item']//a").click()
        time.sleep(4)

        # browser.find_element_by_xpath("//a[@href='/collections/snacks/products/nature-land-organics-dry-amla-candy-sweet']//div[@class='snize-item clearfix snize-stock-status-showed']//span[@class='snize-overhidden']//button[@class='snize-button snize-action-button snize-quick-view-button'][normalize-space()='Quick view']").click()
        # helper.wait()
        quick_views = browser.find_elements_by_xpath(locators.quick_views_xpath)
        if quick_views:
            # Generate a random index within the range of elements
            random_index = random.randint(0, len(quick_views) - 1)

            # Access the element at the random index
            random_product = quick_views[random_index]

            # Perform a click operation on the randomly selected product
            ActionChains(browser).move_to_element(random_product).click().perform()
        else:
            print("No elements found for the given XPath.")
        helper.wait()
        helper.wait()
        helper.wait()
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            try:
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            except:
                helper.wait()
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            if (len(No_thanks) > 0):
                # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[text()='No Thanks']").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()

        try:
            variants = browser.find_elements_by_xpath("//div[@class='snize-quick-view-form-wrapper']//*[contains(@class, 'snize-option-selector-wrapper')]")
            variants_first_components = browser.find_elements_by_xpath("//select[@id='snize-option-selector-1']/option")
            variants_first_components_dropdown = browser.find_element_by_id("snize-option-selector-1")
            variants_second_components_dropdown = browser.find_element_by_id("snize-option-selector-2")
            variants_second_components = browser.find_elements_by_xpath("//select[@id='snize-option-selector-2']/option")

            if (len(variants) == 2):

                if (len(variants_first_components) > 1 and len(variants_second_components) > 1):

                    browser.find_element_by_xpath("//select[@id='snize-option-selector-1']").click()
                    initial_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                    dropdown = Select(variants_first_components_dropdown)
                    dropdown.select_by_index(1)
                    dropdown = Select(variants_second_components_dropdown)
                    dropdown.select_by_index(1)



                    quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                    browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                    helper.wait()
                    cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                    assert quick_view_product_price == cart_product_price
                    browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                    helper.wait_small()
                    checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                    assert checkout_cart_total in quick_view_product_price



                elif (len(variants_first_components) == 1 and len(variants_second_components) > 1):
                   initial_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                   dropdown = Select(variants_second_components_dropdown)
                   dropdown.select_by_index(1)
                   quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                   browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                   helper.wait()
                   cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                   assert quick_view_product_price == cart_product_price
                   browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                   helper.wait_small()
                   checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                   assert checkout_cart_total in quick_view_product_price

                elif (len(variants_first_components) > 1 and len(variants_second_components) == 1):
                   # initial_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                   browser.find_element_by_xpath("//select[@id='snize-option-selector-1']").click()
                   dropdown = Select(variants_first_components_dropdown)
                   dropdown.select_by_index(1)

                   quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                   browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                   helper.wait()
                   cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                   assert quick_view_product_price == cart_product_price
                   browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                   helper.wait_small()
                   checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                   assert checkout_cart_total in quick_view_product_price

                else:
                   helper.wait()
                   assert helper.is_element_present_by_xpath(locators.quick_view_product_title_xpath)
                   assert helper.is_element_present_by_xpath(locators.quick_view_add_to_cart_xpath)
                   quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                   browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                   helper.wait()
                   cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                   assert quick_view_product_price == cart_product_price
                   browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                   helper.wait_small()
                   checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                   assert checkout_cart_total in quick_view_product_price

        except ElementNotInteractableException: #when the product is sold out
            browser.get("https://www.distacart.com/collections/snacks")
            helper.wait()
            browser.find_element_by_xpath("//a[@href='https://www.distacart.com/collections/snacks/products/vellanki-chegodi-small?lshst=collection']//div[@class='snize-item clearfix snize-stock-status-showed']//span[@class='snize-overhidden']//button[@class='snize-button snize-action-button snize-quick-view-button'][normalize-space()='Quick view']").click()
            helper.wait()
            assert helper.is_element_present_by_xpath(locators.quick_view_product_title_xpath)
            assert helper.is_element_present_by_xpath(locators.quick_view_add_to_cart_xpath)
            quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
            browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
            helper.wait()
            cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
            assert quick_view_product_price == cart_product_price
            browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
            helper.wait_small()
            checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            assert checkout_cart_total in quick_view_product_price








        except NoSuchElementException:
            variants_first_components = browser.find_elements_by_xpath("//select[@id='snize-option-selector-1']/option")
            variants_first_components_dropdown = browser.find_element_by_id("snize-option-selector-1")

            if(len(variants_first_components) > 1):
                browser.find_element_by_xpath("//select[@id='snize-option-selector-1']").click()
                dropdown = Select(variants_first_components_dropdown)
                dropdown.select_by_index(1)

                quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                helper.wait()
                cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                assert quick_view_product_price == cart_product_price
                browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                helper.wait_small()
                checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                assert checkout_cart_total in quick_view_product_price

            else:
                helper.wait()
                assert helper.is_element_present_by_xpath(locators.quick_view_product_title_xpath)
                assert helper.is_element_present_by_xpath(locators.quick_view_add_to_cart_xpath)
                quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
                browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
                helper.wait()
                cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
                assert quick_view_product_price == cart_product_price
                browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
                helper.wait_small()
                checkout_cart_total = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
                assert checkout_cart_total in quick_view_product_price









