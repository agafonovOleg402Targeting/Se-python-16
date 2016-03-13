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
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_new_movie(self):
        driver = self.driver
        wait = WebDriverWait(driver,10)
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        add_element = driver.find_element_by_css_selector('a[href$="=add"]')
        add_element.click()
        check_page_opened = wait.until(
            visibility_of_element_located((By.ID,'imdbsearchform'))
        )

        IMDb = driver.find_element_by_name('imdbid')
        IMDb.clear()
        IMDb.send_keys('12345789')
        also_known_as = driver.find_element_by_name('aka')
        also_known_as.clear()
        also_known_as.send_keys('grdrhdrhdrhdrhdrhrhrdh')
        year = driver.find_element_by_name('year')
        year.clear()
        year.send_keys('1991')
        duration = driver.find_element_by_name('duration')
        duration.clear()
        duration.send_keys('123')
        rating = driver.find_element_by_name('rating')
        rating.clear()
        rating.send_keys('5.9')
        i_Own = driver.find_element_by_id('own_no')
        i_Own.click()
        i_Have_Seen = driver.find_element_by_id('seen_yes')
        i_Have_Seen.click()
        loaned_Out = driver.find_element_by_id('loaned_yes')
        loaned_Out.click()
        trailer = driver.find_element_by_name('trailer')
        trailer.clear()
        trailer.send_keys('http://software-testing.ru/lms/course/view.php?id=349')
        personal_Notes = driver.find_element_by_name('notes')
        personal_Notes.clear()
        personal_Notes.send_keys('Personal Notes')
        taglines  = driver.find_element_by_name('taglines')
        taglines.clear()
        taglines.send_keys('#tag')
        plot_Outline = driver.find_element_by_name('plotoutline')
        plot_Outline.clear()
        plot_Outline.send_keys('plotoutline')
        plots = driver.find_element_by_name('plots')
        plots.clear()
        plots.send_keys('plots')
        language = driver.find_element_by_id('text_languages_0')
        language.clear()
        language.send_keys('English, Germany, Russian')
        subtitles = driver.find_element_by_name('subtitles')
        subtitles.clear()
        subtitles.send_keys('Yes')
        audio = driver.find_element_by_name('audio')
        audio.clear()
        audio.send_keys('audio')
        video = driver.find_element_by_name('video')
        video.clear()
        video.send_keys('video')
        country = driver.find_element_by_name('country')
        country.clear()
        country.send_keys('country')
        genres = driver.find_element_by_name('genres')
        genres.clear()
        genres.send_keys('genres')
        director = driver.find_element_by_name('director')
        director.clear()
        director.send_keys('director')
        writer = driver.find_element_by_name('writer')
        writer.clear()
        writer.send_keys('writer')
        producer = driver.find_element_by_name('producer')
        producer.clear()
        producer.send_keys('producer')
        music = driver.find_element_by_name('music')
        music.clear()
        music.send_keys('music')
        cast = driver.find_element_by_name('cast')
        cast.clear()
        cast.send_keys('cast')
        save = driver.find_element_by_id('submit')
        save.click()
        error = driver.find_element_by_name('name')
        assert error.text == ''
        driver.quit()

    if __name__ == "__main__":
        unittest.main()
