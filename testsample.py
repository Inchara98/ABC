import time

from selenium.webdriver.common.by import By

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

a = driver.find_element(By.ID, "font-size-reset")
print(a.value_of_css_property('font-size'))
a.click()
if 'style="font-size: 16px;"' in driver.page_source:
    print("A button is clicked ")
    assert True
else:
    assert False

a_plus = driver.find_element(By.ID, "font-size-increase")
a_plus.click()
if 'style="font-size: 18px;"' in driver.page_source:
    print("A+ button is clicked ")
    assert True
else:
    assert False
a_minus = driver.find_element(By.ID, "font-size-decrease")
a_minus.click()
if 'style="font-size: 16px;"' in driver.page_source:
    print("A- button is clicked ")
    assert True
else:
    assert False


