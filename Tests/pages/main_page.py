from selenium.webdriver.common.by import By

from Tests.pages.page import Page
import time

class MainPage(Page):

    @property
    def add_button(self):
        return self.driver.find_element_by_css_selector("a[href = './?go=add']")

    @property
    def movie_for_delete(self):
        return self.driver.find_element_by_css_selector('div[id^="movie"]')

    @property
    def no_movies(self):
        if self.driver.find_element_by_id('results').text == 'No movies where found.':
            time.sleep(5)
            self.driver.quit()

    @property
    def remove_button(self):
        return self.driver.find_element_by_css_selector('a[onclick^="if"]')

    @property
    def alert_when_delete(self):
        self.driver.switch_to_alert().accept()

    @property
    def search_field(self):
        return self.driver.find_element_by_id('q')

    @property
    def is_this_found_movie(self):
        return self.is_element_visible((By.CSS_SELECTOR,'div[class="title"]'))

    @property
    def there_is_movie(self):
        assert "No movies where found." not in self.driver.page_source