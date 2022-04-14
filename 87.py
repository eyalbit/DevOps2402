from selenium import webdriver
from  time import sleep

from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome()
def get_element_from(url, element):
    my_driver.get(url)
    if element == "name":
       return my_driver.name
    elif element == "title":
        return  my_driver.title

#my_driver.get("http://www.walla.co.il")
#txt = my_driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/section[2]/section/article/a/h2").text
#print(txt)

my_driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")

my_driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("שולחן")
my_driver.get("https://www.youtube.com")
my_driver.find_element(By.XPATH, value="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("mozart")
sleep(2)
my_driver.find_element(By.XPATH, value="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()

