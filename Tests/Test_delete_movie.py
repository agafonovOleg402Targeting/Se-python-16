from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import unittest, time, re

class addNewMovie(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_new_movie(self):
        driver = self.driver
        wait = WebDriverWait(driver,4)
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        results = driver.find_element_by_id('results')
        if results.text == 'No movies where found.':
            time.sleep(5)
            driver.quit()
        else:
            delete_Movie = driver.find_element_by_css_selector('div[id^="movie"]')
            delete_Movie.click()
            delete = driver.find_element_by_css_selector('a[onclick^="if"]')
            delete.click()
            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(5)
            driver.quit()


    if __name__ == "__main__":
        unittest.main()