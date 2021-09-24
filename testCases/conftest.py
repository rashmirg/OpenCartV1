from datetime import datetime
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(browser):
    print(browser)
    if(browser=='edge'):
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge Browser")
    elif(browser=='firefox'):
        driver=webdriver.firefox(GeckoDriverManager().install())
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser ")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#generating pytest HTML reports

def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Rashmi'
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%m-%d-%Y %H-%M-%S") + ".html"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%m-%d-%Y %H-%M-%S")+".html"
