# https://selenium-python.readthedocs.io/index.html # selenium with python # 6.1 test case
import unittest

from selenium import webdriver
import page

PATH = '../chromedriver.exe'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print('setup')
        global PATH
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")

# # read below carefully
#     def test_example(self): # should start with "test_" + filename
#         print('Test1')
#         assert True
#
#     def test_example2(self): # should start with "test_" + filename
#         print('Test2')
#         assert True
#
#     def not_a_test(self): # this wont work because the wrong def name. it does not start with "test_"
#         print('this wont print')
#         assert True
# # Important work sequence : ① setUp ② test_example ③ tearDown ④ setUp ⑤ test_example2 ⑥ tearDown

    # def test_title(self):
    #     if __name__ == '__main__':
    #         mainPage = page.MainPage()
    #         assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
