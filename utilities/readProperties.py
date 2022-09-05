import configparser
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from get_directory import DirectoryPath

config = configparser.RawConfigParser()
# config.read("../Configurations/config.ini")
path = Path(__file__)
ROOT_DIR = os.path.abspath("../../../Configurations")
config_path = os.path.join(ROOT_DIR, "config.ini")
config.read(config_path)


class ReadConfig:

    def __int__(self, driver):
        self.driver = driver

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_state_ApplicationURL():
        url = config.get('common info', 'stateURL')
        return url

    @staticmethod
    def get_state_Username():
        username = config.get('common info', 'stateUser')
        return username

    @staticmethod
    def get_state_Password():
        password = config.get('common info', 'statePassword')
        return password

    @staticmethod
    def get_chrome_browser():
        p = DirectoryPath()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # headless enable or disable
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options, executable_path=p.get_driver_path())
        return driver

    @staticmethod
    def get_the_application():
        data = ReadConfig()
        driver = data.get_chrome_browser()
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get(data.getApplicationURL())
        time.sleep(5)
        return driver

    @staticmethod
    def navigate_to_dashboard():
        p = DirectoryPath()
        data = ReadConfig()
        driver = webdriver.Chrome(executable_path=p.get_driver_path())
        driver.maximize_window()
        driver.get(data.getApplicationURL())
        driver.implicitly_wait(30)
        time.sleep(3)
        return driver

    @staticmethod
    def navigate_to_nishtha():
        p = DirectoryPath()
        pageobjects = Program_Objects()
        data = ReadConfig()
        driver = webdriver.Chrome(executable_path=p.get_driver_path())
        driver.maximize_window()
        driver.get(data.getApplicationURL())
        driver.implicitly_wait(30)
        time.sleep(3)
        driver.find_element(By.ID, pageobjects.nishtha).click()
        time.sleep(3)
        return driver

    @staticmethod
    def navigate_to_pm_poshina():
        p = DirectoryPath()
        pageobjects = Program_Objects()
        data = ReadConfig()
        driver = webdriver.Chrome(executable_path=p.get_driver_path())
        driver.maximize_window()
        driver.get(data.getApplicationURL())
        driver.implicitly_wait(30)
        time.sleep(3)
        driver.find_element(By.ID, pageobjects.pm_poshan).click()
        time.sleep(3)
        return driver
    @staticmethod
    def navigate_to_PGI_dashboard():
        p = DirectoryPath()
        pageobjects = Program_Objects()
        data = ReadConfig()
        driver = webdriver.Chrome(executable_path=p.get_driver_path())
        driver.maximize_window()
        driver.get(data.getApplicationURL())
        driver.implicitly_wait(30)
        time.sleep(3)
        driver.find_element(By.ID, pageobjects.pgi_button).click()
        time.sleep(3)
        return driver

    @staticmethod
    def test_click_on_A_default_button(self, driver):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_default)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 16px;"' in self.driver.page_source:
            self.logger.info("************* A button is clicked *************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A button is not clicked *******************")
            count = count + 1
        return count

    @staticmethod
    def test_click_on_A_plus_button(self, driver):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_plus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 18px;"' in self.driver.page_source:
            self.logger.info("************* A+ button is clicked *************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not clicked *******************")
            count = count + 1
        return count

    @staticmethod
    def test_click_on_A_minus_button(self, driver):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_minus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 14px;"' in self.driver.page_source:
            self.logger.info("************* A- button is clicked *************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not clicked *******************")
            count = count + 1
        return count

    @staticmethod
    def test_check_nishtha_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        count = 0
        options = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        if len(options) > 0:
            self.logger.info("************** Program Dropdown Showing Options *******************")
            assert True
        else:
            self.logger.error("****************** Program Dropdown is Empty... *************************")
            count = count + 1
        return count

    @staticmethod
    def test_check_selection_nishtha_2_options(self):
        count = 0
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_2).click()
        time.sleep(2)
        if "NISHTHA 2.0" in self.driver.page_source:
            self.logger.info("************* NISHTHA 2.0 option is selected  ****************")
            assert True
        else:
            self.logger.error("************** NISHTHA 2.0 option is not selected *****************")
            count = count + 1
        return count

    @staticmethod
    def test_check_selection_nishtha_1_options(self, driver):
        count = 0
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_2).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_1).click()
        if "NISHTHA 1.0" in self.driver.page_source:
            self.logger.info("************* NISHTHA 1.0 option is selected  ****************")
            assert True
        else:
            self.logger.error("************** NISHTHA 1.0 option is not selected *****************")
            count = count + 1
        return count

    @staticmethod
    def test_check_selection_nishtha_3_options(self):
        count = 0
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_3).click()
        if "NISHTHA 3.0" in self.driver.page_source:
            self.logger.info("************* NISHTHA 3.0 option is selected  ****************")
            assert True
        else:
            self.logger.error("************** NISHTHA 3.0 option is not selected *****************")
            count = count + 1
        return count

    @staticmethod
    def test_validate_state_column_names(self):
        state_tablevals = []
        count = 0
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        state_name = self.driver.find_elements(By.XPATH, self.pageobjects.state_values)
        for i in range(1, len(state_name)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[1]")
            state_tablevals.append(state_list.text)
        if len(state_tablevals) == len(state_name) - 1:
            self.logger.info("************ State Table values are showing ****************")
            assert True
        else:
            self.logger.error("************ State names are not showing **************")
            count = count + 1
        return count

    @staticmethod
    def test_validate_course_column_validate(self):
        course_tablevals = []
        count = 0
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        course_name = self.driver.find_elements(By.XPATH, self.pageobjects.course_values)
        for i in range(1, len(course_name)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[2]")
            course_tablevals.append(state_list.text)
        if len(course_tablevals) == len(course_name) - 1:
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
                count = count + 1
        return count

    @staticmethod
    def test_validate_medium_column_values(self):
        medium_tablevals = []
        count = 0
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        medium_val = self.driver.find_elements(By.XPATH, self.pageobjects.medium_values)
        for i in range(1, len(medium_val)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[3]")
            medium_tablevals.append(state_list.text)
        if len(medium_tablevals) == len(medium_val) - 1:
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
                count = count + 1
        return count

    # District Wise Status
    @staticmethod
    def test_check_district_program_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.click_district_program).click()
        time.sleep(1)
        count = 0
        options = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        if len(options) > 0:
            self.logger.info("************** Program Dropdown Showing Options *******************")
            assert True
        else:
            self.logger.error("****************** Program Dropdown is Empty... *************************")
            count = count + 1
        return count

    @staticmethod
    def test_check_states_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.click_state_options).click()
        time.sleep(1)
        count = 0
        options = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        if len(options) > 0:
            self.logger.info("************** State Dropdown Showing Options *******************")
            assert True
        else:
            self.logger.error("****************** State Dropdown is Empty... *************************")
            count = count + 1
        return count

    @staticmethod
    def selecting_the_state_dropdown_options(self):
        count = 0
        self.driver.find_element(By.XPATH, self.pageobjects.click_state_options).click()
        time.sleep(1)
        state_list = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        for i in range(len(state_list)):
            state_options = self.driver.find_element(By.ID, self.pageobjects.state_names_id + str(i))
            state_options.click()
            statename = self.driver.find_element(By.ID, self.pageobjects.state_names_id + str(i) + "/span").text
            if statename in self.driver.page_source:
                self.logger.info("****************** State Name are Selecting From Dropdown **********************")
                assert True
            else:
                self.logger.error("**************** State Name Options are not Selected ********************")
                count = count + 1
        return count

    @staticmethod
    def get_map_tooltip_info_validation(self, driver):
        blue_marks = 0
        white_marks = 0
        map_data = []
        lst = self.driver.find_elements(By.CLASS_NAME, "leaflet-interactive")
        print("No of Markers", len(lst) - 1)
        markers = int(len(lst) - 1) / 2
        if len(lst) - 1 == 0:
            self.logger.info("*************** MAP Does not have Markers")
            assert False
        else:
            for x in range(1, 3):
                if lst[x].get_attribute('fill') == '#FFFFFF':
                    white_marks = white_marks + 1
                else:
                    blue_marks = blue_marks + 1
                act = ActionChains(self.driver)
                act.move_to_element(lst[x]).perform()
                act.pause(4)
                txt = self.driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
                map_data.append(txt.text)
        return map_data
    @staticmethod
    def get_map_markers_tooltip_info_validation(self, driver):
        driver.implicitly_wait(30)
        lst = self.driver.find_elements(By.CLASS_NAME, "leaflet-interactive")
        print("No of Markers", len(lst) - 1)
        blue_marks = 0
        white_marks = 0
        time.sleep(2)
        map_data = []
        for x in range(1, len(lst)):
            if lst[x].get_attribute('fill') == '#FFFFFF':
                white_marks = white_marks + 1
            else:
                blue_marks = blue_marks + 1
            act = ActionChains(self.driver)
            act.move_to_element(lst[x]).perform()
            act.pause(4)
            # txt = self.driver.find_elements(By.CLASS_NAME, "//*[@class='leaflet-popup-content']/b") for i in range(
            # len(txt)): details = self.driver.find_elements(By.CLASS_NAME, "//*[@class='leaflet-popup-content']/b[
            # "+str(i)+"]") map_data.append(details)
        return len(lst)

    @staticmethod
    def test_validate_course_column_validate(self):
        course_tablevals = []
        count = 0
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        course_name = self.driver.find_elements(By.XPATH, self.pageobjects.course_values)
        for i in range(1, len(course_name)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[2]")
            course_tablevals.append(state_list.text)
        if len(course_tablevals) == len(course_name) - 1:
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
                count = count + 1
        return count

    @staticmethod
    def test_validate_medium_column_values(self):
        medium_tablevals = []
        count = 0
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        medium_val = self.driver.find_elements(By.XPATH, self.pageobjects.medium_values)
        for i in range(1, len(medium_val)):
            state_list = self.driver.find_element(By.XPATH, "//div/table/tbody/tr[" + str(i) + "]/td[3]")
            medium_tablevals.append(state_list.text)
        if len(medium_tablevals) == len(medium_val) - 1:
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
                count = count + 1
        return count

    # District Wise Status
    @staticmethod
    def test_check_district_program_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.click_district_program).click()
        time.sleep(1)
        count = 0
        options = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        if len(options) > 0:
            self.logger.info("************** Program Dropdown Showing Options *******************")
            assert True
        else:
            self.logger.error("****************** Program Dropdown is Empty... *************************")
            count = count + 1
        return count

    @staticmethod
    def test_check_states_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.click_state_options).click()
        time.sleep(1)
        count = 0
        options = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        if len(options) > 0:
            self.logger.info("************** State Dropdown Showing Options *******************")
            assert True
        else:
            self.logger.error("****************** State Dropdown is Empty... *************************")
            count = count + 1
        return count

    @staticmethod
    def selecting_the_state_dropdown_options(self):
        count = 0
        self.driver.find_element(By.XPATH, self.pageobjects.click_state_options).click()
        time.sleep(1)
        state_list = self.driver.find_elements(By.XPATH, self.pageobjects.dropdown_options)
        for i in range(len(state_list)):
            state_options = self.driver.find_element(By.ID, self.pageobjects.state_names_id + str(i))
            state_options.click()
            statename = self.driver.find_element(By.ID, self.pageobjects.state_names_id + str(i) + "/span").text
            if statename in self.driver.page_source:
                self.logger.info("****************** State Name are Selecting From Dropdown **********************")
                assert True
            else:
                self.logger.error("**************** State Name Options are not Selected ********************")
                count = count + 1
        return count

    @staticmethod
    def get_stacked_bar_tooltip_validation(self, driver):
        count = 0
        values = self.driver.find_elements(By.CSS_SELECTOR, 'tspan.highcharts-text-outline')
        lst = self.driver.find_elements(By.CSS_SELECTOR, "rect.highcharts-point")
        stateList = []
        for x in range(1, round(len(lst) / 2)):
            act = ActionChains(driver)
            act.move_to_element(lst[x]).perform()
            act.pause(5)
            time.sleep(2)
            state_names = self.driver.find_element(By.XPATH, "//*[@class='highcharts-label highcharts-tooltip "
                                                             "highcharts-color-undefined']/*/*[1]")
            stateList.append(state_names.text)
        for j in range(len(stateList)):
            st_name = stateList[j]
            if st_name != st_name.lower() and st_name != st_name.upper() and "_" not in st_name:
                print(st_name, "State Name Options are present and displayed on UI")
            else:
                print(st_name, type(st_name), 'is not in camel case')
                count = count + 1
        return count

    @staticmethod
    def check_the_state_list_options_from_the_dropdown(self, driver):
        count = 0
        data = ReadConfig()
        self.pageobjects = Program_Objects()
        self.driver.find_element(By.XPATH, self.pageobjects.choose_states).click()
        time.sleep(3)
        # state_options = self.driver.find_elements(By.CLASS_NAME, "ng-option-label ng-star-inserted")
        for i in range(1, 10):
            state_ids = self.driver.find_element(By.XPATH, "//div[starts-with(@id,'a')][" + str(i) + "]")
            state_name = self.driver.find_element(By.XPATH, "//div[starts-with(@id,'a')][" + str(i) + "]/span")
            print(state_name.text, ' is selected')
            state_ids.click()
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.pageobjects.choose_states).click()
            time.sleep(4)
        return count
