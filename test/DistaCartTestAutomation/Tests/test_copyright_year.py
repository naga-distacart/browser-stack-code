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


class TestCopyrightYear:

    @pytest.mark.sanityH
    def test_Copy_Right_Year(self, browser):
        copy_right=browser.find_element_by_xpath(locators.copy_right_info_xpath)
        ActionChains(browser).move_to_element(copy_right).perform()
        today= datetime.date.today()
        year=today.strftime("%Y")
        assert year in copy_right.text
