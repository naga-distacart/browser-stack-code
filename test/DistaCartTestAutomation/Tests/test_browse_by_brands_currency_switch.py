from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import random


class TestBrowseByBrandsCurrencySwitch:
    def test_browse_by_brands_currency_switch(self,browser):
        helper = Helper(browser)
        link=browser.current_url
        helper.get_correct_link(link)
        browser.get(link+"/collections/types?q=24%20Mantra%20Organic")
        helper=Helper(browser)
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
        browser.find_element_by_xpath(locators.Currency_select).click()
        time.sleep(2)
        currencies=browser.find_elements_by_xpath(locators.Currency_select)
        num=random.randint(0,len(currencies))
        currencies[num].click()
        text=browser.find_element_by_xpath(locators.assert_shop_now_page).text
        assert text=="24 Mantra Organic"
