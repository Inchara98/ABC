import logging

from selenium.webdriver.common.by import By

from PageObjects.Dashboard_Page import Dashboard_Objects
from utilities import login_logGen
from utilities.readProperties import ReadConfig
from selenium.webdriver import ActionChains
import time
import pandas as pd

pageobjects = Dashboard_Objects()

# logger = login_logGen.setup_logger('log_pl', 'Logs/login.log', level=logging.DEBUG)
#
dirpath = ReadConfig()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()
#
driver.get("https://cqube-nvskpack.tibilprojects.com/")
time.sleep(5)
#
# driver.implicitly_wait(20)
# # driver.get("https://cqube-release.tibilprojects.com/")
# time.sleep(3)
# driver.find_element(By.ID, "username1").send_keys("admin")
# driver.find_element(By.ID, "password1").send_keys("Tibil@123")
# driver.find_element(By.ID, "login").click()
# driver.find_element(By.XPATH, '//*[@id="cQb_dhsbrd"]').click()
# time.sleep(2)

driver.find_element(By.ID, "menu-item-1").click()
time.sleep(5)
# driver.find_element(By.XPATH, "//*[contains(text(),'Implementation Status')]").click()
# time.sleep(3)
lst = driver.find_elements(By.CLASS_NAME, "leaflet-interactive")
print("No of States", len(lst) - 1)
count = 0
blue_marks = 0
white_marks = 0
time.sleep(2)
map_data = []
for x in range(1, len(lst)):
    if lst[x].get_attribute('fill') == '#FFFFFF':
        white_marks = white_marks + 1
    else:
        blue_marks = blue_marks + 1
    act = ActionChains(driver)
    act.move_to_element(lst[x]).perform()
    act.pause(2)
    txt = driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
    print(txt.text)
    if txt.text is not None and txt.text not in 'No':
        print(txt.text, ' is not empty tooltip')
    else:
        print('Tooltip is empty')
        count = count + 1
    map_data.append(txt.text)

if "NISHTHA 1.0" in map_data[0]:
    print("NISHTHA 1.0 IS PRESENT IN MAP TOOLTIP ")
else:
    print("NISHTHA 1.0 IS NOT PRESENT ")

