from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random

class TestOrderWithInFeature:

    def test_order_with_in_feature(self, browser):
        helper = Helper(browser)
        helper.wait()
        # browser.find_element_by_xpath(locators.spirituality_xpath).click()
        browser.find_element_by_xpath("//li[@class='wellness-menu-item']//a").click()
        time.sleep(4)
        #browser.get("https://www.distacart.com/collections/wellness/products/himalaya-liv-52-tablets-100-counts?variant=14282611032109")

        # browser.find_element_by_xpath("//a[@href='/collections/snacks/products/nature-land-organics-dry-amla-candy-sweet']//div[@class='snize-item clearfix snize-stock-status-showed']//span[@class='snize-overhidden']//button[@class='snize-button snize-action-button snize-quick-view-button'][normalize-space()='Quick view']").click()
        helper.wait_small()
        selected_product_name = ""
        product_titles = browser.find_elements_by_xpath("//span[@class='snize-title']")
        if product_titles:
            # Generate a random index within the range of elements
            random_index = random.randint(0, len(product_titles) - 1)

            # Access the element at the random index
            random_product = product_titles[random_index]
            selected_product_name = random_product.text

            # Perform a click operation on the randomly selected product
            #browser.execute_script("arguments[0].scrollIntoView();", random_product)
            time.sleep(6)
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

        product_name = browser.find_element_by_xpath(locators.product_tile_name).text

        assert selected_product_name in product_name

        assert helper.is_element_present_by_xpath(locators.delivery_time_xpath)
        assert helper.is_element_present_by_xpath(locators.i_icon_xpath)
        assert helper.is_element_present_by_xpath(locators.order_with_in_xpath)
        i_icon = browser.find_element_by_xpath(locators.i_icon_xpath)
        ActionChains(browser).move_to_element(i_icon).perform()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//img[@class='delivery_by_tooltip']")))
        element = browser.find_element_by_xpath("//img[@class='delivery_by_tooltip']")
        prop_value = element.get_attribute("style")
        print(prop_value)
        assert prop_value == "display: inline;"




        order_with_in_days = browser.find_elements_by_xpath(locators.order_with_in_days_xpath)
        days_list = []
        formatted_result = ""

        for order_with_in_days in order_with_in_days:
            days_list.append(order_with_in_days.text)

        if len(days_list) == 2:
            final_days = days_list[0] + '-' + days_list[1]
            split_result = final_days.split('.')
            formatted_result = split_result[0]
            print(formatted_result)
        else:
            print("Not enough elements in the list to combine.")

        shipping_table_name = browser.find_element_by_xpath(locators.shipping_box_title)

        browser.execute_script("arguments[0].scrollIntoView();", shipping_table_name)
        time.sleep(3)
        shipping_progress_days = browser.find_element_by_xpath("//div[@class='delivery_date deliverydate']").text

        assert formatted_result in shipping_progress_days
