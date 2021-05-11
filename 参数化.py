import pandas as pd
from selenium import webdriver
from time import sleep
def excel_data():
    data = pd.read_excel("D:/Star/Pytest/test.xlsx")
    a = data.iloc[:, 0]   #读取单列参数
    print(len(a))
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    for i in range(0,len(data.iloc[:, 0])):
        driver.find_element_by_id("kw").send_keys(data.iloc[i, 0])
        sleep(2)
        driver.find_element_by_id("su").click()
        sleep(1)
        driver.find_element_by_id("kw").clear()
        i = 1 + i

    sleep(2)
    driver.quit()

if __name__ == '__main__':
    excel_data()

'''
Excel 表内信息

    username
0    aaa
1    bbb
2    ccc
3    ddd
4    eee
5    fff
6    ggg

'''