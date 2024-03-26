# import re
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from DistaCartTestAutomation.Helpers.helper import Helper
# from DistaCartTestAutomation.Locators.locators import Locators as locators
# from selenium.webdriver.support import expected_conditions as EC
#
# from DistaCartTestAutomation.Tests.dista_shopify import ShopifyAPIClass
#
#
# class TestrapidDeliveryAtVariantLevel:
#
#     def test_rapid_delivery_at_variant_level_US(self, browser):
#         helper = Helper(browser)
#         link=browser.current_url
#         helper = Helper(browser)
#         helper.get_correct_link(link)
#         helper.get_correct_link(link)
#         #browser.get(link+"/products/isha-life-neem-and-turmeric-capsules")
#         browser.get(link +"/products/himalaya-speman-tablets-60-tablets")
#         WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,locators.rapid_label_xpath)))
#         assert EC.element_to_be_clickable((By.XPATH,locators.rapid_label_xpath))
#         browser.find_element_by_xpath(locators.rapid_delivery_info_xpath).click()
#         time.sleep(5)
#         assert EC.presence_of_element_located((By.XPATH,locators.rapid_delivery_pop_up_content_xpath))
#
#     def test_shipping_days_US(self,browser):
#         helper = Helper(browser)
#         variants = ShopifyAPIClass('variants')
#         mf1 = variants.shopify_object_metafield_get(36171208917151,filters={'key': 'product_ready_to_ship', 'namespace': "distacart"})
#         print(mf1)
#         print(mf1[0]['value'])
#         min_max_days=mf1[0]['value']
#         tis = min_max_days.split('"')
#         print(tis)
#         min_days = tis[2]
#         min_days = re.sub("[^0123456789\0]", "", min_days)
#         print("Min Days:",min_days)
#         max_days = tis[4]
#         max_days = re.sub("[^0123456789\0]", "", max_days)
#         print("Max_days:",max_days)
#         link = browser.current_url
#         helper.get_correct_link(link)
#         browser.get(link + "/products/amit-pharma-dehshuddi-tablets?variant=36171208917151")
#         WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,locators.shipping_info_xpath)))
#         shipping_days=browser.find_element_by_xpath(locators.shipping_info_xpath).text
#         assert "Ready to dispatch in {} - {} business days".format(min_days,max_days) == shipping_days
#
#
#
