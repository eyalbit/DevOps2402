from selenium import webdriver
from  time import sleep

from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome()


def open_web(url, titleXPath, element):
    my_driver.get(url)
    print(url)
    if element == "title":
        return my_driver.title #.find_element(by=By.XPATH, value=titleXPath).text
    elif element == "sitename":
        return my_driver.name.encode()



#walla_title = open_web("http://www.walla.co.il","//*[@id=\"root\"]/div/div[2]/section[2]/section/article/a/h2")

ynet_title = open_web("http://www.ynet.co.il", "//*[@id='B1bLNJeyIkX9']/h1/span", "sitename")
walla_sitename = open_web("http://www.walla.co.il", "//*[@id='root']/div/div[2]/section[2]/section/article/a/h2", "title")
if ynet_title == walla_sitename:
    print("true")
else:
    print("false")
print(ynet_title)
print(walla_sitename.encode("utf-8"))