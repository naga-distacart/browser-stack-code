import random
from selenium.webdriver import ActionChains
import time
from DistaCartTestAutomation.Locators.locators import Locators
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper


class CollectionPage():

    def __init__(self, driver):
        locators = Locators()
        self.driver = driver
        self.search_textbox_xpath = locators.search_textbox_xpath
        self.collection_product_price = ""
        self.rounded_number = ""

    def select_random_product_from_collection(self, current_url):
        time.sleep(3)
        actions = ActionChains(self.driver)
        collection_products = self.driver.find_elements_by_css_selector(locators.home_products_css)
        collection_product_name = ""

        if len(collection_products) > 1:

            if collection_products:
                random_index = random.randint(0, len(collection_products) - 1)

                # Access the element at the random index
                random_product = collection_products[random_index]
                print(random_product.text)
                collection_product_name = random_product.find_element_by_css_selector(locators.collection_product_name_css)
                print(collection_product_name.text)
                self.collection_product_price = random_product.find_element_by_css_selector(locators.collection_product_price_css).text
                # self.driver.execute_script("arguments[0].scrollIntoView(true);", collection_product_name)
                # time.sleep(3)
                # collection_product_name.click()

                actions.move_to_element(collection_product_name).click().perform()

            else:
                print("No elements found for the given XPath.")

        else:
            collections_list = ["/collections/pet-care", "/collections/spirituality", "/collections/books", "/collections/home-furnishing", "/collections/home-furnishing"]
            random_index = random.randint(0, len(collections_list)-1)
            collection = collections_list[random_index]
            self.driver.get(current_url+collection)
            time.sleep(3)
            if collection_products:
                random_index = random.randint(0, len(collection_products) - 1)

                # Access the element at the random index
                random_product = collection_products[random_index]
                print(random_product.text)
                collection_product_name = random_product.find_element_by_css_selector(locators.collection_product_name_css)
                print(collection_product_name.text)
                self.collection_product_price = random_product.find_element_by_css_selector(locators.collection_product_price_css).text

                actions.move_to_element(collection_product_name).click().perform()

            else:
                print("No elements found for the given XPath.")

    def actual_product_price(self, product_price_without_country_currency, multiply_count):
        actual_price = product_price_without_country_currency
        print(actual_price)
        remove_dollar = actual_price.split("$")
        actual_product_price = remove_dollar[1]
        print(actual_product_price)
        final_product_price = float(actual_product_price) * multiply_count
        print(final_product_price)
        self.rounded_number = round(final_product_price, 2)
        print(self.rounded_number)

    def closing_discount_usd_pop_up(self):
        helper = Helper(self.driver)
        helper.wait()
        time.sleep(6)
        popup = self.driver.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            self.driver.switch_to.frame("cmessage_form_iframe")
            print(len(self.driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            if (len(self.driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
                print(len(self.driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                self.driver.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
