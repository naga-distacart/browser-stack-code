import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers.helper import Helper
from DistaCartTestAutomation.Locators.locators import Locators as locators
import time



class TestCheckFulfillmentError:
    # Description:Checking for the product card attributes in all pages
    @pytest.mark.sanityH
    def test_check_fulfillment_count_error_limespot(self, browser):
        helper = Helper(browser)
        #Checking from limespot
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        link=browser.current_url
        WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,locators.most_popular_section_product_title_xpath)))
        product_titles=browser.find_elements_by_xpath(locators.most_popular_section_product_title_xpath)
        helper.get_correct_link(link)
        browser.get(link+"/products/isha-life-neem-and-turmeric-capsules")
        WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,locators.add_to_cart_product_page)))
        browser.find_element_by_xpath(locators.add_to_cart_product_page).click()
        WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,locators.cart_popup_product_title_xpath)))
        fulfillment_error=browser.find_elements_by_xpath(locators.cart_pop_up_fulfillment_error)
        assert len(fulfillment_error)==0
        print("INFO: Asserted Fulfillment Error is not shown")
        #Checking in full cart
        browser.get("https://www.distacart.com/cart")
        fulfillment_error = browser.find_elements_by_xpath(locators.cart_pop_up_fulfillment_error)
        assert len(fulfillment_error) == 0
        print("INFO: Asserted Fulfillment Error is not shown in Full cart")
    @pytest.mark.sanityH
    def test_check_fulfillment_count_error_search(self, browser):
        #checking from search
        browser.switch_to.default_content()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, locators.search_text_box_xpath)))
        browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys("Isha Life Neem and Turmeric Capsules")
        time.sleep(2)
        browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(Keys.ENTER)
        WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,locators.search_product_title)))
        product_titles=browser.find_elements_by_xpath(locators.search_product_title)
        #Looping all the products in search products
        for product_title in product_titles:
            if(product_title.text=="Isha Life Neem and Turmeric Capsules"):
                ActionChains(browser).move_to_element(product_title).click().perform()
                break
        WebDriverWait(browser, 70).until(EC.presence_of_element_located((By.XPATH, locators.add_to_cart_product_page)))
        browser.find_element_by_xpath(locators.add_to_cart_product_page).click()
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, locators.cart_popup_product_title_xpath)))
        fulfillment_error = browser.find_elements_by_xpath(locators.cart_pop_up_fulfillment_error)
        assert len(fulfillment_error) == 0
        # Checking in full cart
        browser.get("https://www.distacart.com/cart")
        fulfillment_error = browser.find_elements_by_xpath(locators.cart_pop_up_fulfillment_error)
        assert len(fulfillment_error) == 0
        print("INFO: Asserted Fulfillment Error is not shown")


