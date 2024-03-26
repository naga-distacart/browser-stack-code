BROWSERSTACK_URL = 'http://pavithragenieexp1:YiuvqecR5os5Xcssp1tF@hub-cloud.browserstack.com/wd/hub'
from selenium import webdriver

desired_cap = dict(browser='Chrome', browser_version='81.0', os='Windows', os_version='8.1')
os_list = ["Windows"]
os_x_version_list = ["8.1"]
browser_list = ["Chrome"]
chrome_browser_version_list = ["81.0"]

os_list = ["Windows"]
os_x_version_list = ["8.1"]
browser_list = ["Chrome"]
chrome_browser_version_list = ["81.0"]


def search_item(driver):
    try:
        driver.get("https://www.distacart.com/")
    except:
        assert 0, "Distacart website not found"
    try:
        driver.find_element_by_name("q").send_keys("Patanjali Kutajarishta")

    except:
        assert 1, "Search not working"
    try:
         driver.find_element_by_css_selector("#shopify-section-header > header.desktop-header > div.main_nav_wrapper > div > div.sticky-top > div > div > div.cart-user-search > li > form > span").click()

    except:
        assert 2, "Not clickable"


def test_search():
    # opening distacart
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
                                driver = webdriver.Remote(command_executor=BROWSERSTACK_URL,
                                                          desired_capabilities=desired_cap)
                            except:
                                assert 0, "Unable to instantiate a %s session" % browser
                            search_item(driver)
                            driver.quit()

