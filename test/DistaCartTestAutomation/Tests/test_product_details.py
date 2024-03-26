from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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


class TestProductDetails:

    def test_product_tile_info(self, browser):
        category = "Ayurveda"
        homepage = HomePage(browser)
        helper = Helper(browser)
        homepage.click_on_shop_by_categories_menu(category)
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
        helper.set_currency("CAD")
        print("INFO: Verifying category page title...Ayurvedic Products Online")
        assert helper.is_element_present_by_xpath(locators.product_category_title.format("Ayurvedic Products Online"))
        helper.wait()
        # assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_thumbnail_xpath))
        assert 0 != len(helper.get_elements_by_xpath(locators.product_name_xpath))
        assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_stars_badge_xpath))
        assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_stars_xpath))
        qa_icon=browser.find_elements_by_xpath(locators.product_tile_qa_icon_xpath)
        if(len(qa_icon)>0):
            assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_qa_icon_xpath))
        qa_text=browser.find_elements_by_xpath(locators.product_tile_qa_text_xpath)
        if(len(qa_text)>0):
            assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_qa_text_xpath))
        assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_reviews_display_xpath))
        assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_price_xpath))
        category = "Patanjali"
        no_of_items = 1
        while no_of_items <= 1:
            available_items = helper.get_elements_by_xpath(locators.product_available_xpath.format(category))
            print("INFO: Available items found in 1st page of " + category + " category : ", len(available_items))
            selected_element = random.choice(available_items)
            product = selected_element.text
            print("INFO: Randomly selected available product : ", product)
            helper.move_to_element(selected_element)
            helper.click_on_element(selected_element)
            element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath))
            )
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
            assert 0 != len(helper.get_elements_by_xpath(locators.product_fulfilled_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.product_detail_star_badges_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.product_detail_stars_xpath))
            qa_icon = browser.find_elements_by_xpath(locators.product_tile_qa_icon_xpath)
            if (len(qa_icon) > 0):
                assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_qa_icon_xpath))
            qa_text = browser.find_elements_by_xpath(locators.product_tile_qa_text_xpath)
            if (len(qa_text) > 0):
                assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_qa_text_xpath))

            # Validate customers who bought this item also bought elements
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(4)
            browser.refresh()
            helper.wait()
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(4)
            cbb_product_item = browser.find_element_by_xpath(locators.cbb_product_image_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", cbb_product_item)
            assert 0 != len(helper.get_elements_by_xpath(locators.cbb_product_image_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.cbb_product_name_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.cbb_product_variant_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.cbb_product_price_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.cbb_product_add_to_cart_xpath))
            cbb_currency = browser.find_element_by_xpath(locators.cbb_product_price_xpath).text
            assert "CAD" in cbb_currency

            # Validate related items elements
            related_product_item = browser.find_element_by_xpath(locators.related_product_thumbnail_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", related_product_item)
            assert 0 != len(helper.get_elements_by_xpath(locators.related_product_thumbnail_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.related_product_name_xpath))
            # assert 0 != len(helper.get_elements_by_xpath(locators.related_product_stars_badge_xpath))
            # assert 0 != len(helper.get_elements_by_xpath(locators.related_product_stars_xpath))
            #assert 0 != len(helper.get_elements_by_xpath(locators.related_product_qa_icon_xpath))
            #assert 0 != len(helper.get_elements_by_xpath(locators.related_product_qa_text_xpath))
            # assert 0 != len(helper.get_elements_by_xpath(locators.product_tile_reviews_display_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.related_product_price_xpath))
            related_product_currency = browser.find_element_by_xpath(locators.related_product_price_xpath).text
            assert "CAD" in related_product_currency

            # Validate recently viewed items elements
            """search_product = "kaju rolls"
            search_product_xpath = locators.product_xpath.format("Vellanki Foods - Kaju Rolls")
            homepage = HomePage(browser)
            homepage.search_product(search_product, search_product_xpath)
            recent_product_item = browser.find_element_by_xpath(locators.recent_product_thumbnail_xpath)
            browser.execute_script("arguments[0].scrollIntoView();", recent_product_item)
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_thumbnail_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_name_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_stars_badge_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_stars_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_qa_icon_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_qa_text_xpath))
            assert 0 != len(helper.get_elements_by_xpath(locators.recent_product_price_xpath))
            recent_product_currency = browser.find_element_by_xpath(locators.recent_product_price_xpath).text
            assert "CAD" in recent_product_currency"""
            no_of_items += 1

    def default_product_for_variant_title_king(self, browser):
        helper = Helper(browser)
        product_names_list = ["Ensure Diabetes Care Powder Vanilla Flavour -Refill - 200 gm", "Ensure Diabetes Care Powder Vanilla Flavour -Refill - 400 gm", "Ensure Diabetes Care Powder Vanilla Flavour -Refill - 1 kg", "Ensure Diabetes Care Powder Vanilla Flavour -Jar - 400 gm"]
        browser.switch_to.default_content()
        browser.find_element_by_xpath("//div[@class='main-nav__wrapper']//div[@class='search-container']//input[@placeholder='Search']").click()
        time.sleep(10)
        browser.find_element_by_xpath("//div[@class='main-nav__wrapper']//div[@class='search-container']//input[@placeholder='Search']").send_keys('Ensure Diabetes Care Powder Vanilla Flavour - Refill - 200 gm')
        time.sleep(10)
        browser.find_element_by_xpath("//div[@class='main-nav__wrapper']//div[@class='search-container']//span[@class='icon-search search-submit']").click()
        time.sleep(20)
        products = browser.find_elements_by_xpath(locators.all_products_in_collection_page_title)
        for product in products:
            product_title = product.text
            if (product_title == "Ensure Diabetes Care Powder Vanilla Flavour"):
                product.find_element_by_xpath("//*[@class='snize-title']").click()
                break
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
                browser.find_element_by_xpath("//*[text()='No Thanks']").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()
        helper.wait()
        product_name = browser.find_element_by_xpath("//h1[@class='product_name']").text
        assert product_name in product_names_list
        title1_200gm_url = browser.current_url
        browser.find_element_by_xpath("//label[@for='swatch-1-400-gm-5316513071263-product-template']").click()
        product_name = browser.find_element_by_xpath("//h1[@class='product_name']").text
        print(product_name)
        title1_400_gm_url = browser.current_url
        assert product_name in product_names_list
        # assert title1_200gm_url != title1_400_gm_url
        browser.find_element_by_xpath("//label[@for='swatch-1-1-kg-5316513071263-product-template']").click()
        product_name = browser.find_element_by_xpath("//h1[@class='product_name']").text
        print(product_name)
        title1_1_kg_url = browser.current_url
        assert product_name in product_names_list
        # assert title1_1_kg_url != title1_200gm_url != title1_400_gm_url
        browser.find_element_by_xpath("//label[@for='swatch-0-jar-5316513071263-product-template']").click()
        browser.find_element_by_xpath("//label[@for='swatch-1-400-gm-5316513071263-product-template']").click()
        product_name = browser.find_element_by_xpath("//h1[@class='product_name']").text
        title2_400_gm_url = browser.current_url
        assert product_name in product_names_list
        # assert title2_400_gm_url != title1_1_kg_url

        assert title1_200gm_url != title1_400_gm_url and title1_200gm_url != title1_1_kg_url and title1_400_gm_url != title1_1_kg_url
        assert title2_400_gm_url != title1_200gm_url and title2_400_gm_url != title1_400_gm_url and title2_400_gm_url != title1_1_kg_url


    def test_product_variant_details(self, browser):
        helper = Helper(browser)
        helper.wait()
        browser.find_element_by_xpath("//li[@class='wellness-menu-item']//a[normalize-space()='Wellness']").click()
        time.sleep(4)
        #browser.get("https://www.distacart.com/products/patanjali-hridyamrit-vati-extra-power?variant=42225200398495")
        product_titles = browser.find_elements_by_xpath(locators.all_products_in_collection_page_title)
        if product_titles:
            # Generate a random index within the range of elements
            random_index = random.randint(0, len(product_titles) - 1)

            # Access the element at the random index
            random_product = product_titles[random_index]

            # Perform a click operation on the randomly selected product
            ActionChains(browser).move_to_element(random_product).click().perform()
        else:
            print("No elements found for the given XPath.")

        helper.wait()
        helper.wait()
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
                browser.find_element_by_xpath("//*[text()='No Thanks']").click()
                browser.switch_to.default_content()
        browser.switch_to.default_content()

        # Find all product variant elements
        product_variants = browser.find_elements_by_xpath("//*[contains(@class,'swatch-element')]/label")

        if len(product_variants) <= 1:
            # Navigate to another URL if product variants are less than or equal to 1
            self.default_product_for_variant_title_king(browser)

        else:
            initial_title = browser.find_element_by_xpath("//h1[@class='product_name']").text
            initial_url = browser.current_url
            initial_price = browser.find_element_by_css_selector("div[class='price__container price__container--display-price-true has-margin-right'] span[class='money']").text
            non_blue_variants = []
            blue_variants = []
            variant_list = []

            for variant in product_variants:
                if variant.value_of_css_property('color') == "rgba(255, 255, 255, 1)":
                    blue_variants.append(variant)

                elif variant.value_of_css_property('color') == "rgba(63, 79, 232, 1)":
                    non_blue_variants.append(variant)

                else:
                    variant_list.append(variant)


            print("non blue")
            print(len(non_blue_variants))
            print(len(blue_variants))
            print(len(variant_list))

            for variant in non_blue_variants:
                variant.click()

                # Grab product name, price, and URL
                product_name = browser.find_element_by_xpath("//div[@class='one-half columns medium-down--one-whole product-section__right']/h1").text
                # product_price = browser.find_element_by_css_selector("div[class='price__container price__container--display-price-true has-margin-right'] span[class='money']").text
                product_url = browser.current_url
                #price_element = browser.find_element_by_css_selector("div[class='price__container price__container--display-price-true has-margin-right'] span[class='money']")

                try:
                    #product_name = browser.find_element_by_xpath("//div[@class='one-half columns medium-down--one-whole product-section__right']/h1").text
                    product_price = browser.find_element_by_css_selector("div[class='price__container price__container--display-price-true has-margin-right'] span[class='money']").text
                    #product_url = browser.current_url
                    helper.wait()
                    browser.find_element_by_css_selector("div[class='price__container price__container--display-price-true has-margin-right'] span[class='money']")

                    updated_product_tile1 = product_name
                    assert initial_title != updated_product_tile1
                    assert initial_url != product_url
                    updated_price = product_price
                    assert initial_price != updated_price

                    # Update initial values for the next iteration
                    initial_title = updated_product_tile1
                    initial_url = browser.current_url
                    initial_price = updated_price

                except NoSuchElementException:
                    self.default_product_for_variant_title_king(browser)
                    break



