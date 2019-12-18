# encoding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def baidu_search(driver, search_word):
    WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element_by_id('kw'))
    #  输入要爬的关键词
    input_area = driver.find_element_by_id('kw')
    input_area.clear()
    input_area.send_keys(search_word)
    submit_btn = driver.find_element_by_id('su')
    submit_btn.click()


def browser_init(url="https://www.baidu.com"):
    # 启动浏览器
    # 指定浏览器驱动程序路径或者将驱动程序加入环境变量
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    # driver = webdriver.Chrome()

    driver.get(url)
    return driver
