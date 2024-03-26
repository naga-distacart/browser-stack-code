import json
import os
import random
import time

import pytest
from selenium.webdriver import Chrome, Firefox, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from DistaCartTestAutomation.Helpers.helper import Helper
from selenium.webdriver.chrome.options import Options as ChromeOptions

CONFIG_PATH = './../Data/config.json'
DEFAULT_WAIT_TIME = 10
DEFAULT_OS = 'Windows'
DEFAULT_OS_VERSION = '10'
BROWSER_VERSION = '120.0'
DEFAULT_APP_URL = 'https://www.distacart.com/'
SUPPORTED_BROWSERS = ['Chrome', 'Firefox']
SUPPORTED_CURRENCIES = ['USD', 'CAD', 'AUD', 'GBP', 'EUR', 'JPY']
global location


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


def pytest_addoption(parser):
    parser.addoption("--os", action="store")
    parser.addoption("--os_version", action="store")
    parser.addoption("--browser", action="store")
    parser.addoption("--browser_version", action="store")
    parser.addoption("--currency", action="store")
    parser.addoption("--app_url", action="store")
    parser.addoption("--build", action="store")


@pytest.fixture(scope='session')
def params(request):
    params = {}
    params['os'] = request.config.getoption('--os')
    params['os_version'] = request.config.getoption('--os_version')
    params['browser'] = request.config.getoption('--browser')
    params['browser_version'] = request.config.getoption('--browser_version')
    params['currency'] = request.config.getoption('--currency')
    params['app_url'] = request.config.getoption('--app_url')
    params['build'] = request.config.getoption('--build')
    return params


@pytest.fixture(scope='session')
def config_browser(config, params):
    # Validate and return the browser choice from the config data
    if params['browser'] is not None and params['browser'] in SUPPORTED_BROWSERS:
        return params['browser']
    elif 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception('"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def get_user_name(config):
    # Validate and return the user name from the config data
    return config['user_name'] if 'user_name' in config else "distatestbot@gmail.com"


@pytest.fixture(scope='session')
def get_password(config):
    # Validate and return the user password from the config data
    return config['user_password'] if 'user_password' in config else "DistaTest@123"


@pytest.fixture(scope='session')
def config_currency(config, params):
    # Set the currency
    if params['currency'] is not None and params['currency'] not in SUPPORTED_CURRENCIES:
        return params['currency']
    if 'currency' not in config:
        raise Exception('The config file does not contain "currency"')
    elif config['currency'] not in SUPPORTED_CURRENCIES:
        raise Exception('"{config["currency"]}" is not a supported currency')
    return config['currency']


@pytest.fixture(scope='session')
def config_app_url(config, params):
    # Validate and return the wait time from the config data
    if params['app_url'] is not None:
        return params['app_url']
    else:
        return config['app_url'] if 'app_url' in config else DEFAULT_APP_URL


def get_test_name():
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
    test_file = full_name.split("::")[0].split('/')[-1].split('.py')[0]
    test_name = full_name.split("::")[2]
    return test_file + "::" + test_name


@pytest.fixture(scope='session')
def config_os(config, params):
    # Validate and return the wait time from the config data
    if params['os'] is not None:
        return params['os']
    else:
        return config['os'] if 'os' in config else DEFAULT_OS


@pytest.fixture(scope='session')
def config_os_version(config, params):
    # Validate and return the wait time from the config data
    if params['os_version'] is not None:
        return params['os_version']
    else:
        return config['os_version'] if 'os_version' in config else DEFAULT_OS_VERSION


@pytest.fixture(scope='session')
def config_browser_version(config, params):
    # Validate and return the wait time from the config data
    if params['browser_version'] is not None:
        return params['browser_version']
    else:
        return config['browser_version'] if 'browser_version' in config else BROWSER_VERSION


@pytest.fixture(scope='session')
def config_build_name(config, params):
    # Validate and return the wait time from the config data
    if params['build'] is not None:
        return params['build']
    else:
        return config['build'] if 'build' in config else 'DistaCartTestAutomation'


@pytest.fixture(scope='session')
def config_browser_stack_url(config):
    # Validate and return the wait time from the config data
    return config['browser_stack_url'] if 'browser_stack_url' in config else ''


@pytest.fixture
def browser(config_build_name, config_browser, config_wait_time, config_app_url, config_currency, config_os, config_os_version, config_browser_version, config_browser_stack_url):
    global location
    desired_cap = {

        'platform': config_os + " " + config_os_version,
        'browserName': config_browser,
        'version': config_browser_version,
        'name': get_test_name(),
        'build': config_build_name,
        'network': True,
        'network.full.har': True,
        'DisableXFHeaders': True,
        'pageLoadStrategy': 'eager',
        'visual': 'True'

    }
    location='US'

    if 'test_geolocation' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location

    if 'afterpay' in get_test_name():
        location = 'GB'
        desired_cap['geoLocation'] = location
    if 'test_geolocation_coupons' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location
    if 'test_shipping_box_text_US' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location
    if 'test_shipping_box_text_GB' in get_test_name():
        location = 'GB'
        desired_cap['geoLocation'] = location
    if 'google_ads_url_currency_check' in get_test_name():
        list = ['US', 'AU', 'GB', 'JP', 'AE', 'CA', 'CH', 'CZ', 'DK', 'NL', 'HK', 'HU', 'ID', 'IL', 'NO', 'NZ',
                'PH', 'PL', 'QA', 'SA', 'SG', 'TW', 'VN', 'ZA']
        location = random.choice(list)
        desired_cap['geoLocation'] = location






    if 'test_currency_switch_check_US' in get_test_name():
        # list=['US','AU','GB','JP','AE','CA','CH','CZ','DK','NL','HK','HU','ID','IL','MT','NO','NZ','PH','PL','QA','SA','SG','TW','VN','ZA','AR','RO','PE']
        location = 'US'
        desired_cap['geoLocation'] = location

    if 'test_currency_switch_check_CA' in get_test_name():
        # list=['US','AU','GB','JP','AE','CA','CH','CZ','DK','NL','HK','HU','ID','IL','MT','NO','NZ','PH','PL','QA','SA','SG','TW','VN','ZA','AR','RO','PE']
        location = 'CA'
        desired_cap['geoLocation'] = location

    if 'test_currency_switch_check_AU' in get_test_name():
        # list=['US','AU','GB','JP','AE','CA','CH','CZ','DK','NL','HK','HU','ID','IL','MT','NO','NZ','PH','PL','QA','SA','SG','TW','VN','ZA','AR','RO','PE']
        location = 'AU'
        desired_cap['geoLocation'] = location
    if 'test_google_ads_shipping_progress_bar_US' in get_test_name():
        location='US'
        desired_cap['geoLocation']=location

    if 'test_geolocation_afterpay_product_page' in get_test_name():
        location='GB'
        desired_cap['geoLocation']=location

    if 'test_google_ads_shipping_progress_bar_AU' in get_test_name():
        location='AU'
        desired_cap['geoLocation']=location

    if 'test_google_ads_shipping_progress_bar_CA' in get_test_name():
        location='CA'
        desired_cap['geoLocation']=location
        
    if 'test_geolocation_coupons' in get_test_name():
        location='GB'
        desired_cap['geoLocation']=location

    if 'test_currency_switch_check_GB' in get_test_name():
        # list=['US','AU','GB','JP','AE','CA','CH','CZ','DK','NL','HK','HU','ID','IL','MT','NO','NZ','PH','PL','QA','SA','SG','TW','VN','ZA','AR','RO','PE']
        location = 'GB'
        desired_cap['geoLocation'] = location

    if 'test_currency_switch_check_NL' in get_test_name():
        # list=['US','AU','GB','JP','AE','CA','CH','CZ','DK','NL','HK','HU','ID','IL','MT','NO','NZ','PH','PL','QA','SA','SG','TW','VN','ZA','AR','RO','PE']
        location = 'NL'
        desired_cap['geoLocation'] = location

    if 'test_after_pay_check_US' in get_test_name():
        location='US'
        desired_cap['geoLocation'] = location

    if 'test_after_pay_check_NZ' in get_test_name():
        location = 'NZ'
        desired_cap['geoLocation'] = location



    if 'test_after_pay_check_UK' in get_test_name():
        location = 'GB'
        desired_cap['geoLocation'] = location

    if 'test_after_pay_check_CA' in get_test_name():
        location = 'CA'
        desired_cap['geoLocation'] = location

    if 'test_after_pay_check_AU' in get_test_name():
        location = 'AU'
        desired_cap['geoLocation'] = location

    if 'test_after_pay_check_SG' in get_test_name():
        location = 'SG'
        desired_cap['geoLocation'] = location
    if 'test_after_pay_check_FR' in get_test_name():
        location = 'FR'
        desired_cap['geoLocation'] = location

    if 'test_limespot' in get_test_name():
        location='US'
        desired_cap['geoLocation'] = location

    if 'test_rapid_delivery' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_US' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location
        
    if 'test_increase_quantity_form_sticky_cart' in get_test_name():
        location = 'US'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_CA' in get_test_name():
        location = 'CA'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_AU' in get_test_name():
        location = 'AU'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_GB' in get_test_name():
        location = 'GB'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_NZ' in get_test_name():
        location = 'NZ'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_EU' in get_test_name():
        location = 'NL'
        desired_cap['geoLocation'] = location

    if 'test_add_to_cart_SG' in get_test_name():
        location = 'SG'
        desired_cap['geoLocation'] = location

    if 'test_login_to_checkout_AU' in get_test_name():
        location = 'AU'
        desired_cap['geoLocation'] = location

    if 'test_login_to_checkout_CA' in get_test_name():
        location = 'CA'
        desired_cap['geoLocation'] = location

    if 'test_non_usa_customer_checkout' in get_test_name():
        location = 'CA'
        desired_cap['geoLocation'] = location





    # Initialize WebDriver
    if config_browser == 'Chrome':
        chrome_options = webdriver.ChromeOptions()
        options = ChromeOptions()
        options.set_capability('sessionName', 'BStack Local Test')
        options.set_capability('browserstack.geoLocation', location)
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        # desired_cap.update({'selenium_version': '4.4.3'})
        #desired_cap.update({'chrome.driver': '109.0'})
        #desired_cap.update(chrome_options.to_capabilities())
        print(desired_cap)
        #desired_cap['ChromeOptions.CAPABILITY'] = chrome_options
        driver = webdriver.Remote(command_executor=config_browser_stack_url,
                                    options=options)
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Remote(command_executor=config_browser_stack_url, desired_capabilities=desired_cap, options=chrome_options)
        #driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./../Drivers/chromedriver.exe")
        #driver = webdriver.Chrome("C:/Users/xyz/PycharmProjects/DistaCartTestAutomation/DistaCartTestAutomation/Drivers/chromedriver.exe")
    elif config_browser == 'Firefox':
        options = Options()
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('pref.privacy.disable_button.tracking_protection_exceptions', True)
        options.set_preference('privacy.socialtracking.block_cookies.enabled', False)
        options.set_preference('privacy.trackingprotection.annotate_channels', False)
        options.set_preference('privacy.trackingprotection.fingerprinting.enabled', False)
        #desired_cap.update({'selenium_version': '3.13.0'})
        #desired_cap.update({'firefox.driver': 'v0.26.0'})
        desired_cap['selenium_version'] = '3.13.0'
        desired_cap['firefox.driver'] = 'v0.26.0'
        print(desired_cap)
        #desired_cap.update(options.to_capabilities())
        driver = webdriver.Remote(command_executor=config_browser_stack_url, desired_capabilities=desired_cap, options=options)
    else:
        raise Exception('"{config_browser}" is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    # config_app_url="https://www.distacart.com?preview_theme_id=132334846111"


    driver.get(config_app_url)
    driver.implicitly_wait(config_wait_time)
       # driver.refresh()
    link = driver.current_url
    if link.__contains__("?"):
        links = link.split("?")
        # print(links[0])
        link = links[0]
    driver.get(link)
    driver.maximize_window()
    driver.delete_all_cookies()
   # time.sleep(120)
    driver.set_page_load_timeout(config_wait_time)
    helper = Helper(driver)
    driver.switch_to.frame("cmessage_form_iframe")
    element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='close_icon']"))
    )
    popup = driver.find_elements_by_xpath("//div[@class='close_icon']")
    action = ActionChains(driver)
    if (len(popup) > 0):
        element = driver.find_element_by_xpath("//div[@class='close_icon']")
        time.sleep(5)
        element.click()
        driver.switch_to.default_content()
        time.sleep(4)
        # action.click()
        # driver.switch_to.frame("cmessage_form_iframe")
        # print(len(driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
        # if (len(driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")) > 0):
        #     print(len(driver.find_elements_by_xpath("//*[@class='popup_header']//*[@cx='10']")))
        #     #driver.find_element_by_xpath("//*[@class='popup_header']//*[@cx='10']/../..").click()
        # driver.switch_to.default_content()
    """if helper.is_element_present_by_xpath("//button[contains(@class,'needsclick CloseButton')]"):
        driver.find_element_by_xpath("//button[contains(@class,'needsclick CloseButton')]").click()"""
    # k = 0
    # p = 0
    # t = 0
    # while k != 2 and config_os != 'macOS':
    #     if len(driver.find_elements_by_xpath("//div[@class='cc-bottom_close']")) > 0:
    #         driver.find_element_by_xpath("//div[@class='cc-bottom_close']").click()
    #         k += 1
    #     """WebDriverWait(driver, 120).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='ccparty-cc-content']/div[@class='cc-close']"))
    #     )"""
    #     if t == 0:
    #         if len(driver.find_elements_by_xpath("//div[text()='Later']")) > 0:
    #             driver.find_element_by_xpath("//div[text()='Later']").click()
    #             driver.switch_to.default_content()
    #             t += 1
    #             k += 1
    #     if len(driver.find_elements_by_xpath("//div[@class='ccparty-cc-content']/div[@class='cc-close']")) > 0:
    #         driver.find_element_by_xpath("//div[@class='ccparty-cc-content']/div[@class='cc-close']").click()
    #         k += 1
    #     """WebDriverWait(driver, 120).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='cc-close']"))
    #     )"""
    #     if len(driver.find_elements_by_xpath("//div[@class='cc-bottom_close']")) > 0:
    #         driver.find_element_by_xpath("//div[@class='cc-bottom_close']").click()
    #         k += 1
    #     """WebDriverWait(driver, 120).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'needsclick klaviyo-close-form')]"))
    #     )"""
    #     if len(driver.find_elements_by_xpath(
    #             "//h4[text()='your first order when you sign up']/../../div[@class='cc-close']")) > 0:
    #         # cls_popup = driver.find_element_by_xpath("//div[@class='cc-second-drop']/div[@class='cc-close']")
    #         # driver.execute_script("arguments[0].click();", cls_popup)
    #         while k != 2:
    #             if len(driver.find_elements_by_xpath("//button[contains(@class,'needsclick klaviyo-close-form')]")) > 0:
    #                 cls_popup = driver.find_element_by_xpath(
    #                     "//button[contains(@class,'needsclick klaviyo-close-form')]")
    #                 driver.execute_script("arguments[0].click();", cls_popup)
    #                 k += 1
    #             driver.find_element_by_xpath(
    #                 "//h4[text()='your first order when you sign up']/../../div[@class='cc-close']").click()
    #             k += 1
    #     if len(driver.find_elements_by_xpath("//button[contains(@class,'needsclick klaviyo-close-form')]")) > 0:
    #         cls_popup = driver.find_element_by_xpath("//button[contains(@class,'needsclick klaviyo-close-form')]")
    #         driver.execute_script("arguments[0].click();", cls_popup)
    #         k += 1
    #     helper.wait()
    #
    #     if p == 0:
    #         driver.switch_to.frame("ps__widget")
    #         WebDriverWait(driver, 120).until(
    #             EC.presence_of_element_located((By.XPATH, "//button[@id='ps-desktop-widget__close-link']"))
    #         )
    #         if len(driver.find_elements_by_xpath("//button[@id='ps-desktop-widget__close-link']")) > 0:
    #             driver.find_element_by_xpath("//button[@id='ps-desktop-widget__close-link']").click()
    #             p += 1
    #             k += 1
    # driver.switch_to.default_content()
    # if len(driver.find_elements_by_xpath("//div[@class='cc-bottom_close']")) > 0:
    #     driver.find_element_by_xpath("//div[@class='cc-bottom_close']").click()
    #     k += 1
    # """WebDriverWait(driver, 120).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'needsclick CloseButton')]"))
    # )
    # driver.find_element_by_xpath("//button[contains(@class,'needsclick CloseButton')]").click()
    # WebDriverWait(driver, 120).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@id='ps-desktop-widget__close-link']"))
    # )
    # driver.find_element_by_xpath("//button[@id='ps-desktop-widget__close-link']").click()"""
    # if 'afterpay' or 'shipping_progress' or 'test_currency_switch_check' or 'google_ads_url_currency_check' or 'test_google_page_speed_insights' or 'test_limespot' or 'TestAddToCart' or 'test_after_pay_check' in get_test_name():
    #     test = 1
    # else:
    #     helper.set_currency(config_currency)
    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()