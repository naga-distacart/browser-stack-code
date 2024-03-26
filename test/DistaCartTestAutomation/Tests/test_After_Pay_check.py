
import math
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DistaCartTestAutomation.Helpers import helper
from DistaCartTestAutomation.Locators.locators import Locators as locators
from DistaCartTestAutomation.Helpers.helper import Helper
import time
import random


class TestAfterPayCheck:

    def test_after_pay_check_US(self, browser):
        helper=Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        for i in range(1,4):
            #Selecting random product
            currency=browser.find_element_by_xpath(locators.Currency_select).text
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath("//*[@class='snize-title']")
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link+"/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
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
            brand_product_titles[random_num].click()
            helper.wait()
            sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
            if(len(sold_out)>0):
                browser.get("https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

            #Checking the after pay price
            prices=browser.find_elements_by_xpath(locators.product_page_price_xpath)
            if(len(prices)>0):
                price=prices[0].text
            else:
                continue
            import re
            s = re.sub("[^0123456789\.]", "", price)
            price_without_currency = float(s)
            price_after_pay=price_without_currency/4
            fac = 10 ** 2
            exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
            length = len(str(exp_price_after_pay))
            price_after_pay=str(exp_price_after_pay)
            exp_price_after_pay = price_after_pay[:length - 1]
            print(exp_price_after_pay)
            actual_after_pay_price=browser.find_element_by_xpath(locators.after_pay_price_xpath).text
            length = len(str(actual_after_pay_price))
            actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
            assert str("${} ".format(exp_price_after_pay)+"USD") == str(actual_after_pay_price)

            # After pay info click
            time.sleep(4)
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
            browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
            time.sleep(4)
            assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

            #After pay check for unavailable items
            helper.get_correct_link(link)
            browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            time.sleep(4)
            afterpay_check=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check=="display: none;"

            # After pay check for sold out items
            helper.get_correct_link(link)
            browser.get(link+"/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
            helper.wait()
            afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check == "display: none;"

    def test_after_pay_check_NZ(self, browser):
        helper=Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        print(link)
        for i in range(1,4):
            #Selecting random product
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link+"/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            brand_product_titles[random_num].click()
            helper.wait()
            sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
            if (len(sold_out) > 0):
                browser.get("https://www.distacart.com/en-nz/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

            #Checking the after pay price
            price=browser.find_element_by_xpath(locators.product_page_price_xpath).text
            import re
            s = re.sub("[^0123456789\.]", "", price)
            price_without_currency = float(s)
            price_after_pay=price_without_currency/4
            fac = 10 ** 2
            exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
            length = len(str(exp_price_after_pay))
            price_after_pay = str(exp_price_after_pay)
            exp_price_after_pay = price_after_pay[:length - 1]
            print(exp_price_after_pay)
            actual_after_pay_price = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
            length = len(str(actual_after_pay_price))
            actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
            assert str("${} NZD".format(exp_price_after_pay)) == str(actual_after_pay_price)

            # After pay info click
            time.sleep(4)
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
            browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
            time.sleep(4)
            assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

            #After pay check for unavailable items
            helper.get_correct_link(link)
            browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            time.sleep(4)
            afterpay_check=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check=="display: none;"

            # After pay check for sold out items
            helper.get_correct_link(link)
            browser.get(link+"/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
            helper.wait()
            afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check == "display: none;"

    def test_after_pay_check_UK(self, browser):
        helper=Helper(browser)
        # link = browser.current_url
        # if link.__contains__("?"):
        #     links = link.split("?")
        #     # print(links[0])
        link = "https://www.distacart.com/en-gb"
        for i in range(1,4):
            #Selecting random product
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link+"/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            brand_product_titles[random_num].click()
            time.sleep(30)
            sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
            if (len(sold_out) > 0):
                browser.get("https://www.distacart.com/en-gb/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

            #Checking the after pay price
            price=browser.find_element_by_xpath(locators.product_page_price_xpath).text
            import re
            s = re.sub("[^0123456789\.]", "", price)
            price_without_currency = float(s)
            price_after_pay=price_without_currency/4
            fac = 10 ** 2
            exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
            length = len(str(exp_price_after_pay))
            price_after_pay = str(exp_price_after_pay)
            exp_price_after_pay = price_after_pay[:length - 1]
            print(exp_price_after_pay)
            actual_after_pay_price = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
            length = len(actual_after_pay_price)
            actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
            assert str("GBP".format(exp_price_after_pay)) in actual_after_pay_price

            # After pay info click
            time.sleep(4)
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
            browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
            time.sleep(4)
            assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

            #After pay check for unavailable items
            helper.get_correct_link(link)
            browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            time.sleep(4)
            afterpay_check=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check=="display: none;"

            # After pay check for sold out items
            helper.get_correct_link(link)
            browser.get(link+"/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
            time.sleep(30)
            afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check == "display: none;"

    def test_after_pay_check_CA(self, browser):
        helper=Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        for i in range(1,4):
            #Selecting random product
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link+"/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            brand_product_titles[random_num].click()
            helper.wait()
            sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
            if (len(sold_out) > 0):
                browser.get("https://www.distacart.com/en-ca/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

            #Checking the after pay price
            price=browser.find_element_by_xpath(locators.product_page_price_xpath).text
            import re
            s = re.sub("[^0123456789\.]", "", price)
            price_without_currency = float(s)
            price_after_pay=price_without_currency/4
            fac = 10 ** 2
            exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
            length = len(str(exp_price_after_pay))
            price_after_pay = str(exp_price_after_pay)
            exp_price_after_pay = price_after_pay[:length - 1]
            print(exp_price_after_pay)
            actual_after_pay_price = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
            length = len(str(actual_after_pay_price))
            actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
            assert str("${} CAD".format(exp_price_after_pay)) == str(actual_after_pay_price)

            # After pay info click
            time.sleep(4)
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
            browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
            time.sleep(4)
            assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

            #After pay check for unavailable items
            helper.get_correct_link(link)
            browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            time.sleep(4)
            afterpay_check=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check=="display: none;"

            # After pay check for sold out items
            helper.get_correct_link(link)
            browser.get(link+"/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
            helper.wait()
            afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check == "display: none;"

    def test_after_pay_check_AU(self, browser):
        helper=Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        for i in range(1,4):
            #Selecting random product
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link+"/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).click().perform()
            helper.wait()
            sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
            if (len(sold_out) > 0):
                browser.get("https://www.distacart.com/en-au/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

            #Checking the after pay price
            price=browser.find_element_by_xpath(locators.product_page_price_xpath).text
            import re
            s = re.sub("[^0123456789\.]", "", price)
            price_without_currency = float(s)
            price_after_pay=price_without_currency/4
            fac = 10 ** 2
            exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
            length = len(str(exp_price_after_pay))
            price_after_pay = str(exp_price_after_pay)
            exp_price_after_pay = price_after_pay[:length - 1]
            print(exp_price_after_pay)
            actual_after_pay_price = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
            length = len(str(actual_after_pay_price))
            actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
            assert str("${} AUD".format(exp_price_after_pay)) == str(actual_after_pay_price)

            # After pay info click
            time.sleep(4)
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
            browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
            time.sleep(4)
            assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

            #After pay check for unavailable items
            helper.get_correct_link(link)
            browser.get(link+"/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            time.sleep(4)
            afterpay_check=browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check=="display: none;"

            # After pay check for sold out items
            helper.get_correct_link(link)
            browser.get(link+"/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
            helper.wait()
            afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            assert afterpay_check == "display: none;"

    def test_after_pay_check_SG(self, browser):
        helper = Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        for i in range(1, 4):
            # Selecting random product
            helper.get_correct_link(link)
            browser.get(link + "/pages/brands")
            WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, locators.all_brands_xpath)))
            all_brands = browser.find_elements_by_xpath(locators.all_brands_xpath)
            random_num = random.randint(1, len(all_brands) - 1)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            brand_name = all_brands[random_num].text
            print(brand_name)
            ActionChains(browser).move_to_element(all_brands[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(3)
            all_brands[random_num].click()
            time.sleep(10)
            brand_product_titles = browser.find_elements_by_xpath(
                locators.all_products_in_collection_page_title.format(brand_name))
            if (len(brand_product_titles) == 0):
                brand_name = 'Patanjali'
                helper.get_correct_link(link)
                browser.get(link + "/collections/types?q=Patanjali")
                time.sleep(9)
                brand_product_titles = browser.find_elements_by_xpath(
                    locators.all_products_in_collection_page_title.format(brand_name))
            print(len(brand_product_titles))
            if (len(brand_product_titles) > 2):
                random_num = random.randint(1, len(brand_product_titles) - 1)
            else:
                random_num = 0
            print(random_num)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).perform()
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            time.sleep(1)
            browser.find_element_by_xpath("//body").send_keys(Keys.DOWN)
            ActionChains(browser).move_to_element(brand_product_titles[random_num]).click().perform()
            helper.wait()
            after_pay=browser.find_elements_by_xpath(locators.after_pay_logo_badge_xpath)
            assert len(after_pay)==0

    def test_after_pay_check_FR(self, browser):
        helper = Helper(browser)
        link = browser.current_url
        if link.__contains__("?"):
            links = link.split("?")
            # print(links[0])
            link = links[0]
        browser.get("https://www.distacart.com/en-eu/products/astaberry-professional-mulberry-skin-whitening-face-gel")
        sold_out = browser.find_elements_by_xpath(locators.product_sold_out_xpath)
        if (len(sold_out) > 0):
            browser.get(
                "https://www.distacart.com/en-eu/products/isha-life-neem-and-turmeric-capsules?variant=37625830736031")

        # Checking the after pay price
        # price = browser.find_element_by_xpath(locators.product_page_price_xpath).text
        # import re
        # s = re.sub("[^0123456789\.]", "", price)
        # price_without_currency = float(s)
        # price_after_pay = price_without_currency / 4
        # fac = 10 ** 2
        # exp_price_after_pay = '{:.2f}'.format(math.floor(price_after_pay * fac) / fac)
        # length = len(str(exp_price_after_pay))
        # price_after_pay = str(exp_price_after_pay)
        # exp_price_after_pay = price_after_pay[:length - 1]
        # print(exp_price_after_pay)
        # actual_after_pay_price = browser.find_element_by_xpath(locators.after_pay_price_xpath).text
        # length = len(str(actual_after_pay_price))
        # actual_after_pay_price = actual_after_pay_price[:length - 5] + actual_after_pay_price[length - 4:]
        # assert str("EUR".format(exp_price_after_pay)) in actual_after_pay_price

        # After pay info click
        time.sleep(4)
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
        browser.find_element_by_xpath(locators.after_pay_popup_xpath).click()
        time.sleep(4)
        assert browser.find_element_by_xpath(locators.after_pay_popup_logo_xpath)

        # After pay check for unavailable items
        helper.get_correct_link(link)
        browser.get(link + "/products/patanjali-tulsi-ghan-vati?variant=41993852846239")
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
            # browser.switch_to.default_content()
            # browser.find_element_by_xpath(locators.product_variant_of_pack_of_3_xpath).click()
            # time.sleep(4)
            # afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
            # assert afterpay_check == "display: none;"

        # After pay check for sold out items
        helper.get_correct_link(link)
        browser.get(link + "/products/terracotta-lotus-pendant-mini-necklace-set-with-studs?variant=41523354173599")
        helper.wait()
        afterpay_check = browser.find_element_by_xpath(locators.after_pay_logo_badge_xpath).get_attribute('style')
        assert afterpay_check == "display: none;"



