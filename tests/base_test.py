import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.constants import TimeoutVariables, Urls


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(TimeoutVariables.IMPLICIT_WAIT.value)
        cls.driver.get(Urls.HOME_PAGE.value)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
