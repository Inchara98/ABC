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

logger = login_logGen.setup_logger('log_pl','Logs/login.log', level=logging.DEBUG)

dirpath = ReadConfig()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()

# driver.get("https://cqube-nvskpack.tibilprojects.com/")
# time.sleep(5)
# logger.info("browser opened ")
# actual_window = driver.get_window_size()
# driver.find_element(By.ID, "menu-item-1").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH, "//button/i").click()
# time.sleep(3)
#
# logger.info("Zoom icon is clicked ")
# after_window = driver.get_window_size()
# # driver.execute_script("window.stop();")
# action = ActionChains(driver)
# action.send_keys(Keys.ESCAPE).perform()
#
# time.sleep(3)
# driver.close()

logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)

