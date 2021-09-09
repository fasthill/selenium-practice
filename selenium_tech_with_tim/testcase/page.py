from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = 'q'  # in python home page the name is 'q'

class GoButtonElement(BasePageElement):
    locator = 'go'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)  # * unpack
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source


if __name__ == "__main__":
    print('Good')
