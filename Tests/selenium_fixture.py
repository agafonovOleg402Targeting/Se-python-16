from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
	driver = webdriver.Firefox()
	driver.implicity_wait(10)
	request.addfinalizer(driver.quit)
	return driver