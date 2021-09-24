from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    lnk_myaccount_xpath = "//a[@title='My Account']"
    lnk_register_xpath ="//*[@id='top-links']/ul/li[2]/ul/li[1]/a"
    lnk_login_linktext = "Login"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()