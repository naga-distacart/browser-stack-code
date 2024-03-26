from selenium import webdriver

BROWSERSTACK_URL = 'http://pavithragenieexp1:YiuvqecR5os5Xcssp1tF@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
#    "os" : "OS X",
#    "os_version" : "Catalina",
#    "browser" : "Chrome",
#    "browser_version" : "80.0",
    "browserstack.local" : "false",
    "browserstack.selenium_version" : "3.5.2"
}

os_list                     = ["OS X"]
os_x_version_list           = ["Catalina"]
browser_list                = ["Chrome"]
chrome_browser_version_list = ["80.0"]

def open_browser_and_test(driver):
    # Opening distacart
    try:
        driver.get("https://www.distacart.com/")
    except:
        assert 0, "Unable to open distacart.com"
    

def test_add_to_cart():
    for os in os_list:
        desired_cap['os'] = os
        if os == "OS X":
            for os_x_version in os_x_version_list:
                desired_cap['os_version'] = os_x_version
                for browser in browser_list:
                    desired_cap['browser'] = browser
                    if browser == "Chrome":
                        for browser_version in chrome_browser_version_list:
                            desired_cap['browser_version'] = browser_version
                            try:
                                driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
                            except:
                                assert 0, "Unable to instantiate a %s session" %(browser)
                            open_browser_and_test(driver)
                            driver.quit()

def test_print_hello():
    print("Hello")
