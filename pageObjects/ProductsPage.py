import time

from selenium.webdriver.common.by import By


class ProductsPage:

    #fields in the products page
    lnkCatalog_menu_xpath="//p[normalize-space()='Catalog']//i[contains(@class,'right fas fa-angle-left')]"
    lnkProducts_menu_xpath="//p[normalize-space()='Products']"
    lnkAdd_new_xpath="//a[@class='btn btn-primary']"
    txtProductName_id="Name"
    txtShortdescription_id="ShortDescription"
    txtFulldescription_xpath="//iframe[@id='FullDescription_ifr']"
    txtSKU_id="Sku"
    drpCategories_Select_xpath="(//input[@role='listbox'])[1]"
    drpCategories_xpath="//*[@id='SelectedCategoryIds_listbox']/li[2]"
    drpManufacturers_Select_xpath="//*[@id='product-info']/div[2]/div[3]/div[2]/div/div"
    drpManufacturers_id="9a2492b3-6b88-4085-9a70-0fc6033f65f7"
    lnkSave_xpath="//button[@name='save']"
    finProductAdded_xpath="//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCatalogPage(self):
        self.driver.find_element(By.XPATH, self.lnkCatalog_menu_xpath).click()

    def clickOnProductsPage(self):
        self.driver.find_element(By.XPATH, self.lnkProducts_menu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.lnkAdd_new_xpath).click()

    def ProductName(self,productname):
        self.driver.find_element(By.ID, self.txtProductName_id).send_keys(productname)

    def Shortdescription(self,Shortdescription):
        self.driver.find_element(By.ID, self.txtShortdescription_id).send_keys(Shortdescription)

    def Fulldescription(self,description):

        self.driver.find_element(By.XPATH, self.txtFulldescription_xpath).send_keys(description)


    def SKU(self,sku):
        self.driver.find_element(By.ID, self.txtSKU_id).send_keys(sku)

    def clickOndrpCategories_Select(self):
        self.driver.find_element(By.XPATH, self.drpCategories_Select_xpath).click()

    def setdrpCategories_DRP(self):
        self.driver.find_element(By.LINK_TEXT, self.drpCategories_xpath).click()

    def Clickonmanufacturers(self):
        self.driver.find_element(By.CLASS_NAME, self.drpManufacturers_Select_xpath).click()

    def Clickonmanufacturers_DRP(self):
        self.driver.find_element(By.ID, self.drpManufacturers_id).click()

    def SaveLink(self):
        self.driver.find_element(By.XPATH, self.lnkSave_xpath).click()

    def ProductAdded(self):
        return self.driver.find_element(By.XPATH, self.finProductAdded_xpath).text
