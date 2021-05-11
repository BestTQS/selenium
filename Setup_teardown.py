import unittest
from selenium import webdriver
from time import sleep

class Baidu_test(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.baidu.com")
        sleep(2)
        self.driver = driver

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("test")
        self.driver.find_element_by_id("su").click()
        sleep(1)

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("is")
        self.driver.find_element_by_id("su").click()
        sleep(1)

    def test_03(self):
        self.driver.find_element_by_id("kw").send_keys("ok")
        self.driver.find_element_by_id("su").click()
        sleep(1)

