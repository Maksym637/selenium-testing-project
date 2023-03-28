import unittest 
from selenium import webdriver


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.get("http://localhost:3000/home")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
