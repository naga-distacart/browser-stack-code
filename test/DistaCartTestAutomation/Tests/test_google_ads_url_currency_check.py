# import datetime
# import json

# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common import actions
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from DistaCartTestAutomation.Locators.locators import Locators as locators
# from DistaCartTestAutomation.Helpers.helper import Helper
# import time
# import pytest
# import random
# import DistaCartTestAutomation.Tests.conftest as c


# class TestGoogleAdsUrlCurrencyCheck:

#     def test_google_ads_url_currency_check(self, browser):
#         print("INFO: Checking the google ad whether it is going to the right currency as the location")
#         currency = {"US": "USD", "JP": "JPY", "AU": "AUD", "GB": "GBP", "AE": "AED",
#                    "CA": "CAD", "CH": "CHF", "CZ": "CZK", "DK": "DKK", "NL": "EUR",
#                    "HK": "HKD", "HU": "HUF", "ID": "IDR", "IL": "ILS", "NO": "NOK",
#                    "NZ": "NZD", "PH": "PHP", "PL": "PLN", "QA": "QAR", "SA": "SAR",
#                    "SG": "SGD", "TW": "TWD", "VN": "VND", "ZA": "ZAR"}
#         print("\n")
#         print(currency[c.location])
#         browser.get("https://www.google.com")
#         accept_all=browser.find_elements(By.XPATH,"//*[@class='QS5gu sy4vM']")
#         if(len(accept_all)>0):
#             accept_all[0].click()
#         browser.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Isha Life Neem and Turmeric")
#         browser.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys(Keys.ENTER)
#         WebDriverWait(browser, 30).until(EC.presence_of_element_located(((By.XPATH, "//*[@class='xSQxL HDOrGf']"))))
#         updatelocation = browser.find_element(By.XPATH, "//*[@class='xSQxL HDOrGf']")
#         ActionChains(browser).move_to_element(updatelocation).perform()
#         browser.find_element(By.XPATH,"//body").send_keys(Keys.PAGE_DOWN)
#         ActionChains(browser).move_to_element(updatelocation).click().perform()
#         WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Distacart')]")))
#         flag=0
#         current_handle=browser.current_window_handle
#         product_ads = browser.find_elements(By.XPATH,"//*[@class='top-pla-group-inner']//*[contains(@data-nt-icon-id,'planti')]/..//*[@class='LbUacb']/span")
#         product_ads_titles = browser.find_elements(By.XPATH,"//*[@class='top-pla-group-inner']//*[contains(@data-nt-icon-id,'planti')]/..//*[@class='plantl pla-unit-title-link']/span")
#         for k in range(0, len(product_ads) - 1):
#             if (product_ads[k].text == "Distacart" and product_ads_titles[k].text.__contains__("Isha Life Neem and Turmeric")):
#                 ActionChains(browser).move_to_element(product_ads_titles[k]).click().perform()
#                 flag=1
#                 break
#         if(flag==0):
#             browser.find_element(By.XPATH,"//*[contains(text(),'Distacart')]").click()
#             print("clicked")
#         all_handles=browser.window_handles
#         for handle in all_handles:
#             if(handle!=current_handle):
#                 browser.switch_to_window(handle)
#         WebDriverWait(browser,260).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-controls='currency-list']")))
#         currency_text=browser.find_element(By.XPATH,"//*[@aria-controls='currency-list']").text
#         print("Expected:",currency[c.location])
#         print("Actual:",currency_text)
#         assert currency[c.location]==currency_text
