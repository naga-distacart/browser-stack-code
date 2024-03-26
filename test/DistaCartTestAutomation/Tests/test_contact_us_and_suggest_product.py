# import re

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from DistaCartTestAutomation.Pages.homePage import HomePage
# from DistaCartTestAutomation.Pages.productPage import ProductPage
# from DistaCartTestAutomation.Locators.locators import Locators as locators
# from DistaCartTestAutomation.Helpers.helper import Helper
# import time
# import pytest
# import random


# class TestContactUsAndSuggestProduct:

#     def test_contact_us_and_suggest_product(self, browser):
#         homepage = HomePage(browser)
#         helper = Helper(browser)
#         homepage.go_to_home_page()
#         WebDriverWait(browser, 60).until(
#                 EC.presence_of_element_located((By.XPATH, locators.home_button_xpath))
#         )
#         assert helper.is_element_present_by_xpath(locators.suggest_a_product_homepage)
#         browser.find_element_by_xpath(locators.suggest_a_product_homepage).click()
#         WebDriverWait(browser, 60).until(
#             EC.presence_of_element_located((By.XPATH, locators.suggest_product_page_title))
#         )
#         #assert helper.is_element_present_by_xpath(locators.suggest_product_page_element_cs)
#         assert helper.is_element_present_by_xpath(locators.suggest_a_product_page_element_name)
#         assert helper.is_element_present_by_xpath(locators.send_button)
#         browser.find_element_by_xpath(locators.home_button_xpath).click()
#         WebDriverWait(browser, 60).until(
#             EC.presence_of_element_located((By.XPATH, locators.suggest_a_product_homepage))
#         )
#         contact_us = browser.find_element_by_xpath(locators.contact_us_link)
#         browser.execute_script("arguments[0].scrollIntoView();", contact_us)
#         browser.execute_script("arguments[0].click();", contact_us)
#         helper.wait()
#         WebDriverWait(browser, 60).until(
#             EC.presence_of_element_located((By.XPATH, locators.contact_us_page_title))
#         )
#         assert helper.is_element_present_by_xpath(locators.contact_us_page_email)
#         assert helper.is_element_present_by_xpath(locators.send_button)
