import random
import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from DistaCartTestAutomation.Helpers.helper import Helper
from DistaCartTestAutomation.Locators.locators import Locators as locators

from DistaCartTestAutomation.Pages.homePage import HomePage


class TestViewFullCart:

    def test_promobanner_overlapping_viewfullcart(self, browser):
        helper = Helper(browser)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        helper.wait_small()
        print("INFO: Checking for Most popular section---------------------------")
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        actions = ActionChains(browser)
        popular_titles = browser.find_elements_by_xpath(locators.most_popular_section_product_title_xpath)

        if (len(popular_titles) > 0):
            # Select one element randomly from the list
            random_integer = random.randint(0, len(popular_titles) - 1)

            random_element = popular_titles[random_integer]

            random_add_to_cart_xpathappeneder = "(//*[contains(text(),'Products')]/following-sibling::div/div/ul/li//*[text()='+ Add to cart'])[{}]"
            time.sleep(30)
            random_add_to_cart_xpath = browser.find_element_by_xpath(
                random_add_to_cart_xpathappeneder.format(random_integer))

            ActionChains(browser).move_to_element(random_add_to_cart_xpath).perform()
            ActionChains(browser).move_to_element(random_add_to_cart_xpath).click().perform()
        variant_text = browser.find_elements_by_xpath(locators.most_popular_section_product_variants_xpath)
        if (len(variant_text) > 0):
            helper.wait_small()
            browser.find_element_by_xpath(locators.most_popular_section_product_variants_xpath).click()
        time.sleep(30)
        helper.wait_small()
        browser.find_element_by_xpath(locators.view_full_cart_link)
        assert helper.is_element_present_by_xpath(locators.view_full_cart_link)

        mini_cart_close_xpath = "//*[@class='close_mini_cart ls-is-cached lazyloaded']"
        helper.wait()
        browser.find_element_by_xpath(mini_cart_close_xpath).click()
        helper.wait()
        browser.find_element_by_xpath(locators.my_cart_button_xpath).click()
        helper.wait()
        assert helper.is_element_present_by_xpath(locators.view_full_cart_link)
        browser.find_element_by_xpath(locators.view_full_cart_link).click()

        browser.get("https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")
        helper.wait()
        time.sleep(30)
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
        browser.switch_to.default_content()

        browser.find_element_by_xpath(locators.my_cart_button_xpath).click()
        helper.wait()
        assert helper.is_element_present_by_xpath(locators.view_full_cart_link)
        browser.find_element_by_xpath(locators.cart_popup_product_remove_icon).click()

        helper.wait()
        # browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        helper.wait_small()
        add_to_cart = browser.find_element_by_xpath(locators.add_to_cart_product_page)
        ActionChains(browser).move_to_element(add_to_cart).perform()
        ActionChains(browser).move_to_element(add_to_cart).click().perform()
        helper.wait_small()
        browser.find_element_by_xpath(mini_cart_close_xpath).click()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
        helper.wait()
        browser.find_element_by_xpath(locators.my_cart_button_xpath).click()
        helper.wait_small()
        browser.find_element_by_xpath(locators.product_page_price_xpath)
        product_page_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
        print(product_page_price)
        mini_cart_price = browser.find_element_by_xpath(locators.cart_popup_total_xpath).text
        print(mini_cart_price)
        assert product_page_price == mini_cart_price
        helper.wait_small()
        assert helper.is_element_present_by_xpath(locators.view_full_cart_link)
        browser.find_element_by_xpath(locators.view_full_cart_link).click()
        helper.wait_small()
        full_cart_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
        assert product_page_price == mini_cart_price == full_cart_price
