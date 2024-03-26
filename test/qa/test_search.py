BROWSERSTACK_URL ='https://keertivutukuru1:h81vpYThhW81sTh9jF3Y@hub-cloud.browserstack.com/wd/hub'

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

from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException

def open_browser_and_test(driver):
    try:
      driver.get("https://www.distacart.com/")
    except:
       assert 0, "not found 1"
    try:
      element = driver.find_element_by_name("q")
      element.send_keys("books")
      element.submit()
    except:
       assert 0, "not found 2"
    #try:
     # driver.find_element_by_xpath("//*[@id="shopify-section-header "]/header[2]/div[2]/div/div[1]/div/div/div[2]/li/form/span").click()
    #except:
      # assert 0,"not found 3"
    try:
      driver.find_element_by_xpath("//li[@id='snize-product-4098890891309']//span[@class='snize-thumbnail']").click()
    except:
       assert 0, "not found 4"
    try:
      driver.find_element_by_name("add").click()
    except:
       assert 0, "not found 5"
    #except:
       # assert 0,"Element not found"
    try:
        cart_count = driver.find_element_by_class_name("cart_count")
        if cart_count.get_attribute("innerHTML") == '1':
            print("test pass")
        else:
            assert -1,"test fail"
    except:
         assert 0,"Item is not added"

def test_search():
   #opening distacart
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




