from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Programs_Page import Program_Objects
from utilities.readProperties import ReadConfig

dirpath = ReadConfig()
pageobjects = Program_Objects()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()

driver.get("http://www.google.com")
for elem in driver.find_elements(By.XPATH,'.//span[@class = "gbts"]'):
    print(elem.text)
