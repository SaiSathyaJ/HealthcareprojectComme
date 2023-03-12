import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = r"C:\Users\Lenovo\PycharmProjects\HealthcareprojectComm\TestData\LoginData.xlsx"
    logger = LogGen.loggen()
    logger.info("Started writing")

    def test_login_DDT(self, setup):

        self.logger.info("**************Test_003_DDT_LoginTest **************")
        self.logger.info("**************Verifying Login test**************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = ExcelUtils.getRowcount(self.path, "Sheet1")
        print("Number of rows in an excel:", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("***** Failed *****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")
        print("list status is", lst_status)
        if "Fail" not in lst_status:
            self.logger.info("**********DDT login test Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("************DDT login test failed *****")
            self.driver.close()
            assert False

        self.logger.info("*************End of Login DDT test **********")
        self.logger.info("*************Completed Test_003_DDT_LoginTest *******************")
