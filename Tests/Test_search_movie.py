from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import unittest, time, re
import MySQLdb

class searchMovie(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.db = MySQLdb.connect(host='localhost', user='root', passwd='', db='php4dvd', charset='utf8')

    def test_search_All_Movies_In_Databases(self):
        cursor = self.db.cursor()
        sql = """SELECT name FROM movies"""
        cursor.execute(sql)
        data = cursor.fetchall()
        driver = self.driver
        wait = WebDriverWait(driver,10)
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
            search = driver.find_element_by_id('q')
            for rec in data:
                search.send_keys(rec)
                search.send_keys(Keys.RETURN)
                search.clear()
                found_Movie = wait.until(
                    visibility_of_element_located((By.CSS_SELECTOR,'div[id^="movie"]'))
                )
            time.sleep(5)
            driver.quit()


if __name__ == "__main__":
    unittest.main()


