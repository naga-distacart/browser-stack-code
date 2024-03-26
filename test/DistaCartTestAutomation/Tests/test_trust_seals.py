from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

class TestTrustSeals:

    def test_trust_seals(self, browser):
        category = "Ayurveda"

        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
        print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
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
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        # product_titles = browser.find_elements_by_xpath(locators.all_products_in_collection_page_title)
        product_titles = browser.find_elements_by_xpath(locators.all_products_in_collection_page_title)
        if product_titles:
            # Generate a random index within the range of elements
            random_index = random.randint(0, len(product_titles) - 1)

            # Access the element at the random index
            random_product = product_titles[random_index]

            # Perform a click operation on the randomly selected product
            ActionChains(browser).move_to_element(random_product).click().perform()
        else:
            print("No elements found for the given XPath.")

        # Trust Seals Icons for product page, minicart and checkout page

        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.product_page_sslsecure_xpath)))
        helper.wait()
        assert helper.is_element_present_by_xpath(locators.product_page_sslsecure_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.product_page_Authentic_xpath)))
        assert helper.is_element_present_by_xpath(locators.product_page_Authentic_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.product_page_Guaranteed_xpath)))
        assert helper.is_element_present_by_xpath(locators.product_page_Guaranteed_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.product_page_easy_xpath)))
        assert helper.is_element_present_by_xpath(locators.product_page_easy_xpath)
        print("trust seals of product page are displayed")

        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.add_to_cart_product_page)))
        browser.find_element_by_xpath(locators.add_to_cart_product_page).click()
        helper.wait()
        # WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.minicart_secure_xpath)))
        # assert helper.is_element_present_by_xpath(locators.minicart_secure_xpath)
        # WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.minicart_authentic_xpath)))
        # assert helper.is_element_present_by_xpath(locators.minicart_authentic_xpath)
        # WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.minicart_guaranteed_xpath)))
        # assert helper.is_element_present_by_xpath(locators.minicart_guaranteed_xpath)
        # print("trust seals of minicart  are displayed")

        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.cart_popup_checkout_xpath)))
        browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
        helper.wait()
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.checkoutPage_fast_shipping_xpath)))
        assert helper.is_element_present_by_xpath(locators.checkoutPage_fast_shipping_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.checkoutPage_safe_checkout_xpath)))
        assert helper.is_element_present_by_xpath(locators.checkoutPage_safe_checkout_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.checkoutPage_customer_support_xpath)))
        assert helper.is_element_present_by_xpath(locators.checkoutPage_customer_support_xpath)
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, locators.checkoutPage_no_custom_duties_xpath)))
        assert helper.is_element_present_by_xpath(locators.checkoutPage_no_custom_duties_xpath)
        print("trust seals of checkout page are displayed")
