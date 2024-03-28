from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random

class TestAddToCart:
    @pytest.mark.sanityH
    def test_add_to_cart_US(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        #homepage.go_to_home_page()
        test = browser.get_cookie('countryName')
        print(test)
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.product_category_title.format("Ayurvedic Products Online")))
        )
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            length=browser.find_element_by_xpath("//*[@class='tos_warning cart_content animated fadeIn']")
            attribute=length.get_attribute('style')
            if(attribute=="display: none;"):
                browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
                time.sleep(3)
                browser.execute_script("arguments[0].click();", product_item)
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.navigate_to_url("https://www.distacart.com/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.cart_item_price).text
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []
    @pytest.mark.sanityH
    def test_add_to_cart_CA(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link=browser.current_url
        #homepage.go_to_home_page()
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanityH
    def test_add_to_cart_AU(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link = browser.current_url
        #homepage.go_to_home_page()
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanityH
    def test_add_to_cart_GB(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link = browser.current_url
        #homepage.go_to_home_page()
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            # print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            # print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            helper.wait_small()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            # print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanityH
    def test_add_to_cart_NZ(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link = browser.current_url
        #homepage.go_to_home_page()
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanityH
    def test_add_to_cart_EU(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link = browser.current_url
        #homepage.go_to_home_page()
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
            helper.get_correct_link(link)
            browser.get(link+"/products/a-r-silk-womens-net-original-shisha-emb-golden-fancy-dupatta?variant=31593686466696")
            helper.wait()
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            # print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            # print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            # print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.replace(" ","") + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanityH
    def test_add_to_cart_SG(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        link = browser.current_url
        #homepage.go_to_home_page()
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
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
            helper.wait()
            time.sleep(6)
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                    print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count

            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.get_correct_link(link)
            helper.navigate_to_url(link+"/cart")
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, locators.full_cart_item_price))
            )
            cart_item_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price == price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanity
    @pytest.mark.sanityH
    def test_increase_quantity_from_cart_page(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        #homepage.go_to_home_page()
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
            print("INFO: Click on add to cart button : ", product)
            product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", product_item)
            assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
            price = browser.find_element_by_xpath(locators.product_price_xpath).text
            print("INFO: Verify price of {} is {}".format(product, price))
            browser.execute_script("arguments[0].click();", product_item)
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
            browser.find_element_by_xpath("//div[@class='mini-cart-header']/img").click()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            print("INFO: Total items displayed in cart : ", cart_count)
            assert '1' == cart_count
            helper.wait_small()


            # click on cart link to navigate to cart page
            #browser.find_element_by_xpath(locators.cart_link_xpath).click()
            helper.navigate_to_url("https://www.distacart.com/cart")
            element = WebDriverWait(browser, 90).until(
                EC.element_to_be_clickable((By.XPATH, locators.cart_quantity_plus_button_xpath))
            )
            browser.find_element_by_xpath(locators.cart_quantity_plus_button_xpath).click()
            helper.wait()
            cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
            cart_item_price = browser.find_element_by_xpath(locators.cart_item_price).text
            print("INFO: Total items displayed in cart after increasing the quantity by 1 : ", cart_count)
            assert '2' == cart_count
            print("INFO: Price displayed in cart page for product {} is {}".format(product, cart_item_price))
            assert cart_item_price != price

            # click on checkout button in cart page
            browser.find_element_by_name(locators.checkout_button_id).click()
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.checkout_page_total_price_xpath))
            )
            helper.wait()
            items_in_checkout_page = browser.find_element_by_xpath(locators.checkout_item_count_xpath).text
            print("INFO: Total items displayed in checkout page : ", items_in_checkout_page)
            assert '2' == items_in_checkout_page
            checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
            checkout_total_currency = browser.find_element_by_xpath(locators.checkout_page_currency_xpath).text
            print("INFO: Total price displayed in checkout page for product {} is {}".format(product, checkout_total_price))
            assert cart_item_price == checkout_total_price.strip() + " " + checkout_total_currency
            no_of_items += 1
            available_items = []

    @pytest.mark.sanity
    @pytest.mark.sanityH
    def test_free_shipping_progress_bar(self, browser):
        helper = Helper(browser)
        product = 'g-pulla-reddy-special-assorted-sweets'
        helper.navigate_to_url("https://www.distacart.com/collections/food/products/"+product)
        helper.wait()
        print("INFO: Click on add to cart button")
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        price = browser.find_element_by_xpath(locators.product_price_xpath).text
        print("INFO: Verify product price of {} is {}".format(product, price))
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        """cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
        print("INFO: Total items displayed in cart : ", cart_count)
        assert '1' == cart_count"""
        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print("INFO: Subtotal displayed in cart is : ", subtotal)
        assert '$32.35 USD' == subtotal
        free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
        helper.wait_small()
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            if (len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()

        print("INFO: Free shipping message displayed after adding {} in cart is {}".format(product,free_shipping_msg))
        assert 'Shop for $26.65 USD more for FREE SHIPPING !' in free_shipping_msg
        """free_shipping_bar_percentage = browser.find_element_by_xpath(locators.cart_free_shipping_progress_bar_xpath).text
        print("INFO: Free shipping progress bar percentage displayed after adding {} in cart is {}".format(product, free_shipping_bar_percentage))
        assert '50%' == free_shipping_bar_percentage"""
        print("INFO: Increase the product quantity from cart slider")
        browser.find_element_by_xpath(locators.cart_slider_quantity_plus_button_xpath).click()
        helper.wait_small()
        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print("INFO: Subtotal displayed in cart after increasing the product quantity for first time : ", subtotal)
        assert '$64.70 USD' == subtotal
        """free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
        print("INFO: Free shipping message displayed after increasing product quantity is : ", free_shipping_msg)
        assert 'Shop for $0.06 USD more for ' in free_shipping_msg
        free_shipping_bar_percentage = browser.find_element_by_xpath(locators.cart_free_shipping_progress_bar_xpath).text
        print("INFO: Free shipping progress bar percentage displayed after increasing product quantity is : ", free_shipping_bar_percentage)
        assert '93%' == free_shipping_bar_percentage
        browser.find_element_by_xpath(locators.cart_slider_quantity_plus_button_xpath).click()"""
        free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
        print("INFO: Free shipping unlocked message displayed after increasing product quantity is : ", free_shipping_msg)
        assert 'Congrats! You\'ve unlocked ' in free_shipping_msg
        """free_shipping_bar_percentage = browser.find_element_by_xpath(locators.cart_free_shipping_progress_bar_xpath).text
        print("INFO: Free shipping progress bar percentage after free shipping unlocked is : ", free_shipping_bar_percentage)
        assert '100%' == free_shipping_bar_percentage"""
        print("INFO: Decrease the product quantity from cart slider")
        browser.find_element_by_xpath(locators.cart_slider_quantity_minus_button_xpath).click()
        helper.wait_small()
        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print("INFO: Subtotal displayed in cart after decreasing the product quantity for 2 times : ", subtotal)
        assert '$32.35 USD' == subtotal
        free_shipping_msg = browser.find_element_by_xpath(locators.cart_free_shipping_msg_xpath).text
        print("INFO: Free shipping unlocked message displayed after decreasing product quantity 2 times is : ", free_shipping_msg)
        assert 'Shop for $26.65 USD more for FREE SHIPPING !' in free_shipping_msg
        """free_shipping_bar_percentage = browser.find_element_by_xpath(locators.cart_free_shipping_progress_bar_xpath).text
        print("INFO: Free shipping progress bar percentage after decreasing product quantity 2 times is : ", free_shipping_bar_percentage)
        assert '46%' == free_shipping_bar_percentage"""

    @pytest.mark.sanity
    @pytest.mark.sanityH
    def test_add_to_cart_from_collections_page(self, browser):
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
        helper.wait()
        product = browser.find_element_by_xpath(locators.product_available_xpath.format(category)).text
        print("INFO: Product selected is :", product)
        helper.wait()
        # select = Select(browser.find_element_by_xpath("//div[@class='purchase-details__buttons purchase-details__spb--false ']/button[@name='add']/../../../div/div/select"))
        # options = select.options

        """for element in options:
            variant_price = element.get_attribute("id")
            cleanr = re.compile('<.*?>')
            price = re.sub(cleanr, '', variant_price)
            select.select_by_visible_text(element.text)
            product_price = browser.find_element_by_xpath("//span[@class='current_price']/span").text
            print("INFO: Product variant {} price is {}".format(element.text, product_price))
            time.sleep(3)
            assert price == product_price"""
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

        product_price = browser.find_element_by_xpath(locators.collection_page_product_price_s).text
        print("INFO: Click on Add to cart on product tile in collections page")
        assert helper.is_element_present_by_xpath(
            locators.collection_page_product_add_to_cart_s.format("Isha Life Neem and Turmeric"))
        product_selected = browser.find_element_by_xpath(
            locators.collection_page_product_add_to_cart_s.format("Isha Life Neem and Turmeric"))
        browser.execute_script("arguments[0].click();", product_selected)
        helper.click_on_element(product_selected)
        helper.wait()
        product_selected = browser.find_element_by_xpath(locators.search_product_add_to_cart)
        product_selected.click()
        helper.wait()
        # browser.execute_script("arguments[0].click();", product_selected)
        # helper.wait_small()
        # browser.execute_script("arguments[0].click();", product_selected)
        browser.refresh()
        helper.wait()
        browser.find_element_by_xpath("//*[@class='top-bar--right-menu']//*[@class='icon-bag mini_cart ']").click()
        time.sleep(5)
        cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
        print("INFO: Total items displayed in cart : ", cart_count)
        assert '1' == cart_count
        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print("INFO: Subtotal displayed in cart is : ", subtotal)
        assert product_price == subtotal
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
        # time.sleep(6)
        browser.find_element_by_xpath(locators.cart_plus_button_xpath).click()
        helper.wait_small()
        cart_count = browser.find_element_by_xpath(locators.cart_count_xpath).text
        assert '2' == cart_count
        subtotal = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        assert product_price != subtotal
        browser.find_element_by_xpath("//span[@class='remove-icon']").click()
        time.sleep(5)
        browser.find_element_by_xpath("//div[@class='top-bar--right-menu']/div/a[@class='icon-bag mini_cart ']").click()
        print("INFO: Verify cart becomes empty after removing product")
        empty_cart_text = browser.find_element_by_xpath("//p[@class='empty_cart']").text
        assert empty_cart_text == 'Your Cart is Empty'
