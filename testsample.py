# import logging

from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from utilities.readProperties import ReadConfig
from selenium.webdriver import ActionChains
import time

dirpath = ReadConfig()
pageobjects = Program_Objects()
driver = dirpath.get_chrome_browser()
driver.implicitly_wait(50)
driver.maximize_window()
count = 0
blue_marks = 0
white_marks = 0
time.sleep(2)
map_data = []

driver.get("https://cqube-nvskpack.tibilprojects.com/")
time.sleep(5)

driver.find_element(By.ID, "menu-item-1").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(),'District wise Status')]").click()
time.sleep(3)
values = driver.find_elements(By.CSS_SELECTOR, 'tspan.highcharts-text-outline')
lst = driver.find_elements(By.CSS_SELECTOR, "rect.highcharts-point")
print(len(lst) - 1)
stateList = []
Scores = []
for x in range(1, len(lst)):
    act = ActionChains(driver)
    act.move_to_element(lst[x]).perform()
    act.pause(5)
    state_names = driver.find_element(By.XPATH, "//*[@class='highcharts-label highcharts-tooltip "
                                                "highcharts-color-undefined']/*/*[1]")
    # state_values = driver.find_element(By.XPATH, "//*[@class='highcharts-label highcharts-tooltip "
    #                                              "highcharts-color-undefined']/*/*[@class='highcharts-br']")
    state_values = driver.find_element(By.CLASS_NAME,"highcharts-br")
    state_values.text.__contains__('Total Certifications')
    print(state_values.tag_name)
    stateList.append(state_names.text)
    Scores.append(state_values.text)
    print(state_names.text, state_values.text)

print("State Lists", stateList)
print("Score Lists", Scores)

#     map_data.append(txt.text)
# if len(map_data) == len(lst) - 1:
#     print(len(map_data), len(lst) - 1, "Total tooltip is equal to total bar's ")
# else:
#     print(len(map_data), len(lst) - 1, "Total no of tooltip is not equal to bar's")
#
# if len(values) == len(lst) - 1:
#     print(values, len(lst) - 1, "No of Bar chart and Enrollment/Completion Score")
# else:
#     print(values, len(lst) - 1, "Bars and Enrollment/Completion scores are not matching!...")
#
