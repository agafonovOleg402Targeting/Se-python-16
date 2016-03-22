from selenium.webdriver.common.by import By

from Tests.pages.page import Page


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
    def year_field(self):
        return self.driver.find_element_by_name('year')

    @property
    def duration_field(self):
        return self.driver.find_element_by_name('duration')

    @property
    def rating_field(self):
        return self.driver.find_element_by_name('rating')

    @property
    def i_own_field(self):
        return self.driver.find_element_by_id('own_no')

    @property
    def i_have_seen_field(self):
        return self.driver.find_element_by_id('seen_yes')

    @property
    def loaned_out_field(self):
        return self.driver.find_element_by_id('loaned_yes')

    @property
    def trailer_field(self):
        return self.driver.find_element_by_name('trailer')

    @property
    def personal_notes_field(self):
        return self.driver.find_element_by_name('notes')

    @property
    def taglines_field(self):
        return self.driver.find_element_by_name('taglines')

    @property
    def plot_outline_field(self):
        return self.driver.find_element_by_name('plotoutline')

    @property
    def plots_field(self):
        return self.driver.find_element_by_name('plots')

    @property
    def language_field(self):
        return self.driver.find_element_by_id('text_languages_0')

    @property
    def subtitles_field(self):
        return self.driver.find_element_by_name('subtitles')

    @property
    def audio_field(self):
        return self.driver.find_element_by_name('audio')

    @property
    def video_field(self):
        return self.driver.find_element_by_name('video')

    @property
    def country_field(self):
        return self.driver.find_element_by_name('country')

    @property
    def genres_field(self):
        return self.driver.find_element_by_name('genres')

    @property
    def director_field(self):
        return self.driver.find_element_by_name('director')

    @property
    def writer_field(self):
        return self.driver.find_element_by_name('writer')

    @property
    def producer_field(self):
        return self.driver.find_element_by_name('producer')

    @property
    def music_field(self):
        return self.driver.find_element_by_name('music')

    @property
    def cast_field(self):
        return self.driver.find_element_by_name('cast')

    @property
    def save_field(self):
        return self.driver.find_element_by_id('submit')

    @property
    def is_this_page_field(self):
        return self.is_element_visible((By.ID, 'imdbsearchform'))