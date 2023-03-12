
import pytest
import time
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen
from pageObjects.LoginPage import Login
from pageObjects.ProductsPage import ProductsPage

class TestAddProduct:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_add_Product(self, setup):
        self.logger.info("************* TestAddProduct **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Adding Product Test **********")

        self.add_prod=ProductsPage(self.driver)
        self.add_prod.clickOnCatalogPage()
        self.add_prod.clickOnProductsPage()
        self.add_prod.clickOnAddNew()

        self.logger.info("************* Providing Product info **********")
        self.ProductName=random_generator()
        self.add_prod.ProductName(self.ProductName)
        self.add_prod.Shortdescription("Wealthy Product")


#         self.add_prod.Fulldescription("The Bluetooth icon is missing or Bluetooth can't be turned on or off.\
# Bluetooth doesn't work after a Windows 10 update is installed.")
        self.add_prod.SKU("SKU")
        # self.add_prod.clickOndrpCategories_Select()
        # time.sleep(3)
        # self.add_prod.setdrpCategories_DRP()
        # self.add_prod.Clickonmanufacturers()
        # time.sleep(3)
        # self.add_prod.Clickonmanufacturers_DRP()
        self.add_prod.SaveLink()
        self.res=self.add_prod.ProductAdded()
        if "The new product has been added successfully" in self.res:
            assert True
        else:
            print("The result is -",self.res,"--")
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))