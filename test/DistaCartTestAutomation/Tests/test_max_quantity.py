from selenium import webdriver
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


class TestProductMaxQuantity:

    def test_product_max_quantity(self, browser):
        category = "Ayurveda"
        max_quantity = "1000"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        no_of_items = 1
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
        helper.wait_small()
        while no_of_items <= 1:
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            element = WebDriverWait(browser, 45).until(
                EC.element_to_be_clickable((By.XPATH, locators.add_to_cart_button_xpath))
            )
            """print("INFO: Enter max quantity of product as : ", max_quantity)
            helper.set_input_text(locators.quantity_input_xpath, max_quantity)
            browser.find_element_by_xpath(locators.quantity_input_xpath).send_keys(Keys.TAB)"""
            #helper.wait()
            print("INFO: Click on add to cart button : ", product)
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            #browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            """WebDriverWait(browser, 45).until(
                EC.visibility_of_element_located((By.XPATH, locators.max_quantity_msg_xpath))
            )
            max_quantity_msg = browser.find_element_by_xpath(locators.max_quantity_msg_xpath).text
            print("INFO: Max quantity allowed message {} is displayed".format(max_quantity_msg))
            assert 0 == max_quantity_msg.find("You can order maximum upto")
            max_quantity = max_quantity_msg.split(" ")[5]
            print("INFO: Max quantity allowed for {} is {}".format(product, max_quantity))"""
            #helper.set_input_text("//input[@data-cart-quantity-input='mini-cart']", 999)
            browser.find_element_by_xpath("//input[@data-cart-quantity-input='mini-cart']").click()
            #browser.find_element_by_xpath("//input[@data-cart-quantity-input='mini-cart']").clear()
            browser.find_element_by_xpath("//input[@data-cart-quantity-input='mini-cart']").send_keys(999)
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            """max_quantity_msg = browser.find_element_by_xpath(locators.max_quantity_msg_xpath).text
            print("INFO: Max quantity allowed message {} is displayed".format(max_quantity_msg))
            assert 0 == max_quantity_msg.find("You can order maximum upto")
            max_quantity = max_quantity_msg.split(" ")[5]
            print("INFO: Max quantity allowed for {} is {}".format(product, max_quantity))"""
            max_quantity = browser.find_element_by_xpath("//input[@data-cart-quantity-input='mini-cart']").get_attribute("value")
            print("INFO: Total items displayed in cart : ", cart_count)
            assert max_quantity == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.navigate_to_url("https://www.distacart.com/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.cart_item_price))
            )
            browser.find_element_by_xpath(locators.cart_quantity_plus_button_xpath).click()
            assert helper.is_element_present_by_xpath(locators.cart_max_quantity_msg_xpath)
            cart_max_quantity_msg = browser.find_element_by_xpath(locators.cart_max_quantity_msg_xpath).text
            assert max_quantity + " items left" == cart_max_quantity_msg
            no_of_items += 1
            available_items = []
