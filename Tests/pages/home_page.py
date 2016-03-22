from selenium.webdriver.common.by import By

from Tests.pages.page import Page


class HomePage(Page):

    @property
    def add_movie_button(self):
        return self.driver.find_element_by_css_selector('a[href$="=add"]')

    @property
    def search_field(self):
        return self.driver.find_element_by_id('q')

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, 'a[href$="=add"]'))

