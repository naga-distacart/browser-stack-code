from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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


class TestJudgemeBottomReviews:
    def test_judgeme_bottom_reviews(self,browser):
        helper=Helper(browser)
        helper.set_currency("AED")
        helper.wait()
        judgeme_img=browser.find_element_by_xpath(locators.judge_me_reviews_bottom_img)
        browser.execute_script("arguments[0].scrollIntoView();",judgeme_img)
        time.sleep(9)
        left_arrow= browser.find_element_by_xpath(locators.judge_me_reviews_bottom_left_arrow)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
        time.sleep(3)
        ActionChains(browser).move_to_element(left_arrow).click().perform()
        time.sleep(3)
        browser.execute_script("arguments[0].click();",judgeme_img)
        link=browser.current_url
        assert "ae" in link
