from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import random


class TestLimespot:

    def test_limespot_homepage(self, browser):
        helper=Helper(browser)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        print("INFO: Checking for Most popular section---------------------------")
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        most_xpath = browser.find_elements_by_xpath(locators.most_popular_section_xpath)
        if (len(most_xpath) > 0):
            ActionChains(browser).move_to_element(most_xpath[0]).perform()
        add_to_cart = browser.find_elements_by_xpath(locators.most_popular_section_add_to_cart_xpath)
        time.sleep(4)
        length = len(add_to_cart) - 1
        random_num = random.randint(1, length)
        # comment
        print(random_num)
        product_text = browser.find_elements_by_xpath(locators.most_popular_section_product_title_xpath)
        print(len(product_text))
        product_title = product_text[random_num].text
        product_prices = browser.find_elements_by_xpath(locators.most_popular_section_product_price_xpath)
        product_price = product_prices[random_num].text
        time.sleep(2)
        #browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        # ActionChains(browser).move_to_element(add_to_cart[random_num]).click().perform()
        add_to_cart[random_num].click()
        time.sleep(3)
        variant_text = browser.find_elements_by_xpath(locators.most_popular_section_product_variants_xpath)
        if (len(variant_text) > 0):
            browser.find_element_by_xpath(locators.most_popular_section_product_variants_xpath).click()
        time.sleep(3)
        product_added_from_UI_title = product_title
        time.sleep(8)
        cart_product_title = browser.find_element_by_xpath(locators.cart_popup_product_title_xpath).text
        print(product_added_from_UI_title)
        print(cart_product_title)
        assert cart_product_title.__contains__(product_added_from_UI_title)
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_product_price_xpath).text
        product_price = product_price.replace('&nbsp;', '')
        print(product_price)
        print(cart_product_price)
        assert product_price == cart_product_price
        product_quantity = browser.find_element_by_xpath(locators.cart_popup_product_quantity_xpath).get_attribute(
            "value")
        assert product_quantity == '1'
        time.sleep(4)
        browser.find_element_by_xpath(locators.cart_popup_product_remove_icon).click()
        time.sleep(7)
        browser.refresh()
        helper.wait()
        reviews=browser.find_elements_by_xpath(locators.most_popular_section_product_reviews_xpath)
        assert len(reviews)>0
        stars=browser.find_elements_by_xpath(locators.most_popular_section_product_stars_xpath)
        assert len(stars)>0
        questions=browser.find_elements_by_xpath(locators.most_popular_section_product_questions_xpath)
        assert len(questions)>0

    def test_limespot_view_full_cart(self,browser):
        helper = Helper(browser)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        print("INFO: Checking for Most popular section---------------------------")
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        most_xpath = browser.find_elements_by_xpath(locators.most_popular_section_xpath)
        if (len(most_xpath) > 0):
            ActionChains(browser).move_to_element(most_xpath[0]).perform()
        add_to_cart = browser.find_elements_by_xpath(locators.most_popular_section_add_to_cart_xpath)
        time.sleep(4)
        length = len(add_to_cart) - 1
        random_num = random.randint(1, length)
        # comment
        print(random_num)
        product_text = browser.find_elements_by_xpath(locators.most_popular_section_product_title_xpath)
        print(len(product_text))
        product_title = product_text[random_num].text
        product_prices = browser.find_elements_by_xpath(locators.most_popular_section_product_price_xpath)
        product_price = product_prices[random_num].text
        print(str(random_num)+"-------")
        print(str(product_price)+"-------")
        time.sleep(2)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        # ActionChains(browser).move_to_element(add_to_cart[random_num]).click().perform()
        time.sleep(3)
        add_to_cart[random_num].click()
        time.sleep(3)
        variant_text = browser.find_elements_by_xpath(locators.most_popular_section_product_variants_xpath)
        if (len(variant_text) > 0):
            browser.find_element_by_xpath(locators.most_popular_section_product_variants_xpath).click()
        time.sleep(3)
        product_added_from_UI_title = product_title
        time.sleep(8)
        cart_product_title = browser.find_element_by_xpath(locators.cart_popup_product_title_xpath).text
        print(product_added_from_UI_title)
        print(cart_product_title)
        assert cart_product_title.__contains__(product_added_from_UI_title)
        cart_product_title = browser.find_element_by_xpath(locators.cart_popup_product_title_xpath).text
        print(product_added_from_UI_title)
        print(cart_product_title)
        assert cart_product_title.__contains__(product_added_from_UI_title)
        cart_product_price = browser.find_element_by_xpath(locators.cart_popup_product_price_xpath).text
        product_price = product_price.replace('&nbsp;', '')
        print(product_price)
        print(cart_product_price)
        assert product_price == cart_product_price
        product_quantity = browser.find_element_by_xpath(locators.cart_popup_product_quantity_xpath).get_attribute(
            "value")
        assert product_quantity == '1'
        time.sleep(4)
        browser.find_element_by_xpath("//*[@class='view-full-cart']/a").click()
        time.sleep(8)


        # Checking the add to cart of frequently bought together-----------------------------------------------------------
        browser.refresh()
        helper.wait()
        browser.refresh()
        helper.wait()
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        time.sleep(3)
        frequently_bought = browser.find_elements_by_xpath(locators.frequently_bought_together)
        if (len(frequently_bought) > 0):
            print("INFO: frequently bought together products Full Cart-----------------------")
            ActionChains(browser).move_to_element(frequently_bought[0]).perform()
            time.sleep(2)
            add_to_cart = browser.find_elements_by_xpath(
                locators.frequently_bought_together_product_add_to_cart_xpath)
            length = len(add_to_cart) - 1
            random_num = random.randint(0, length)
            ActionChains(browser).move_to_element(add_to_cart[random_num]).perform()
            add_to_cart = browser.find_elements_by_xpath(
                locators.frequently_bought_together_product_add_to_cart_xpath)
            time.sleep(4)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            ActionChains(browser).move_to_element(add_to_cart[random_num]).click().perform()
            time.sleep(3)
            product_text = browser.find_elements_by_xpath(locators.frequently_bought_together_product_title_xpath)
            product_title = product_text[random_num].get_attribute("data-product-title")
            product_price_elements = browser.find_elements_by_xpath(
                locators.frequently_bought_together_product_price_xpath)
            product_price = product_price_elements[random_num].text
            time.sleep(3)
            time.sleep(3)
            var_click = browser.find_elements_by_xpath(locators.most_popular_section_product_variants_xpath)
            if (len(var_click) > 0):
                var_click[0].click()
            product_added_from_UI_title = product_title
            time.sleep(8)
            browser.refresh()
            time.sleep(10)
            full_cart_title = browser.find_element_by_xpath(locators.full_cart_item_title).text
            print(product_added_from_UI_title)
            print(full_cart_title)
            assert full_cart_title.__contains__(product_added_from_UI_title)
            full_cart_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            product_price = product_price.replace('&nbsp;', '')
            print(product_price)
            print(full_cart_price)
            assert product_price == full_cart_price
            product_quantity = browser.find_element_by_xpath(
                locators.cart_popup_product_quantity_xpath).get_attribute("value")
            assert product_quantity == '1'
            time.sleep(4)
            browser.refresh()
            helper.wait()
            time.sleep(7)
            reviews = browser.find_elements_by_xpath(locators.frequently_bought_together_product_reviews)
            if (len(reviews) > 0):
                assert len(reviews) > 0
                print("Reviews are present")
            else:
                print("Reviews are not present")
            stars = browser.find_elements_by_xpath(locators.frequently_bought_together_product_stars)
            if (len(stars) > 0):
                assert len(stars) > 0
                print("Stars are present")
            else:
                print("Stars are not present")
            questions = browser.find_elements_by_xpath(locators.frequently_bought_together_product_questions)
            if(len(questions) > 0):
                assert len(questions)>0
                print("Questions are  present")
            else:
                print("Questions are not present")
            time.sleep(5)
            all_reviews=browser.find_elements_by_xpath(locators.frequently_bought_together_product_reviews_all_xpath)
            time.sleep(3)
            # if(len(all_reviews)==0):
            #     print("Extra Checking")
            #     all_rev=browser.find_elements_by_xpath(locators.frequently_bought_together_product_reviews_all_xpath+"/../../..")
            #     all_rev[random_num].click()
            #     helper.wait()
            #     time.sleep(5)
            #     product_page_reviews=browser.find_elements_by_xpath(locators.product_detail_star_badges_xpath)
            #     assert len(product_page_reviews)==0



        else:
            print("INFO:No Frequently bought together section---------------")
        # Checking for you may like add to cart functionality full cart
        print("INFO:You May like Section Full cart-----------------------------------")
        time.sleep(4)
        browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
        you_may_like = browser.find_elements_by_xpath(locators.you_may_like_xpath)
        if (len(you_may_like) > 0):
            ActionChains(browser).move_to_element(you_may_like[0]).perform()
            time.sleep(4)
            add_to_cart = browser.find_elements_by_xpath(locators.you_may_like_add_to_cart_xpath)
            length = len(add_to_cart) - 1
            random_num = random.randint(0, length)
            time.sleep(2)
            ActionChains(browser).move_to_element(add_to_cart[random_num]).perform()
            product_text = browser.find_elements_by_xpath(locators.you_may_like_product_title_xpath)
            product_title = product_text[random_num].get_attribute("data-product-title")
            product_price_elements = browser.find_elements_by_xpath(locators.you_may_like_product_price_xpath)
            product_price = product_price_elements[random_num].text
            # browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
            time.sleep(3)
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            # ActionChains(browser).move_to_element(add_to_cart[random_num]).perform()
            time.sleep(3)
            browser.find_element_by_xpath("//body").send_keys(Keys.PAGE_UP)
            time.sleep(3)
            add_to_cart[random_num].click()
            time.sleep(3)
            print(len(product_price_elements))
            print(random_num)
            time.sleep(3)
            var_click = browser.find_elements_by_xpath(locators.most_popular_section_product_variants_xpath)
            if (len(var_click) > 0):
                var_click[0].click()
            product_added_from_UI_title = product_title
            time.sleep(10)
            browser.refresh()
            time.sleep(10)
            full_cart_title = browser.find_element_by_xpath(locators.full_cart_item_title).text
            full_cart_price = browser.find_element_by_xpath(locators.full_cart_item_price).text
            print(product_added_from_UI_title)
            print(full_cart_title)
            assert full_cart_title.__contains__(product_added_from_UI_title)
            full_cart_price = full_cart_price.replace('&nbsp;', '')
            print(product_price)
            print(full_cart_price)
            assert product_price == full_cart_price
            product_quantity = browser.find_element_by_xpath(
                locators.cart_popup_product_quantity_xpath).get_attribute("value")
            assert product_quantity == '1'
            time.sleep(4)
        else:
            print("INFO: No you may like section")


 


