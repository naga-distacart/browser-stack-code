from selenium import webdriver
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Locators.locators import Locators as locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Helper():

    def __init__(self, driver):
        self.driver = driver

    def get_correct_link(self, link):
        link = self.driver.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        return link

    def is_element_present_by_xpath(self, item):
        return self.driver.find_element_by_xpath(item).is_displayed()

    def get_elements_by_xpath(self, ele_xpath):
        return self.driver.find_elements_by_xpath(ele_xpath)

    def navigate_back(self):
        self.driver.back()
        self.wait()

    def wait(self):
        time.sleep(30)

    def wait_small(self):
        time.sleep(15)

    def move_to_element(self, item):
        #ActionChains(self.driver).move_to_element(item).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", item)

    def click_on_element(self, item):
        self.driver.execute_script("arguments[0].click();", item)

    def set_currency(self, currency):
        self.wait()
        element = WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((By.XPATH, locators.Currency_select))
        )
        select_currency = self.driver.find_element_by_xpath(locators.Currency_select)

        select_currency.click()
        #select_currency = Select(self.driver.find_element_by_id(locators.currency_select_id))
        #select_currency.select_by_visible_text(currency.upper())
        self.driver.find_element_by_xpath(locators.currency_select_xpath_CS.format(currency.upper())).click()

    def click_load_more(self):
        load_more = self.driver.find_element_by_xpath(locators.load_more_button_xpath)
        if self.is_element_present_by_xpath(locators.load_more_button_xpath):
            self.driver.execute_script("arguments[0].click();", load_more)
            #self.move_to_element(self.driver.find_element_by_xpath(locators.load_more_button_xpath))
            #self.driver.find_element_by_xpath(locators.load_more_button_xpath).click()

    def set_input_text(self, item, text):
        if self.is_element_present_by_xpath(item):
            self.driver.find_element_by_xpath(item).clear()
            self.driver.find_element_by_xpath(item).send_keys(text)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def close_discount_popup(self):
        if self.is_element_present_by_xpath(locators.discount_popup_xpath):
            self.driver.find_element_by_xpath(locators.discount_popup_xpath).click()

    def close_product_popup(self):
        if self.is_element_present_by_xpath("//a[@class='cc-close first']"):
            self.driver.find_element_by_xpath("//a[@class='cc-close first']").click()


