import time

import pytest

from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import re


class TestCompareAtPriceCheck:

    @pytest.mark.sanityH
    def test_compare_at_price_check(self, browser):
        helper = Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/collections/toys-games/products/sardar-ji-ki-dukan-ratnas-mandala-art-a-perfect-colouring-kit-for-all-ages-multicolour")
        helper.wait()
        time.sleep(6)
        popup = browser.find_elements_by_xpath("//*[@id='cmessage_form_iframe']")
        if (len(popup) > 0):
            browser.switch_to.frame("cmessage_form_iframe")
            # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
            try:
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            except:
                helper.wait()
                No_thanks = browser.find_elements_by_xpath("//*[text()='No Thanks']")
            if (len(No_thanks) > 0):
                # print(len(browser.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
                browser.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        current_price=browser.find_element_by_xpath(locators.current_product_price_xpath).text
        compare_at_price=browser.find_element_by_xpath(locators.compare_at_price_product_xpath).text
        current_price_e=re.sub("[^0123456789\.]","",current_price)
        current_price_e=current_price_e.split(' ')
        compare_at_price_e=re.sub("[^0123456789\.]","",compare_at_price)
        compare_at_price_e = compare_at_price_e.split(' ')
        if(float(current_price_e[0]) < float(compare_at_price_e[0])):
            assert 0==0
        else:
            assert 0==1
        savings=browser.find_element_by_xpath(locators.savings_line_xpath).text
        assert "You Save " in savings




