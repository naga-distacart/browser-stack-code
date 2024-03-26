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


class TestGuestCheckOut:

    def test_guest_checkout(self, browser):
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
        no_of_items = 1
        while no_of_items <= 1:
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            helper.wait()
            print("INFO: Click on add to cart button : ", product)
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.navigate_to_url("https://www.distacart.com/cart")
            element = WebDriverWait(browser, 45).until(
                EC.presence_of_element_located((By.NAME, locators.checkout_button_id))
            )

            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            cart_item_price = browser.find_element_by_xpath(locators.cart_item_price).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))

            # click on checkout button in cart page
            print("INFO: Click on Checkout button")
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            items_in_checkout_page = browser.find_element_by_xpath(locators.checkout_item_count_xpath).text
            print("INFO: Total items displayed in checkout page : ", items_in_checkout_page)
            assert '1' == items_in_checkout_page
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert cart_item_price == checkout_total_price.strip()+ " " + checkout_total_currency
            no_of_items += 1
            available_items = []
        #Checking the checout page flows
        WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,locators.checkout_breadcrumb_information_xpath)))
        browser.find_element_by_xpath(locators.checkout_information_email).send_keys("nagadineshsunku@gmail.com")
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_information_first_name).send_keys("random")
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_information_last_name).send_keys("random")
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_information_address).send_keys("Tes")
        time.sleep(6)
        browser.find_element_by_xpath(locators.checkout_information_address).send_keys(Keys.ENTER)
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_information_phone).send_keys("16502530000")
        ActionChains(browser).move_to_element(browser.find_element_by_xpath(locators.checkout_continue_shipping_button_xpath)).perform()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_continue_shipping_button_xpath).click()
        WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,locators.checkout_continue_payment_button_xpath)))
        browser.find_element_by_xpath(locators.checkout_continue_payment_button_xpath).click()
        shipping_completed=browser.find_elements_by_xpath(locators.checkout_shipping_completed)
        assert len(shipping_completed)>0
        time.sleep(5)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[2])
        time.sleep(5)
        card_num=browser.find_element_by_xpath(locators.checkout_payment_credit_card)
        ActionChains(browser).move_to_element(card_num).perform()
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_payment_credit_card).send_keys("4024")
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_payment_credit_card).send_keys("0071")
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_payment_credit_card).send_keys("2203")
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_payment_credit_card).send_keys("1858")
        time.sleep(3)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[3])
        time.sleep(3)
        name=browser.find_element_by_xpath(locators.checkout_Name_on_the_card)
        time.sleep(2)
        ActionChains(browser).move_to_element(name).perform()
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_Name_on_the_card).send_keys("Test")
        time.sleep(3)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[4])
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_exp_date).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_exp_date).send_keys("06")
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_exp_date).send_keys("25")
        time.sleep(3)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[5])
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_security_code).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_security_code).send_keys("276")
        time.sleep(5)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_pay_now_button).click()
        helper.wait()
        card_is_wrong=browser.find_elements_by_xpath(locators.checkout_card_is_wrong)
        time.sleep(3)
        assert len(card_is_wrong)>0






    def test_guest_cart_popup_checkout(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"
        no_of_items = 1
        while no_of_items <= 1: 
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            helper.wait()
            print("INFO: Click on add to cart button : ", product)
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()

            # mouse hover on cart link to open the cart popup
            #cart_link = browser.find_element_by_xpath(locators.cart_link_xpath)
            #ActionChains(browser).move_to_element(cart_link).perform()
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                print("Inside if loop")
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()

            # element = WebDriverWait(browser, 45).until(
            #     EC.presence_of_element_located((By.XPATH, locators.cart_popup_order_notes_xpath))
            # )
            # browser.find_element_by_xpath(locators.cart_popup_order_notes_xpath).click()
            browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            items_in_checkout_page = browser.find_element_by_xpath(locators.checkout_item_count_xpath).text
            print("INFO: Total items displayed in checkout page : ", items_in_checkout_page)
            assert '1' == items_in_checkout_page
            no_of_items += 1
            available_items = []
