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


class TestSpellingMistake:

    def test_spelling_mistake(self, browser):
        referral=browser.find_element_by_xpath(locators.referral_program)
        ActionChains(browser).move_to_element(referral).perform()
        text=browser.find_element_by_xpath(locators.referral_program).text
        assert text=="Referral program"