import configparser
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Dashboard_Page import Dashboard_Objects
from utilities.readProperties import ReadConfig

pageobjects = Dashboard_Objects()
dirpath = ReadConfig()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()

driver.get("https://cqube-nvskpack.tibilprojects.com/")
time.sleep(5)

driver.find_element(By.ID, "menu-item-1").click()
time.sleep(3)

drop = driver.find_element(By.XPATH, "//*[@id='filter-Program']/div/span[2]")
drop.click()

time.sleep(3)

driver.find_element(By.ID,"ae8a8c87ace0-1").click()
time.sleep(5)
