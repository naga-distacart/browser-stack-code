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


class TestShippingProgress:

    def test_shipping_progress(self, browser):
        country = {"US": "United States", "JP": "Japan", "AU": "Australia", "GB": "United Kingdom", "AE": "UAE", "CA": "Canada","CH": "Switzerland","CZ": "Czech","DK": "Denmark","NL": "Netherlands", "HK": "Hong Kong","HU": "Hungary","ID": "Indonesia", "IL": "Israel", "MT": "Malta", "NO": "Norway", "NZ": "New Zealand","PH": "Philippines", "PL": "Poland","QA": "Qatar","SA": "Saudi Arabia", "SG": "Singapore","TW": "Taiwan", "VN": "Vietnam","ZA": "South Africa","AR":"Argentina","RO":"Romania","PE":"Peru"}
        with open("./../Data/shipping.json") as jsonFile:
            supported_countries = json.load(jsonFile)
            countries_json = json.dumps(supported_countries)
            countries = json.loads(countries_json)
            print("\n")
            print(country[c.location])
            print(countries[country[c.location]]['fastest shipping method'])
            shipping_method=countries[country[c.location]]['fastest shipping method']
            print(countries[country[c.location]]['shipping rates'][shipping_method]['min delivery days'])
            print(countries[country[c.location]]['shipping rates'][shipping_method]['max delivery days'])
            min_delivery_days=countries[country[c.location]]['shipping rates'][shipping_method]['min delivery days']
            max_delivery_days=countries[country[c.location]]['shipping rates'][shipping_method]['max delivery days']

            browser.get("https://www.distacart.com/pages/brands")
            WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                browser.get("https://www.distacart.com/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            brand_product_titles[random_num].click()
            WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,locators.add_to_cart_product_page)))
            fastest_shipping_text=browser.find_element_by_xpath(locators.fastest_shipping_text_product_page_xpath)
            ready_to_ship_text=browser.find_element_by_xpath(locators.ready_to_ship_text_product_page).text
            import re
            s=re.sub("[^0123456789\-]","",ready_to_ship_text)
            s=str(s)
            ActionChains(browser).move_to_element(fastest_shipping_text).perform()

            def date_by_adding_business_days(from_date, add_days):
                business_days_to_add = add_days
                current_date = from_date
                while business_days_to_add > 0:
                    current_date += datetime.timedelta(days=1)
                    weekday = current_date.weekday()
                    if weekday >= 5:  # sunday = 6
                        continue
                    business_days_to_add -= 1
                return current_date
            order_date_expected = datetime.datetime.now().strftime("%b" + " %-d")
            order_date_actual=browser.find_element_by_xpath(locators.order_date_product_page_xpath).text
            print("INFO:Asserting the order dates")
            print("exp:"+order_date_expected)
            print("Actual:"+order_date_actual)
            assert order_date_expected==order_date_actual
            ship_progress_min_ship_date=date_by_adding_business_days(datetime.date.today(), int(s[0])).strftime("%b" + " %-d")
            ship_progress_max_ship_date=date_by_adding_business_days(datetime.date.today(), int(s[2])).strftime("%b" + " %-d")
            prdct_pge_shipping_dates_expected=ship_progress_min_ship_date+"-"+ship_progress_max_ship_date

            prdct_pge_shipping_dates_actual=browser.find_element_by_xpath(locators.shipping_dates_product_page).text
            print("INFO:Asserting the shipping date")
            print("exp:"+prdct_pge_shipping_dates_expected)
            print("Actual:"+prdct_pge_shipping_dates_actual)
            assert prdct_pge_shipping_dates_expected==prdct_pge_shipping_dates_actual

            print("INFO:Asserting the delivery dates")
            ship_progress_min_delivery_date = date_by_adding_business_days(date_by_adding_business_days(datetime.date.today(), int(s[0])), min_delivery_days).strftime("%b" + " %-d")
            ship_progress_max_delivery_date = date_by_adding_business_days(date_by_adding_business_days(datetime.date.today(), int(s[2])), max_delivery_days).strftime("%b" + " %-d")
            prdct_pge_delivery_dates_expected = ship_progress_min_delivery_date + "-" + ship_progress_max_delivery_date
            prdct_pge_delivery_dates_actual = browser.find_element_by_xpath(locators.delivery_dates_product_page).text
            print("exp:"+prdct_pge_delivery_dates_expected)
            print("Actual:"+prdct_pge_delivery_dates_actual)
            assert prdct_pge_delivery_dates_expected == prdct_pge_delivery_dates_actual




