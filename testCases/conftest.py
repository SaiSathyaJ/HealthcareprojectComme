from selenium import  webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Edge':
        driver=webdriver.Edge()
        print("launching chrome browser..........")

    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser..........")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):  ##This will get the values from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##########Pytest HTML report#############

#it is hook for adding environment info in to HTML report
def pytest_configure(config):
    config._metadata['Project Name']='Healthcare Practice'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Sai'

#it is hook for delete/modify environment info in to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)