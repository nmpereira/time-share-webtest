from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('chromedriver')

link_1='https://time-share.up.railway.app/'
urlSuffix='api/times/time/'
url_Id='62349f14902940fcceb0ebfb'
driver.get(link_1+urlSuffix+url_Id)

def SpecificUrl(link,suffix,id):
    driver.get(link+suffix+id)

def Case1(value):
    # for i in range(value):
    SpecificUrl(link_1,urlSuffix,url_Id)
    el = WebDriverWait(driver,timeout=5).until(lambda d: d.find_element_by_id('timestamp')).text != "Loading..."
    # assert el.text != "Loading..."
    result = driver.find_element_by_id('timestamp').text
    print(result)

    # driver.quit()


Case1(10)




# test1: load specific url and see if timer loads
# test2: load specific url multiple times
# test3: load homepage and see if timer loads
# test4: load specific url and see how long timer takes to load
# test5: load homepage and see how long timer takes to load


