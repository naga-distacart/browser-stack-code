from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from DistaCartTestAutomation.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        locators = Locators()
        self.driver = driver
        self.search_textbox_xpath = locators.search_textbox_xpath

    def search_product(self, search_item, product_name):
        self.driver.implicitly_wait(90)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).click()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(search_item)
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(u'\ue007')
        self.driver.implicitly_wait(30)

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, product_name)))
        #self.driver.find_element_by_xpath(product_name).click()
        element = self.driver.find_element_by_xpath(product_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(20)

    def search_by_result(self):
        self.driver.implicitly_wait(90)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(Locators.click_on_search_xpath).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(
            "//div[@class='main-nav__wrapper']//div[@class='search-container']//input[@placeholder='Search']").send_keys('unani products')
        time.sleep(10)
        self.driver.find_element_by_xpath(
            "//div[@class='main-nav__wrapper']//div[@class='search-container']//span[@class='icon-search search-submit']").click()
        time.sleep(20)

    def go_to_home_page(self):
        self.driver.find_element_by_xpath(Locators.home_button_xpath).click()
        self.driver.implicitly_wait(30)

    def click_on_shop_by_categories_menu(self, menu):
        time.sleep(20)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, Locators.shop_by_categories_xpath)))
        self.driver.find_element_by_xpath(Locators.shop_by_categories_xpath).click()
        main_menu = Locators.product_main_menu_xpath.format(menu)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, main_menu)))
        self.driver.find_element_by_xpath(main_menu).click()

    def login(self, user_name, password):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, Locators.login_register_xpath)))
        self.driver.find_element_by_xpath(Locators.login_register_xpath).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, Locators.user_name_id)))
        self.driver.find_element_by_id(Locators.user_name_id).send_keys(user_name)
        self.driver.find_element_by_id(Locators.user_password_id).send_keys(password)
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, Locators.referral_button_id)))
        WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.ID, Locators.referral_button_id)))

    def logout(self):
        self.driver.find_element_by_xpath(Locators.my_account_xpath).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, Locators.logout_xpath)))
        self.driver.find_element_by_xpath(Locators.logout_xpath).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locators.login_register_xpath)))

    def click_on_main_menu(self, menu):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, Locators.shop_by_categories_xpath)))
        self.driver.find_element_by_xpath(Locators.shop_by_categories_xpath).click()
        main_menu = self.driver.find_element_by_xpath(Locators.mega_menu_path.format(menu))
        self.driver.execute_script("arguments[0].click();", main_menu)
        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, main_menu)))
        #self.driver.find_element_by_xpath(main_menu).click()

    def click_on_sub_menu(self, parentmenu, submenu):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, Locators.shop_by_categories_xpath)))
        self.driver.find_element_by_xpath(Locators.shop_by_categories_xpath).click()
        main_menu = self.driver.find_element_by_xpath(Locators.mega_menu_path.format(parentmenu))
        self.driver.execute_script("arguments[0].click();", main_menu)
        #self.driver.find_element_by_xpath(main_menu).click()
        sub_menu = Locators.product_main_menu_xpath.format(submenu)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, sub_menu)))
        self.driver.find_element_by_xpath(sub_menu).click()

