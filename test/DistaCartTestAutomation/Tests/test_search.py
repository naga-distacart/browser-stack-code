from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
from selenium.webdriver.support.ui import Select
import time
import pytest




class TestSearch():

        # @classmethod
        # def test_setup(self):
        #    global driver
        #    driver = webdriver.Chrome("C:/Users/xyz/PycharmProjects/DistaCartTestAutomation/DistaCartTestAutomation/Drivers/chromedriver.exe")
        #   driver.get("https://www.distacart.com/")
        #   driver.implicitly_wait(60)
        #   driver.maximize_window()

        def test_search_product(self, browser):
            search_product = "kaju rolls"
            search_product_xpath = locators.product_xpath.format("Vellanki Foods - Kaju Rolls")
            homepage = HomePage(browser)
            homepage.search_product(search_product, search_product_xpath)
            helper1 = Helper(browser)
            helper1.wait()
            popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
            if (len(popup) > 0):
                browser.switch_to.frame("cmessage_form_iframe")
                # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                try:
                    No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
                except:
                    helper1.wait()
                    No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
                if (len(No_thanks) > 0):
                    # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                    browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                    browser.switch_to.default_content()
            browser.switch_to.default_content()
            assert helper1.is_element_present_by_xpath("//h1[@class='product_name']/..//button/span[contains(text(),'Add to cart')]")
            productpage = ProductPage(browser)
            print("INFO: Verify search item {} is found with title {}".format(search_product, "Vellanki Foods - Kaju Rolls"))
            assert productpage.product_title() == "Vellanki Foods - Kaju Rolls -250 gm"
            print("INFO: Verify search item {} is sold by {}".format(search_product, "Genie India"))
            assert productpage.product_vendor() == "Genie India"

        def test_search_product_add_to_cart(self, browser):

            helper1 = Helper(browser)
            link = browser.current_url
            search_product = "kaju rolls"
            browser.implicitly_wait(90)
            browser.switch_to.default_content()
            browser.find_element_by_xpath(locators.search_textbox_xpath).click()
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(search_product)
            time.sleep(6)
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(u'\ue007')
            browser.implicitly_wait(30)
            assert helper1.is_element_present_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            quick_view = browser.find_element_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            product_price = browser.find_element_by_xpath(
                locators.search_product_price_format_xpath.format("Vellanki Foods - Kaju Rolls"))
            product_price = product_price.text
            product_selected = browser.find_element_by_xpath(
                locators.collection_page_product_add_to_cart_s.format("Vellanki Foods - Kaju Rolls"))
            browser.execute_script("arguments[0].click();", product_selected)
            helper1.click_on_element(product_selected)
            helper1.wait()
            product_selected = browser.find_element_by_xpath(locators.search_product_add_to_cart)
            product_selected.click()
            time.sleep(3)
            helper1.get_correct_link(link)
            browser.get(link+"/cart")
            helper1.wait()
            # view_cart = browser.find_element_by_xpath(locators.search_view_cart.format("Vellanki Foods - Kaju Rolls"))
            # helper1.click_on_element(view_cart)
            WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Vellanki Foods - Kaju Rolls - 250 gm']")))
            time.sleep(6)
            browser.refresh()
            helper1.wait()
            currency = browser.find_element_by_xpath(locators.Currency_select).text
            time.sleep(3)
            full_cart_price = browser.find_element(By.XPATH, locators.full_cart_item_price).text
            if(currency=='USD'):
                assert product_price  == full_cart_price
            else:
                assert product_price == full_cart_price
            time.sleep(4)
            browser.find_element_by_xpath(locators.full_cart_remove_item).click()




        def test_search_sold_out_product_add_to_cart(self, browser):
            #comments
            search_product = "ffffffff"
            browser.implicitly_wait(90)
            browser.switch_to.default_content()
            browser.find_element_by_xpath(locators.search_textbox_xpath).click()
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(search_product)
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(u'\ue007')
            browser.implicitly_wait(30)
            helper1 = Helper(browser)
            assert helper1.is_element_present_by_xpath(locators.search_empty)
            # browser.find_element_by_xpath(locators.search_instock_filter_chkbox).click()
            # assert helper1.is_element_present_by_xpath(locators.search_sold_out.format("Vellanki Foods - Mango jelly rolls"))

        def test_search_add_to_cart_variant(self, browser):
            helper = Helper(browser)
            search_product = "kaju rolls"
            link=browser.current_url
            browser.implicitly_wait(90)
            browser.switch_to.default_content()
            browser.find_element_by_xpath(locators.search_textbox_xpath).click()
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(search_product)
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(u'\ue007')
            browser.implicitly_wait(30)
            helper1 = Helper(browser)
            assert helper1.is_element_present_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            a = ActionChains(browser)
            m = browser.find_element_by_xpath("//span[text()='Vellanki Foods - Kaju Rolls']")
            # hover over element
            a.move_to_element(m).perform()
            # select = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Vellanki Foods - Kaju Rolls']/../div/div/div/select")))
            # Select(select).select_by_visible_text("1 kg")
            # search_price = browser.find_element_by_xpath("//span[text()='Vellanki Foods - Kaju Rolls']/../div[@class='snize-price-list']/span").text
            # add_to_cart = browser.find_element_by_xpath(locators.search_add_to_cart.format("Vellanki Foods - Kaju Rolls"))
            # helper1.click_on_element(add_to_cart)
            # assert helper1.is_element_present_by_xpath(locators.search_view_cart.format("Vellanki Foods - Kaju Rolls"))
            # view_cart = browser.find_element_by_xpath(locators.search_view_cart.format("Vellanki Foods - Kaju Rolls"))
            # helper1.click_on_element(view_cart)
            # WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Vellanki Foods - Kaju Rolls']")))
            # assert browser.current_url == "https://www.distacart.com/cart"
            # cart_price = browser.find_element_by_xpath("//p[@class='price_total']/span").text
            search_price=browser.find_element_by_xpath(locators.search_product_price_format_xpath.format("Vellanki Foods - Kaju Rolls")).text
            assert helper1.is_element_present_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            quick_view = browser.find_element_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            helper1.click_on_element(quick_view)
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, locators.search_product_add_to_cart)))
            time.sleep(4)
            browser.find_element_by_xpath(locators.search_product_add_to_cart).click()
            time.sleep(7)
            helper.get_correct_link(link)
            browser.get(link+"/cart")
            helper1.wait()
            time.sleep(2)
            cart_price=browser.find_element_by_xpath(locators.full_cart_item_price).text
            assert search_price in cart_price
        def test_price_check(self,browser):
            helper1 = Helper(browser)
            link = browser.current_url
            search_product = "kaju rolls"
            browser.implicitly_wait(90)
            browser.switch_to.default_content()
            browser.find_element_by_xpath(locators.search_textbox_xpath).click()
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(search_product)
            time.sleep(6)
            browser.find_element_by_xpath(locators.search_textbox_xpath).send_keys(u'\ue007')
            browser.implicitly_wait(30)
            assert helper1.is_element_present_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            quick_view = browser.find_element_by_xpath(locators.search_quick_view.format("Vellanki Foods - Kaju Rolls"))
            product_price = browser.find_element_by_xpath(
                locators.search_product_price_format_xpath.format("Vellanki Foods - Kaju Rolls"))
            product_price = product_price.text
            helper1.get_correct_link(link)
            browser.get(link+"/products/vellanki-foods-kaju-rolls")
            helper1.wait()
            product_page_price=browser.find_element_by_xpath(locators.product_page_price_xpath).text
            assert product_price==product_page_price

