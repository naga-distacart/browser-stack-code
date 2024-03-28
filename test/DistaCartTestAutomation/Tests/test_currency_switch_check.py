import datetime
import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random
import DistaCartTestAutomation.Tests.conftest as c


class TestCurrencySwitchCheck:
        #Checks the currency is same when we launch website in particular VPN

    @pytest.mark.sanityH
    def test_currency_switch_check_US(self, browser):
        print("INFO: Checking the currency list is switching to right currency")
        helper = Helper(browser)
        # currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
        #            "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
        #            "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
        #            "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
        #            "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
        # print("\n")
        # print(currency[c.location])
        helper.wait()
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'USD')
        print("Actual:", currency_text)
        assert 'United States (USD)' == currency_text
        browser.find_element(By.XPATH,locators.home_button_xpath).click()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'United States (USD)')
        print("Actual:", currency_text)
        assert 'United States (USD)' == currency_text
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.scrolled_down_home_button).click()
        helper.wait()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        assert 'United States (USD)' == currency_text



    @pytest.mark.sanityH
    def test_currency_switch_check_AU(self, browser):
        helper = Helper(browser)
        print("INFO: Checking the currency list is switching to right currency")
        # currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
        #            "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
        #            "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
        #            "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
        #            "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
        # print("\n")
        # print(currency[c.location])
        helper.wait()
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'AUD')
        print("Actual:", currency_text)
        assert "Australia (AUD)" == currency_text
        browser.find_element(By.XPATH,locators.home_button_xpath).click()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'Australia (AUD)')
        print("Actual:", currency_text)
        assert "Australia (AUD)" == currency_text
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.scrolled_down_home_button).click()
        helper.wait()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        assert 'Australia (AUD)' == currency_text


    @pytest.mark.sanityH
    def test_currency_switch_check_CA(self, browser):
        print("INFO: Checking the currency list is switching to right currency")
        helper = Helper(browser)
        # currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
        #            "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
        #            "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
        #            "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
        #            "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
        # print("\n")
        # print(currency[c.location])
        helper.wait()
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'Canada (CAD)')
        print("Actual:", currency_text)
        assert "Canada (CAD)" == currency_text
        browser.find_element(By.XPATH,locators.home_button_xpath).click()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'Canada (CAD)')
        print("Actual:", currency_text)
        assert "Canada (CAD)" == currency_text
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.scrolled_down_home_button).click()
        helper.wait()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        assert 'Canada (CAD)' == currency_text

    @pytest.mark.sanityH
    def test_currency_switch_check_NL(self, browser):
        print("INFO: Checking the currency list is switching to right currency")
        helper = Helper(browser)
        # currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
        #            "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
        #            "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
        #            "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
        #            "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
        # print("\n")
        # print(currency[c.location])
        helper.wait()
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'EUR')
        print("Actual:", currency_text)
        assert "Netherlands (EUR)" == currency_text
        browser.find_element(By.XPATH,locators.home_button_xpath).click()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'Netherlands (EUR)')
        print("Actual:", currency_text)
        assert 'Netherlands (EUR)' == currency_text
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.scrolled_down_home_button).click()
        helper.wait()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        assert 'Netherlands (EUR)' == currency_text

    @pytest.mark.sanityH
    def test_currency_switch_check_GB(self, browser):
        print("INFO: Checking the currency list is switching to right currency")
        helper = Helper(browser)
        # currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
        #            "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
        #            "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
        #            "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
        #            "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
        # print("\n")
        # print(currency[c.location])
        helper.wait()
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'GBP')
        print("Actual:", currency_text)
        assert 'United Kingdom (GBP)' == currency_text
        browser.find_element(By.XPATH,locators.home_button_xpath).click()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        print("Expected:", 'United Kingdom (GBP)')
        print("Actual:", currency_text)
        assert 'United Kingdom (GBP)' == currency_text
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        browser.find_element_by_xpath(locators.scrolled_down_home_button).click()
        helper.wait()
        print("INFO: LOGO Clicked")
        WebDriverWait(browser, 260).until(EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
        currency_text = browser.find_element_by_xpath(locators.Currency_select).text
        assert 'United Kingdom (GBP)' == currency_text
