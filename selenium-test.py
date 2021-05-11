# coding = utf-8
from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(3)
driver.find_element_by_id("kw").send_keys("Test search")
driver.find_element_by_id("su").click()
sleep(3)

driver.quit()