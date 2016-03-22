from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import *
from Tests.pages.add_movie_page import AddMoviePage
from Tests.pages.home_page import HomePage
from Tests.pages.login_page import LoginPage
from Tests.pages.internal_page import InternalPage
class Application(object):

    def __init__(self, driver, base_url):
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.add_movie_page = AddMoviePage(driver, base_url)
        self.home_page = HomePage(driver,base_url)

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

    def add_new_movie(self, user):
        anm = self.add_movie_page
        anm.is_this_page
        anm.imdb_number_field.clear()
        anm.imdb_number_field.send_keys('123456')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.also_known_as_field.clear()
        anm.also_known_as_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')
        anm.title_field.clear()
        anm.title_field.send_keys('test movie again')



