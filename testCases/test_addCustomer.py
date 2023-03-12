
import pytest
import time
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen
from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer

class TestAddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("************* TestAddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomersMenu()
        self.add_cust.clickOnCustomersMenuItem()

        self.add_cust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword("test123")
        self.add_cust.setCustomerRoles("Guests")
        self.add_cust.setManagerOfVendor("Vendor 2")
        self.add_cust.setGender("Male")
        self.add_cust.setFirstName("Sai")
        self.add_cust.setLastName("Sathya")
        self.add_cust.setDob("3/16/1996")  # Format: D / MM / YYY
        self.add_cust.setCompanyName("SmartSDET")
        self.add_cust.setAdminContent("This is for testing.........")
        self.add_cust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        # print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
