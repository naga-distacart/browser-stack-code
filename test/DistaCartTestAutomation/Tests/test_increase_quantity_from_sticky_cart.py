from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from DistaCartTestAutomation.Pages.collectionPage import CollectionPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import random


class TestIncreaseQuantityFromStickyCart:

    def test_increase_quantity_from_sticky_cart(self, browser):
        helper = Helper(browser)
        current_url = browser.current_url
        collection_page = CollectionPage(browser)
        brand_and_brand_partners = browser.find_elements_by_xpath(locators.brand_and_brand_partners_xpath)

        if brand_and_brand_partners :
            random_index = random.randint(0, len(brand_and_brand_partners)-1)

            random_brand_partner = brand_and_brand_partners[random_index]

            brand_names = browser.find_element_by_xpath("//h2[normalize-space()='NOTABLE BRAND PARTNERS']")

            browser.execute_script("arguments[0].scrollIntoView(true);", brand_names)
            time.sleep(3)
            ActionChains(browser).move_to_element(random_brand_partner).click().perform()

        else:
            print("no xpath matching to brands")

        #selecting random product from the collection
        collection_page.closing_discount_usd_pop_up()
        collection_page.select_random_product_from_collection(current_url)
        helper.wait_small()
        browser.execute_script("window.scrollTo(0, 600);")
        time.sleep(3)
        for _ in range(15):
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)

        #closing the pop-up
        collection_page.closing_discount_usd_pop_up()
        time.sleep(3)
        sticky_add_cart_product_price = browser.find_element_by_xpath(locators.sticky_add_cart_product_price_xpath).text
        collection_product_price = collection_page.collection_product_price
        assert sticky_add_cart_product_price == collection_product_price
        #increasing the quantity
        for _ in range(4):
            browser.find_element_by_xpath(locators.sticky_cart_increase_quantity_xpath).click()

        sticky_add_to_cart_quantity = browser.find_element_by_xpath(locators.sticky_quantity_input_xpath).text
        browser.find_element_by_xpath(locators.sticky_add_cart_xpath).click()
        helper.wait_small()
        product_quantity_in_mini_cart = browser.find_element_by_xpath(locators.cart_input_quantity_xpath).text
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        assert sticky_add_to_cart_quantity == product_quantity_in_mini_cart
        product_currency = sticky_add_cart_product_price.split(" USD")
        increase_quantity = 5
        decrease_quantity = 3
        collection_page.actual_product_price(product_currency[0], increase_quantity)
        assert str(collection_page.rounded_number) in cart_product_price
        browser.find_element_by_xpath(locators.mini_cart_delete_xpath).click()
        helper.wait_small()
        #decreasing the quantity
        for _ in range(2):
            browser.find_element_by_xpath(locators.sticky_cart_decrease_quantity_xpath).click()

        browser.find_element_by_xpath(locators.sticky_add_cart_xpath).click()
        helper.wait_small()
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        collection_page.actual_product_price(product_currency[0], decrease_quantity)
        assert str(collection_page.rounded_number) in cart_product_price
        browser.find_element_by_xpath(locators.mini_cart_delete_xpath).click()
        helper.wait_small()
        input_quantity = 2
        #Clearing the existing quantity and giving input quantity in quantity field in the sticky add to cart
        browser.find_element_by_xpath(locators.sticky_quantity_input_xpath).clear()
        browser.find_element_by_xpath(locators.sticky_quantity_input_xpath).send_keys(input_quantity)
        browser.find_element_by_xpath(locators.sticky_add_cart_xpath).click()
        helper.wait_small()
        collection_page.actual_product_price(product_currency[0], input_quantity)
        sticky_add_to_cart_quantity = browser.find_element_by_xpath(locators.sticky_quantity_input_xpath).text
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        assert str(collection_page.rounded_number) in cart_product_price
        browser.find_element_by_xpath(locators.view_full_cart_link).click()
        helper.wait_small()
        main_cart_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
        main_cart_quantity = browser.find_element_by_xpath(locators.full_cart_quantity_edit).text
        assert main_cart_price == cart_product_price
        assert main_cart_quantity == sticky_add_to_cart_quantity
        browser.find_element_by_id(locators.checkout_button_id).click()
        checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
        assert checkout_total_price in main_cart_price
        browser.find_element_by_xpath(locators.checkout_logo).click()
        browser.find_element_by_xpath(locators.my_cart_button_xpath).click()
        helper.wait_small()
        browser.find_element_by_xpath(locators.cart_popup_checkout_xpath).click()
        checkout_total_price = browser.find_element_by_xpath(locators.checkout_page_total_price_xpath).text
        assert checkout_total_price in main_cart_price
