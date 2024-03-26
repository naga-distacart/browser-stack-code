import datetime
import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random
import DistaCartTestAutomation.Tests.conftest as c


class TestPriceMismatchForGoogleAds:

    def test_price_mismatch(self, browser):
        print("INFO:Checking the landing page when given currency parameter")
        helper=Helper(browser)
        currencies=["AED","AUD","CAD","CHF","CZK","DKK","ETB","GBP","HKD","HUF","IDR","ILS","JPY","KRW","MMK","MUR","MYR","NOK","NZD","PHP","PLN","QAR","SAR","SGD","TTD","TWD","USD","VND","ZAR","ARS"]
        for currency in currencies:
            browser.get("https://www.distacart.com/en-{}".format((currency[:2].lower())))
            helper.wait()
            currency_text=browser.find_element_by_xpath(locators.Currency_select).text
            print("Expected:",currency)
            print("Actual:",currency_text)
            print("----------")
            assert currency in currency_text


    def test_price_mismatch2(self,browser):
        print("INFO:Checking the landing page when given currency parameter")
        helper = Helper(browser)
        currencies = ["PEN","AOA","BSD","RON","NGN"]
        for currency in currencies:
            browser.get("https://www.distacart.com/en-{}".format((currency[:2].lower())))
            helper.wait()
            currency_text = browser.find_element_by_xpath(locators.Currency_select).text
            print("Expected:", currency)
            print("Actual:", currency_text)
            print("----------")
            assert currency in currency_text
        eur_links = ["nl", "eu", "de", "ie"]
        for eur_link in eur_links:
            browser.get("https://www.distacart.com/en-{}".format(eur_link))
            currency_text_eur = browser.find_element_by_xpath(locators.Currency_select).text
            WebDriverWait(browser, 60).until(
                EC.element_to_be_clickable((By.XPATH, locators.Currency_select)))
            print("INFO:Text added to link:", eur_link)
            print("Expected:EUR")
            print("Actual:", currency_text_eur)
            print("----------")
            assert "EUR" in currency_text_eur





