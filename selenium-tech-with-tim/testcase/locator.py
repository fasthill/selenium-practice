from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")  # python homepage에서 버튼 -> inspect 하면 id == 'submit' 임

class SearchResultsPageLocators(object):
    pass
