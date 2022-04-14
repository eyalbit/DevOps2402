from selenium import webdriver
from  time import sleep
my_driver = webdriver.Chrome()
my_driver.get("C:/Users/eyal.bitan/Downloads/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[4]").click()
my_driver.find_element_by_id("calculate").click()
escected = "3.01"
actual = my_driver.find_element_by_id("tip").text
assert escected == actual

#print(total_tip)