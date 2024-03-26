

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper

import time

import random


class TestNonUsaCustomersCheckout:

    def test_non_usa_customer_checkout(self, browser):
        helper = Helper(browser)
        helper.wait_small()
        no_of_items = 1
        current_url = browser.current_url
        actions = ActionChains(browser)
        Explore_top_categories = browser.find_element_by_xpath(locators.Explore_top_categories_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", Explore_top_categories)
        top_categories_collections = browser.find_elements_by_xpath(locators.top_categories_collections_xpath)

        # selecting random category from explore top categories section
        if top_categories_collections:
            random_index = random.randint(0, len(top_categories_collections) - 1)
            if random_index == 2:
                random_index += 1

            # Access the element at the random index
            random_product = top_categories_collections[random_index]
            print(random_product.text)
            actions.move_to_element(random_product).click().perform()

        else:

            print("No elements found for the given XPath.")

        helper.wait_small()
        first_navigation_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in first_navigation_url
        all_banners = browser.find_elements_by_xpath("//div[@class='pf-c']/div/img")
        if all_banners:
            random_index = random.randint(16, 23)
            # Access the element at the random index
            random_product = all_banners[random_index]
            browser.execute_script("arguments[0].scrollIntoView(true);", random_product)
            time.sleep(10)
            random_product.click()

        else:

            print("No elements found for the given XPath.")

        time.sleep(4)
        second_navigation_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in second_navigation_url

        #selecting one product randomly
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

        helper.wait_small()

        quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
        assert "CAD" in quick_view_product_price
        browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
        helper.wait_small()
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
        time.sleep(3)
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        assert quick_view_product_price == cart_product_price
        browser.find_element_by_xpath(locators.cart_minus_button_xpath).click()
        time.sleep(3)
        browser.execute_script("window.scrollTo(0, 0);")
        #browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath("//li[@class='wellness-menu-item']//a").click()
        time.sleep(3)
        home_products = browser.find_elements_by_css_selector("span[class='snize-overhidden']")
        home_product_price = ""

        if home_products:
            random_index = random.randint(0, len(quick_views) - 1)

            # Access the element at the random index
            random_product = home_products[random_index]
            print(random_product.text)
            home_product_title1 = random_product.find_element_by_css_selector("span[class='snize-overhidden'] span[class='snize-title']")
            print(home_product_title1.text)
            home_product_price = random_product.find_element_by_css_selector("span[class='snize-overhidden'] div[class='snize-price-list'] span[class*='snize-price']").text

            ActionChains(browser).move_to_element(home_product_title1).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView(true);", random_product)
            # time.sleep(2)
            # home_product_title1.click()
            #WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='snize-overhidden'] span[class='snize-title']")))
            #actions.move_to_element(random_product).perform()


        else:

            print("No elements found for the given XPath.")

        product_page_price = browser.find_element_by_xpath(locators.product_price_xpath).text
        assert product_page_price == home_product_price
        product_current_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in product_current_url
        product_item = browser.find_element_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", product_item)
        assert helper.is_element_present_by_xpath(locators.add_to_cart_button_xpath)
        browser.execute_script("arguments[0].click();", product_item)
        helper.wait()
        element = WebDriverWait(browser, 85).until(
            EC.presence_of_element_located((By.XPATH, locators.cart_popup_checkout_xpath)))
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
        # browser.back()
        helper.wait()
        # Checking the checkout page flows

        WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, locators.checkout_breadcrumb_information_xpath)))
        helper.wait_small()
        country_currency = browser.find_element_by_xpath("//td[@class='total-line__price payment-due']/span[@class='payment-due__currency remove-while-loading']").text
        assert "CAD" == country_currency
        browser.find_element_by_xpath(locators.checkout_information_email).send_keys("test@gmail.com")



        browser.find_element_by_xpath(locators.checkout_information_first_name).send_keys("Test")
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_information_last_name).send_keys("test")
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_information_address).send_keys("Tes")
        time.sleep(6)
        browser.find_element_by_xpath(locators.checkout_information_address).send_keys(Keys.ENTER)
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_information_phone).send_keys("3333333333")
        ship_button = browser.find_element_by_xpath(locators.checkout_continue_shipping_button_xpath)
        ActionChains(browser).move_to_element(ship_button).click().perform()
        helper.wait_small()
        WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH, locators.checkout_continue_payment_button_xpath)))
        ship_button = browser.find_element_by_xpath(locators.checkout_continue_shipping_button_xpath)
        ActionChains(browser).move_to_element(ship_button).click().perform()
        time.sleep(9)
        country_currency = browser.find_element_by_xpath("//td[@class='total-line__price payment-due']/span[@class='payment-due__currency remove-while-loading']").text
        assert "CAD" == country_currency
        shipping_completed = browser.find_elements_by_xpath(locators.checkout_shipping_completed)
        time.sleep(9)
        # assert len(shipping_completed) > 0
        time.sleep(5)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        length = browser.find_elements_by_xpath(locators.checkout_shipping_text)
        browser.switch_to.frame(browser.find_elements_by_xpath("//*[@class='card-fields-iframe']")[0])
        time.sleep(5)
        card_num = browser.find_element_by_xpath(locators.checkout_payment_credit_card)
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
        browser.switch_to.frame(browser.find_elements_by_xpath("//*[@class='card-fields-iframe']")[1])
        time.sleep(3)
        name = browser.find_element_by_xpath(locators.checkout_Name_on_the_card)
        time.sleep(2)
        ActionChains(browser).move_to_element(name).perform()
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_Name_on_the_card).send_keys("Test")
        time.sleep(3)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.switch_to.frame(browser.find_elements_by_xpath("//*[@class='card-fields-iframe']")[2])
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_exp_date).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_exp_date).send_keys("06")
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_exp_date).send_keys("25")
        time.sleep(3)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.switch_to.frame(browser.find_elements_by_xpath("//*[@class='card-fields-iframe']")[3])
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_security_code).click()
        time.sleep(2)
        browser.find_element_by_xpath(locators.checkout_security_code).send_keys("276")
        time.sleep(5)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_continue_payment_button_xpath).click()
        helper.wait()
        card_is_wrong = browser.find_elements_by_xpath(locators.checkout_card_is_wrong)
        time.sleep(3)
        assert len(card_is_wrong) > 0
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath(locators.checkout_logo).click()
        time.sleep(3)
        browser.find_element_by_xpath("//li[@class='athleisure-wear-menu-item']/a").click()
        time.sleep(3)
        first_navigation_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in first_navigation_url
        browser.find_element_by_xpath("//div[@class='top-bar']//div//img[@alt='Distacart']").click()
        browser.find_element_by_xpath(locators.my_cart_button_xpath).click()
        time.sleep(3)
        browser.find_element_by_xpath(locators.cart_minus_button_xpath).click()
        time.sleep(3)
        Explore_top_categories = browser.find_element_by_xpath(locators.Explore_top_categories_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", Explore_top_categories)
        time.sleep(3)
        browser.find_element_by_xpath("//strong[normalize-space()='Wellness']").click()
        second_navigation_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in second_navigation_url

        # selecting one product randomly
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

        helper.wait_small()
        quick_view_product_price = browser.find_element_by_xpath(locators.quick_view_product_price_xpath).text
        assert "CAD" in quick_view_product_price
        quick_view_quantity = browser.find_element_by_xpath("//input[@id='snize-quick-view-quantity']")
        quick_view_quantity.click()
        quick_view_quantity.clear()
        quick_view_quantity.send_keys("3")
        browser.find_element_by_xpath(locators.quick_view_add_to_cart_xpath).click()
        helper.wait_small()
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print(cart_product_price)
        print(quick_view_product_price)
        mini_cart_product_price = quick_view_product_price.split(" CAD")
        mini_cart_price = mini_cart_product_price[0]
        mini_cart_price1 = mini_cart_price.split("$")
        mini_cart_price2 = mini_cart_price1[1]
        print(mini_cart_price2)
        final_product_price = float(mini_cart_price2) * 3
        print(final_product_price)
        rounded_number = round(final_product_price, 2)
        print(rounded_number)
        assert str(rounded_number) in cart_product_price
        browser.find_element_by_xpath("//div[@class='item_title']/a").click()
        cur_url = browser.current_url
        assert "https://www.distacart.com/en-ca" in cur_url



