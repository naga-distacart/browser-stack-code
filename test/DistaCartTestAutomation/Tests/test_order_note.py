from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
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



class TestOrderNote:
    def test_order_note(self, browser):
        helper = Helper(browser)
        helper.wait()
        browser.find_element_by_xpath("//li[@class='wellness-menu-item']//a[normalize-space()='Wellness']").click()
        time.sleep(4)
        # browser.get("https://www.distacart.com/products/patanjali-hridyamrit-vati-extra-power?variant=42225200398495")
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


        helper.wait_small()
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
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()

        try:
            helper.is_element_present_by_xpath(locators.cart_popup_order_notes_xpath)
            print("oredr note is presented in mini cart")
            assert 1 != 1

        except NoSuchElementException:
            browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
            element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath)))
            element = WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, locators.cart_popup_order_notes_xpath)))
            assert helper.is_element_present_by_xpath(locators.cart_popup_order_notes_xpath)
            browser.find_element_by_xpath(locators.cart_popup_order_notes_xpath).click()
            browser.find_element_by_xpath(locators.cart_popup_order_notes_xpath).send_keys("Writting the note from QA Team, Thank you.")










