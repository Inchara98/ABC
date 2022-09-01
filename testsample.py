from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from utilities.readProperties import ReadConfig
from selenium.webdriver import ActionChains
import time

# dirpath = ReadConfig()
# pageobjects = Program_Objects()
# driver = dirpath.get_chrome_browser()
# driver.implicitly_wait(50)
# driver.maximize_window()
# count = 0
# blue_marks = 0
# white_marks = 0
# time.sleep(2)
# map_data = []
#
# driver.get("https://cqube-nvskpack.tibilprojects.com/")
# time.sleep(5)
#
# driver.find_element(By.ID, "menu-item-1").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[contains(text(),'District wise Status')]").click()
# time.sleep(3)
# values = driver.find_elements(By.CSS_SELECTOR, 'tspan.highcharts-text-outline')
# lst = driver.find_elements(By.CSS_SELECTOR, "rect.highcharts-point")
# stateList = []
# Scores = []
# for x in range(1, len(lst)):
#     act = ActionChains(driver)
#     act.move_to_element(lst[x]).perform()
#     act.pause(5)
#     state_names = driver.find_element(By.XPATH, "//*[@class='highcharts-label highcharts-tooltip "
#                                                 "highcharts-color-undefined']/*/*[1]")
#     stateList.append(state_names.text)
# for j in range(len(stateList)):
#     st_name = stateList[j]
#     if st_name != st_name.lower() and st_name != st_name.upper() and "_" not in st_name:
#         print(st_name, "State Name Options are present and displayed on UI")
#     else:
#         print(st_name, type(st_name), 'is not in camel case')
# driver.find_element(By.XPATH, pageobjects.choose_states).click()
# time.sleep(3)
# # state_options = driver.find_elements(By.CLASS_NAME, "ng-option-label ng-star-inserted")
# for i in range(1, 37):
#     state_ids = driver.find_element(By.XPATH, "//div[starts-with(@id,'a')][" + str(i) + "]")
#     state_ids.click()
#     time.sleep(4)
#     driver.find_element(By.XPATH, pageobjects.choose_states).click()
#     time.sleep(2)

lines = 3
bars = lines/2
print(round(bars))