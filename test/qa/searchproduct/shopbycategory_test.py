BROWSERSTACK_URL = 'http://pavithragenieexp1:YiuvqecR5os5Xcssp1tF@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '81.0',
 'os': 'Windows',
 'os_version': '8.1',
 # 'resolution': '1024x768',
 # 'name': 'Bstack-[Python] Sample Test'
}
os_list = ["Windows"]
os_x_version_list = ["8.1"]
browser_list = ["Chrome"]
chrome_browser_version_list = ["81.0"]

from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def shop_by_categories(driver):
    try:
        driver.get("https://www.distacart.com/")
    except:
        assert 0, "Distacart website not found"
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/header[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div").click()
    except:
        assert 0, "Menu items are not shown"

    try:

        firstLevelMenu = driver.find_element_by_css_selector(
            "#menu > ul > div > div.nav > ul > div > li:nth-child(2) > a")
        action = ActionChains(driver)
        action.move_to_element(firstLevelMenu).perform()
    except:
        assert 0, "SubCategory Items are not showing when hovering on categories"
    try:

        secondLevelMenu = driver.find_element_by_css_selector(
            "#menu > ul > div > div.nav > ul > div > li:nth-child(2) > ul > li:nth-child(2) > a")
        secondLevelMenu.click()

    except:
        assert 0, "Product is not clickable "

    try:
        product_page = driver.find_element_by_xpath("//*[@id='menu']/ul/div/div[1]/ul/div/li[2]/ul/li[2]/a")
        if product_page.get_attribute("innerHTML") == '1':
            print("test pass")
        else:
            assert -1, "test fail"
    except:
        assert 0, "Item is not added"

def test_search():
     #opening distacart
     for os in os_list:
         desired_cap['os'] = os
         if os == "Windows":
             for os_x_version in os_x_version_list:
                 desired_cap['os_version'] = os_x_version
                 for browser in browser_list:
                     desired_cap['browser'] = browser
                     if browser == "Chrome":
                         for browser_version in chrome_browser_version_list:
                             desired_cap['browser_version'] = browser_version
                             try:
                                 driver: WebDriver = webdriver.Remote(command_executor=BROWSERSTACK_URL,
                                                           desired_capabilities=desired_cap)
                             except:
                                 assert 0, "Unable to instantiate a %s session" % (browser)
                             shop_by_categories(driver)
                             driver.quit()

