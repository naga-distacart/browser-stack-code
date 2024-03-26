from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import pytest
import random

class TestLimespotReviews:

    def test_limespot_reviews(self, browser):
        # Home page
        # checking add to cart functionality in Most Popular pages---------------------------------------------------------
        helper=Helper(browser)
        link=browser.current_url
        print("INFO: Checking for Most popular section---------------------------")
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        most_xpath = browser.find_elements_by_xpath(locators.most_popular_section_xpath)
        if (len(most_xpath) > 0):
            assert len(most_xpath)>0
        else:
            trend_xpath = browser.find_elements_by_xpath(locators.trending_section_xpath)
            ActionChains(browser).move_to_element(trend_xpath[0]).perform()
            print("")
        helper.wait()

        # Random Reviews click
        browser.refresh()
        helper.wait()
        reviews = browser.find_elements_by_xpath(locators.most_popular_section_product_reviews_xpath)
        ActionChains(browser).move_to_element(reviews[0]).perform()
        time.sleep(3)
        # ActionChains(browser).context_click(reviews[0]).perform()
        time.sleep(3)
        Num_of_reviews = reviews[1].text
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(2)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(2)
        ActionChains(browser).move_to_element(reviews[1]).perform()

        helper.wait()
        reviews[1].click()
        helper.wait()
        current_url=browser.current_url
        assert current_url!=link
        helper.wait()
        judgeme=browser.find_element_by_xpath(locators.judge_me_text).text
        assert Num_of_reviews in judgeme
        helper.get_correct_link(link)
        browser.get(link+"/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")
        helper.wait()
        questions=browser.find_element_by_xpath(locators.product_questions_xpath).text
        ActionChains(browser).move_to_element(browser.find_element_by_xpath(locators.judge_me_questions_number)).perform()
        time.sleep(4)
        questions_judge_me_number=browser.find_element_by_xpath(locators.judge_me_questions_number).text
        assert questions_judge_me_number in questions


