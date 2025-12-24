import pytest
import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    serv_obj = Service("driver/geckodriver.exe")
    driver = webdriver.Firefox(service=serv_obj)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def read_data_from_csv(file_path="testdata/testdata.csv"):
    with open(file_path,newline='') as datafile:
        reader = csv.DictReader(datafile)
        return [row for row in reader]

@pytest.fixture(params=read_data_from_csv("testdata/testdata.csv"))
def user_data(request):
    return request.param
