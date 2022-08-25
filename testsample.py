import logging
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from PageObjects.Dashboard_Page import Dashboard_Objects
from utilities import login_logGen
from utilities.readProperties import ReadConfig

pageobjects = Dashboard_Objects()

logger = login_logGen.setup_logger('log_pl', 'Logs/login.log', level=logging.DEBUG)

dirpath = ReadConfig()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()

driver.get("https://cqube-nvskpack.tibilprojects.com/")
time.sleep(5)
logger.info("browser opened ")
actual_window = driver.get_window_size()
driver.find_element(By.ID, "menu-item-1").click()
time.sleep(3)

driver.find_element(By.XPATH, "//ng-select[@id ='filter-Program']//div[@role='combobox']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@role='option']/span[contains(text(),'NISHTHA 3.0')]").click()
time.sleep(2)
