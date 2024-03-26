# -*- coding: utf-8 -*-
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
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


class TestBssTags:
    def test_bss_tags(self, browser):
        helper = Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/collections/dista-pick/products/mamaearth-onion-hair-oil-with-onion-oil-redensyl-for-hair-fall-control")
        helper=Helper(browser)
        helper.wait()
        dista_pick_label=browser.find_elements_by_xpath(locators.dista_picks_label_xpath)
        assert len(dista_pick_label)>0
        helper.get_correct_link(link)
        browser.get(link+"/products/a2b-adyar-ananda-bhavan-hand-murukku")
        helper.wait()
        best_seller_label=browser.find_elements_by_xpath(locators.best_seller_label_xpath)
        assert len(best_seller_label)>0
        helper.get_correct_link(link)
        browser.get(link+"/products/abbott-similac-neosure-for-premature-baby-born-before-37-weeks")
        helper.wait()
        text_label=browser.find_elements_by_xpath(locators.text_label_xpath)
        assert len(text_label)>0
