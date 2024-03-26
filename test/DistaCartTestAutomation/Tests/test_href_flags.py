from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import random


class TestHrefFlags:
    count = 0

    def href_tags(self, browser):
        helper = Helper(browser)
        all_links = browser.find_elements_by_xpath("//link")
        for link in all_links:
            link_text = link.get_attribute("data-href")

            if link_text is not None:
                print(link)
                self.count += 1

            else:
                # Continue to the next link
                continue


    def home_page_href_tags(self, browser):
        self.href_tags(browser)

    def search_page_href_tags(self, browser):
        homepage = HomePage(browser)
        homepage.search_by_result()
        self.href_tags(browser)

    def collection_page_href_tgs(self, browser):
        category = "Unani"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
        helper.wait_small()
        self.href_tags(browser)

    def product_page_herf_tags(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        # homepage.go_to_home_page()
        test = browser.get_cookie('countryName')
        print(test)
        helper.wait()
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
        homepage.click_on_shop_by_categories_menu(category)
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        category = "Patanjali"

        available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
        print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
        selected_element = random.choice(available_items)
        product = selected_element.text
        print("INFO: Randomly selected available product : ", product)
        helper.move_to_element(selected_element)
        helper.click_on_element(selected_element)
        self.href_tags(browser)

    def check_data_href_lang_tags(self, browser):
        if self.count > 0:
            assert 1 == 0  # failing the test case intentionally

        else:
            print("there are no data-href property in the tags")

    def test_all_pages_href_lang_tags(self, browser):
        self.home_page_href_tags(browser)
        self.search_page_href_tags(browser)
        self.collection_page_href_tgs(browser)
        self.product_page_herf_tags(browser)
        self.check_data_href_lang_tags(browser)
