from selenium import webdriver
from get_directory import DirectoryPath
import logging
import time
from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from reusable_func import re_call_func
from utilities import Programs_logGen


class Test_Manager_dashboard:

    p = DirectoryPath()
    driver = webdriver.Chrome(executable_path=p.get_driver_path())
    driver.maximize_window()
    driver.get("https://cqube-nvskpack.tibilprojects.com/")
    driver.implicitly_wait(30)
    time.sleep(3)
    resue = re_call_func(driver)
    driver.find_element(By.ID, "menu-item-1").click()
    time.sleep(3)
    pageobjects = Program_Objects()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)

    def test_click_the_nishtha_button(self):
        self.driver.find_element(By.ID, "menu-item-1").click()
        time.sleep(3)
        if 'nishtha' in self.driver.current_url:
            print("Nishtha screen is displaying")
        else:
            print("Nishtha page is not showing ")
            assert False
        self.driver.find_element(By.ID, "menu-item-0").click()
        time.sleep(3)
        print(self.driver.current_url)
        self.driver.find_element(By.ID, "menu-item-1").click()
        time.sleep(3)

    def test_click_on_course_and_medium_tab(self):
        self.driver.find_element(By.ID, "menu-item-1").click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(3)
        result = self.driver.find_element(By.ID, self.pageobjects.CM_status).get_attribute('aria-selected')
        if "true" == result:
            assert True
            self.logger.info("************* Courses and Medium status is clicked *************")
        else:
            self.logger.error("**************** Courses and medium status tab is not clicked *********************")
            assert False

    def test_check_table_state_headers_clickable(self):
        self.logger.info("**************Clicking table headers *****************")
        self.driver.find_element(By.ID, self.pageobjects.nishtha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, self.pageobjects.state_sort).get_attribute('aria-sort')

        self.driver.find_element(By.XPATH, self.pageobjects.state_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.pageobjects.state_sort).get_attribute('aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("state Header is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(now, "******** Status Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if sec_click == 'ascending' or "descending":
            assert True
        else:
            self.logger.error(sec_click, "******** Status Header sorting is not working ***********")
            assert False

    def test_check_table_courses_headers_clickable(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        status = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        now = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("state Header is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(status, now, "********Course launched Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if sec_click == 'ascending' or "descending":
            self.logger.info("state Header is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(status, now, "********Course launched Header sorting is not working ***********")
            assert False

    def test_check_table_mediums_headers_clickable(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        status = self.driver.find_element(By.XPATH, self.pageobjects.medium_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.pageobjects.medium_header).click()
        now = self.driver.find_element(By.XPATH, self.pageobjects.medium_sort).get_attribute('aria-sort')
        if status != now:
            assert True
            self.logger.info("*********** Courses Launched table header is Sorting working *****************")
        else:
            self.logger.error(status, now, "******** Course launched Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if sec_click == 'ascending' or "descending":
            self.logger.info("state Header is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(status, now, "******** Medium Header sorting is not working ***********")
            assert False

    def test_check_state_table_values(self):
        state_tablevals = []
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        state_name = self.driver.find_elements(By.XPATH, self.pageobjects.state_values)
        for i in range(1, len(state_name)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[1]")
            state_tablevals.append(state_list.text)
        if len(state_tablevals) == len(state_name)-1:
            self.logger.info("************ State Table values are showing ****************")
            assert True
        else:
            self.logger.error("************ State names are not showing **************")
            assert False

    def test_check_course_table_values(self):
        course_tablevals = []
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        course_name = self.driver.find_elements(By.XPATH, self.pageobjects.course_values)
        for i in range(1,len(course_name)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[2]")
            course_tablevals.append(state_list.text)
        if len(course_tablevals) == len(course_name)-1:
            assert True
            self.logger.info("************ Course Table Values are showing ****************")
        else:
            self.logger.error("************ Course Values are not showing **************")
            assert False
        for i in range(len(course_tablevals)):
            if course_tablevals[i] is not str and course_tablevals[i] is not None:
                self.logger.info("*********** Course Values are Integers  *************")
                assert True
            else:
                self.logger.error("*********** Course Values are Not Integers *************")
                assert False

    def test_check_medium_table_values(self):
        medium_tablevals = []
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        medium_val = self.driver.find_elements(By.XPATH, self.pageobjects.medium_values)
        for i in range(1,len(medium_val)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[3]")
            medium_tablevals.append(state_list.text)
        if len(medium_tablevals) == len(medium_val)-1:
            assert True
            self.logger.info("************ Medium Table Values are showing ****************")
        else:
            self.logger.error(len(medium_tablevals), len(medium_val),
                              "************ Medium Values are not showing **************")
            assert False
        for i in range(len(medium_tablevals)):
            if medium_tablevals[i] is not str:
                self.logger.info("*********** Medium Values are Integers  *************")
                assert True
            else:
                self.logger.error("*********** Course Values are Not Integers *************")
                assert False

    def test_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        a_minus = self.resue.test_click_on_A_minus_button()
        if a_minus == 0:
            print("value :",a_minus)
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        a_plus = self.resue.test_click_on_A_default_button()
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False
