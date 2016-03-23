from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from Tests.pages.add_movie_page import AddMoviePage
from Tests.pages.home_page import HomePage
from Tests.pages.login_page import LoginPage
from Tests.pages.internal_page import InternalPage
from Tests.pages.main_page import MainPage
from User import User
import MySQLdb
from selenium.webdriver.common.keys import Keys
import time



class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.add_movie_page = AddMoviePage(driver, base_url)
        self.home_page = HomePage(driver,base_url)
        self.main_page = MainPage(driver,base_url)
        self.db = MySQLdb.connect(host='localhost', user='root', passwd='', db='php4dvd', charset='utf8')

    def login(self,user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def add_new_movie(self):
        anm = self.add_movie_page
        mp = self.main_page
        mp.add_button.click()
        anm.imdb_number_field.clear()
        anm.imdb_number_field.send_keys('123456')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.also_known_as_field.clear()
        anm.also_known_as_field.send_keys('test movie again')
        anm.year_field.clear()
        anm.year_field.send_keys('2016')
        anm.duration_field.clear()
        anm.duration_field.send_keys('duration_field')
        anm.rating_field.clear()
        anm.rating_field.send_keys('5,9')
        anm.i_own_field.click()
        anm.i_have_seen_field.click()
        anm.loaned_out_field.click()
        anm.trailer_field.clear()
        anm.trailer_field.send_keys('http://software-testing.ru/lms/course/view.php?id=349')
        anm.personal_notes_field.clear()
        anm.personal_notes_field.send_keys('Personal Notes')
        anm.taglines_field.clear()
        anm.taglines_field.send_keys('#tag')
        anm.plot_outline_field.clear()
        anm.plot_outline_field.send_keys('plotoutline')
        anm.plots_field.clear()
        anm.plots_field.send_keys('plots')
        anm.language_field.clear()
        anm.language_field.send_keys('English, Germany, Russian')
        anm.subtitles_field.clear()
        anm.subtitles_field.send_keys('Yes')
        anm.audio_field.clear()
        anm.audio_field.send_keys('audio')
        anm.video_field.clear()
        anm.video_field.send_keys('video')
        anm.country_field.clear()
        anm.country_field.send_keys('country')
        anm.genres_field.clear()
        anm.genres_field.send_keys('genres')
        anm.director_field.clear()
        anm.director_field.send_keys('director')
        anm.writer_field.clear()
        anm.writer_field.send_keys('writer')
        anm.producer_field.clear()
        anm.producer_field.send_keys('producer')
        anm.music_field.clear()
        anm.music_field.send_keys('music')
        anm.cast_field.clear()
        anm.cast_field.send_keys('cast')
        anm.save_button.click()
        anm.is_this_page_with_new_movie

    def fail_add_new_movie(self):
        anm = self.add_movie_page
        mp = self.main_page
        mp.add_button.click()
        anm.imdb_number_field.clear()
        anm.imdb_number_field.send_keys('123456')
        anm.title_field.clear()
        anm.also_known_as_field.clear()
        anm.also_known_as_field.send_keys('test movie again')
        anm.year_field.clear()
        anm.year_field.send_keys('2016')
        anm.duration_field.clear()
        anm.duration_field.send_keys('duration_field')
        anm.rating_field.clear()
        anm.rating_field.send_keys('5,9')
        anm.i_own_field.click()
        anm.i_have_seen_field.click()
        anm.loaned_out_field.click()
        anm.trailer_field.clear()
        anm.trailer_field.send_keys('http://software-testing.ru/lms/course/view.php?id=349')
        anm.personal_notes_field.clear()
        anm.personal_notes_field.send_keys('Personal Notes')
        anm.taglines_field.clear()
        anm.taglines_field.send_keys('#tag')
        anm.plot_outline_field.clear()
        anm.plot_outline_field.send_keys('plotoutline')
        anm.plots_field.clear()
        anm.plots_field.send_keys('plots')
        anm.language_field.clear()
        anm.language_field.send_keys('English, Germany, Russian')
        anm.subtitles_field.clear()
        anm.subtitles_field.send_keys('Yes')
        anm.audio_field.clear()
        anm.audio_field.send_keys('audio')
        anm.video_field.clear()
        anm.video_field.send_keys('video')
        anm.country_field.clear()
        anm.country_field.send_keys('country')
        anm.genres_field.clear()
        anm.genres_field.send_keys('genres')
        anm.director_field.clear()
        anm.director_field.send_keys('director')
        anm.writer_field.clear()
        anm.writer_field.send_keys('writer')
        anm.producer_field.clear()
        anm.producer_field.send_keys('producer')
        anm.music_field.clear()
        anm.music_field.send_keys('music')
        anm.cast_field.clear()
        anm.cast_field.send_keys('cast')
        anm.save_button.click()
        anm.error_message


    def delete_movie(self):
        anm = self.add_movie_page
        mp = self.main_page
        mp.no_movies
        mp.movie_for_delete.click()
        mp.remove_button.click()
        mp.alert_when_delete
        anm.is_this_page

    def search_movie(self):
        mp = self.main_page
        cursor = self.db.cursor()
        sql = """SELECT name FROM movies"""
        cursor.execute(sql)
        data = cursor.fetchall()
        mp.no_movies
        for rec in data:
                mp.search_field.send_keys(rec)
                mp.search_field.send_keys(Keys.RETURN)
                mp.search_field.clear()
                time.sleep(10) #***Waiting for downloading a list of 10 seconds***
                mp.is_this_found_movie
                mp.there_is_movie

    def fail_search_movie(self):
        mp = self.main_page
        mp.search_field.send_keys("123456789444555")
        mp.search_field.send_keys(Keys.RETURN)
        mp.no_movies