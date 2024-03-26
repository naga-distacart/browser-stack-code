from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random


class TestBlogPage:

    def test_blog_page(self, browser):
        helper = Helper(browser)
        helper.navigate_to_url("https://www.distacart.com/blogs/learn")
        try:
            WebDriverWait(browser, 40).until(
                EC.element_to_be_clickable(
                    (By.XPATH, locators.blog_next_button_xpath))
            )
        except TimeoutException:
            print("INFO: Blog page is not loaded within expected time of 40 secs")

        print("INFO: Click on next button in blog page")
        next_page = browser.find_element_by_xpath(locators.blog_next_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", next_page)
        browser.execute_script("arguments[0].click();", next_page)
        helper.wait()
        url = browser.current_url
        assert 'page=2' in url

        WebDriverWait(browser, 40).until(
            EC.element_to_be_clickable(
                (By.XPATH, locators.blog_prev_button_xpath))
        )
        print("INFO: Click on previous button in blog page")
        previous_page = browser.find_element_by_xpath(locators.blog_prev_button_xpath)
        browser.execute_script("arguments[0].scrollIntoView();", previous_page)
        browser.execute_script("arguments[0].click();", previous_page)
        helper.wait()
        url = browser.current_url
        assert 'page=1' in url

        blog_items = helper.get_elements_by_xpath(locators.blog_read_more_button_xpath)
        print("INFO: Blog items found in 1st page are : ", len(blog_items))
        selected_element = random.choice(blog_items)
        product = selected_element.text
        print("INFO: Randomly selected blog : ", product)
        helper.move_to_element(selected_element)
        print("INFO: Click on Read more button of blog")
        helper.click_on_element(selected_element)
        helper.wait()
        print("INFO: Verify blog page of product is opened successfully")
        url = browser.current_url
        assert "True" == str(helper.is_element_present_by_xpath("//li[@class='breadcrumbs__item']/a[@aria-current='page']"))
