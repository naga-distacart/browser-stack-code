import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from DistaCartTestAutomation.Helpers.helper import Helper
from DistaCartTestAutomation.Pages.homePage import HomePage
from DistaCartTestAutomation.Tests.conftest import get_user_name, get_password

class TestMobile:

 def test_login_details(self, browser, get_user_name, get_password):
    # Click on the login link
    homepage = HomePage(browser)
    helper = Helper(browser)

    clkHamburgMenu=browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu'])[1]/preceding::div[1]")
    clkHamburgMenu.click()
    time.sleep(5)
    Clogin_link = browser.find_element_by_id("customer_login_link")
    Clogin_link.click()
    time.sleep(5)
    #homepage.login(get_user_name, get_password)
    email_input = browser.find_element_by_id("customer_email")

    email_input.send_keys("distatestbot@gmail.com")
    password_input = browser.find_element_by_id("customer_password")
    password_input.send_keys("DistaTest@123")
    browser.close()
