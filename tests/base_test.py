import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.get("http://localhost:3000/home")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
