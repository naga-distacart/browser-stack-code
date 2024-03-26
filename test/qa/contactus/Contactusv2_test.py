BROWSERSTACK_URL = 'http://pavithragenieexp1:YiuvqecR5os5Xcssp1tF@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
    'browser': 'Firefox',
    'browser_version': '77.0 beta',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '1024x768',
    'name': 'Bstack-[Python] Sample Test'
}

os_list = ["Windows"]
os_x_version_list = ["10"]
browser_list = ["Firefox"]
firefox_browser_version_list = ["77.0 beta"]

from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def contact_us(driver):
    try:
        driver.get("https://www.distacart.com/")
    except:
        assert 0, "Distacart website not found"
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            "//*[@id='shopify-section-header']/header[2]/div[2]/div/div[2]/div/div/ul/li[2]/a").click()
    except:
        assert 0, "contactus icon is not clickable"
    try:
        driver.find_element_by_id("contactFormName").send_keys("Pavithra")

    except:
        assert 1, "Name is not taking as input"
    try:
        driver.find_element_by_id("contactFormEmail").send_keys("pavithra.genieexports@gmail.com")

    except:
        assert 2, "Email is not taking as input"
    try:
        driver.find_element_by_id("contactFormMessage").send_keys("This is to test contactus page is working or not")

    except:
        assert 3, "Message is not taking as input"
    try:
        driver.find_element_by_xpath("//*[@id='contact_form']/input[3]").click()

    except:
        assert 4, "Send button not working"

    try:
        product_page = driver.find_element_by_xpath(
            "//*[@id='shopify-section-header']/header[2]/div[2]/div/div[2]/div/div/ul/li[2]/a")
        if product_page.get_attribute("innerHTML") == '1':
            print("test pass")
        else:
            assert -1, "test fail"
    except:
        assert 0, "contactus functionality is not working"


def test_search():
    # opening distacart
    for os in os_list:
        desired_cap['os'] = os
        if os == "Windows":
            for os_x_version in os_x_version_list:
                desired_cap['os_version'] = os_x_version
                for browser in browser_list:
                    desired_cap['browser'] = browser
                    if browser == "Firefox":
                        for browser_version in firefox_browser_version_list:
                            desired_cap['browser_version'] = browser_version
                            try:
                                driver = webdriver.Remote(command_executor=BROWSERSTACK_URL,
                                                          desired_capabilities=desired_cap)
                            except:
                                assert 0, "Unable to instantiate a %s session" % (browser)
                            contact_us(driver)
                            driver.quit()

