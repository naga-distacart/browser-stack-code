from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Pages.productPage import ProductPage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest

import random


# Automation script for displaying product recommendation sections on product page
class TestProductRecommendationOnProductPage:

    def test_product_url_currency(self, browser):
        supported_currencies = ["USD", "CAD", "AUD", "GBP", "EUR", "SGD", "CHF", "SEK", "NZD", "MXN", "AED",
                                "MYR", "ZAR", "IDR", "JPY", "QAR", "KRW", "PHP", "MMK", "MUR", "TTD", "DKK",
                                "ETB", "TWD", "VND", "NOK", "PLN"]
        currency = random.choice(supported_currencies)
        homepage = HomePage(browser)
        helper = Helper(browser)
        helper.set_currency(currency)
        helper.navigate_to_url(
            "https://www.distacart.com/products/nuts-for-us-iranian-mamra-almonds?variant=42278028902559&currency=" + str(currency) + "&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping")
        element = WebDriverWait(browser, 60).until(
            EC.visibility_of_element_located((By.XPATH, locators.product_page_price_xpath))
        )
        product_page_price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
        print("INFO: Currency symbol displayed in product page : ", product_page_price)
        assert currency in product_page_price








