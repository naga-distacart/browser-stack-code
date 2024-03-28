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


class TestCategoryFood():

    @pytest.mark.sanityH
    def test_category_food_available(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        #homepage.go_to_home_page()
        #main_menu = locators.mega_menu_xpath.format("Food")
        #browser.find_element_by_xpath("//div[@class='main-nav__wrapper']/div/div[contains(@class,'mega-menu')]/div[@class='dropdown menu']/div/div/a[text()='Food']").click()
        #homepage.click_on_shop_by_categories_menu("snacks")
        helper.navigate_to_url("https://www.distacart.com/collections/snacks")
        #homepage.click_on_sub_menu("Food", "snacks")
        helper.wait()
        print("INFO: Verifying category page title...Food")
        helper.wait()
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
        test=browser.find_elements_by_xpath(locators.product_category_title.format("Snacks"))
        assert test!=0

        no_of_items = 1
        while (no_of_items <= 1):
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format("Foods"))
            print("INFO: Available items found in 1st page of Food category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            #available_product = browser.find_element_by_xpath(locators.product_xpath.format(product))
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            helper.wait()
            WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, locators.buy_with_shop_pay))
            )
            print("INFO: Verify Add to cart button is displayed for available item : ", product)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            print("INFO: Verify Buy it now button is displayed for available item : ", product)
            assert helper.is_element_present_by_xpath(locators.buy_with_shop_pay)
            no_of_items += 1
            helper.navigate_back()
            #helper.click_load_more()
            helper.wait()
            available_items = []

    @pytest.mark.sanityH
    def test_category_food_sold(self, browser):
        homepage = HomePage(browser)
        helper = Helper(browser)
        link=browser.current_url
        #homepage.go_to_home_page()
        #main_menu = locators.mega_menu_xpath.format("Food")
        #browser.find_element_by_xpath("//div[@class='main-nav__wrapper']/div/div[contains(@class,'mega-menu')]/div[@class='dropdown menu']/div/div/a[text()='Food']").click()
        #homepage.click_on_shop_by_categories_menu("snacks")
        helper.navigate_to_url("https://www.distacart.com/collections/dress-material")
        #homepage.click_on_sub_menu("Food", "snacks")
        helper.wait()
        print("INFO: Verify Food category page title")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Dress Material"))
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
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        browser.get(link+"/products/jompers-women-red-beige-printed-a-line-kurta-jok-1054-red")
        helper.wait()
        browser.find_element_by_xpath(locators.product_notify_button_xpath).click()
        time.sleep(9)
        browser.switch_to.frame('cmessage_bis_iframe')
        time.sleep(3)
        helper.wait()
        length=browser.find_elements_by_xpath(locators.notify_button_xpath1)
        assert len(length)>0
