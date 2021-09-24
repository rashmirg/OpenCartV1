import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
import os
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen #for logging


class Test_001_AccountReg:
    # baseURL = "https://demo.opencart.com/"
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() # for logging

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("****test_001_AccountRegistration started")
        self.driver = setup
        self.logger.info("***** Launching Application *****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("***clicking on my account->Register*****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)
        self.logger.info("***** providing customer details for registration   *****")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        print(self.email)
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()

        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account Registration Passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account Registration Failed")
            self.driver.close()
            assert False
        self.logger.info("***** test_001_AccountRegistration finished *****")
