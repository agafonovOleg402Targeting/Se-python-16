from selenium.webdriver.common.by import By
from page import Page

class AddMoviePage(Page):

    @property
    def imdb_number_field(self):
        return self.driver.find_element_by_name('imdbid')

    @property
    def title_field(self):
        return self.driver.find_element_by_name('name')

    @property
    def also_known_as_field(self):
        return self.driver.find_element_by_name('name')

    @property
    def year(self):
        return self.driver.find_element_by_name('year')

    @property
    def duration(self):
        return self.driver.find_element_by_name('duration')

    @property
    def rating(self):
        return self.driver.find_element_by_name('rating')

    @property
    def i_own(self):
        return self.driver.find_element_by_id('own_no')

    @property
    def i_have_seen(self):
        return self.driver.find_element_by_id('seen_yes')

    @property
    def loaned_out(self):
        return self.driver.find_element_by_id('loaned_yes')

    @property
    def trailer(self):
        return self.driver.find_element_by_name('trailer')

    @property
    def personal_notes(self):
        return self.driver.find_element_by_name('notes')

    @property
    def taglines(self):
        return self.driver.find_element_by_name('taglines')

    @property
    def plot_outline(self):
        return self.driver.find_element_by_name('plotoutline')

    @property
    def plots(self):
        return self.driver.find_element_by_name('plots')

    @property
    def language(self):
        return self.driver.find_element_by_id('text_languages_0')

    @property
    def subtitles(self):
        return self.driver.find_element_by_name('subtitles')

    @property
    def audio(self):
        return self.driver.find_element_by_name('audio')

    @property
    def video(self):
        return self.driver.find_element_by_name('video')

    @property
    def country(self):
        return self.driver.find_element_by_name('country')

    @property
    def genres(self):
        return self.driver.find_element_by_name('genres')

    @property
    def director(self):
        return self.driver.find_element_by_name('director')

    @property
    def writer(self):
        return self.driver.find_element_by_name('writer')

    @property
    def producer(self):
        return self.driver.find_element_by_name('producer')

    @property
    def music(self):
        return self.driver.find_element_by_name('music')

    @property
    def cast(self):
        return self.driver.find_element_by_name('cast')

    @property
    def save(self):
        return self.driver.find_element_by_id('submit')

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, 'imdbsearchform'))