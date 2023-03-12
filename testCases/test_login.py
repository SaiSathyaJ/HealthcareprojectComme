import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    logger.info("Started writing")

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("**************Test_001_Login**************")
        self.logger.info("**************Verifying Home Page Title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home Page Title is passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle1.png")
            self.driver.close()
            self.logger.error("**************Home Page Title is failed**************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************Test_002_Login**************")
        self.logger.info("**************Verifying Login test**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************Login test is passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**************Login test is failed**************")
            assert False
