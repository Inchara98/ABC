import logging
import re
import time

from selenium.webdriver.common.by import By

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_PM_Poshan:
    data = ReadConfig()
    pageobjects = Program_Objects()
    driver = data.navigate_to_pm_poshina()
    logger = Programs_logGen.setup_logger('Program_PM_Poshan', pageobjects.program_logfile, level=logging.DEBUG)

    def test_navigation_to_pm_poshan_dashboard(self):
        self.driver.find_element(By.ID, self.pageobjects.dashboard).click()
        time.sleep(2)
        if 'dashboard' in self.driver.current_url:
            self.logger.info("*************** Navigation to Dashboard Screen *****************")
            assert True
        else:
            self.logger.error("********************* Navigation to Dashboard failed from PM Poshin ***********")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.pm_poshan).click()
        time.sleep(3)
        if 'poshan' in self.driver.current_url or self.driver.page_source:
            self.logger.info("********* PM Poshan Dashboard is displayed in the UI ***************")
            assert True
        else:
            self.logger.error("******** PM Poshan Menu Button is not working  *************")
            assert False

    def test_validate_poshan_state_card_metrics(self):
        state_info = self.driver.find_element(By.XPATH, self.pageobjects.pm_states_info).get_attribute('title')
        state_value = self.driver.find_element(By.XPATH, self.pageobjects.pm_state_value).text
        pm_state_value = re.sub('\D', "", state_value)
        status_title = self.driver.find_element(By.XPATH, self.pageobjects.pm_state_title).text
        if state_info is not None and status_title is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if int(pm_state_value) > 0 and pm_state_value is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM Poshan Card Values is Missing ************")
            assert False

    def test_validate_poshan_Schools_card_metrics(self):
        school_info = self.driver.find_element(By.XPATH, self.pageobjects.pm_schools_info).get_attribute('title')
        school_value = self.driver.find_element(By.XPATH, self.pageobjects.pm_schools_value).text
        pm_school_value = re.sub(self.pageobjects.L, "", school_value)
        status_title = self.driver.find_element(By.XPATH, self.pageobjects.pm_state_title).text
        if school_info is not None and status_title is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if float(pm_school_value) > 0 and pm_school_value is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM Poshan Card Values is Missing ************")
            assert False

    # Implementation Status Tab
    def test_click_on_implementation_status_tab(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_implementation_tab).click()
        time.sleep(2)
        result = self.driver.find_element(By.XPATH, "//*[@role='tab'][1]").get_attribute(
            'aria-selected')
        if "true" == result:
            self.logger.info("************* Implementation Tab is Clicked **************")
            assert True
        else:
            self.logger.error("************** Implementation Tab is not clicked ****************")
            assert False

    def test_check_map_tooltip_information(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_implementation_tab).click()
        time.sleep(2)
        result = self.data.get_map_tooltip_info_validation(self, driver=self.driver)
        if 'Onboarded on PM Poshan' in result[0]:
            self.logger.info("*************** Implementation status map report having tooltip information "
                             "********************")
            assert True
        else:
            self.logger.error("*********** MAP Report Not having tooltip **************")
            assert False

    # Progress Status Tab
    def test_click_on_progress_status_tab(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        result = self.driver.find_element(By.XPATH, "//*[@role='tab'][2]").get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* Progress Status Tab is Clicked **************")
            assert True
        else:
            self.logger.error("************** Progress Tab is not clicked ****************")
            assert False

    def test_click_on_state_check_with_metrics_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_state_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count = len(options)
        for i in range(count):
            state_ids = self.driver.find_element(By.XPATH,
                                                 "//div[starts-with(@id,'a') and contains(@id,"'-' + str(i) + ")]")
            state_ids.click()
            time.sleep(4)
            result = self.data.get_map_tooltip_info_validation(self, driver=self.driver)
            print(result)
            if "Total Enrolled" and "Total Schools" in result[0]:
                self.logger.info("************ State Name ,Total Enrolled , Total Schools **************** ")
                assert True
            else:
                self.logger.error("************ Tooltip information are missing in map **************")
                assert False
            self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
            time.sleep(2)

    def test_click_on_districts_check_with_metrics_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_District_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count = len(options)
        for i in range(count):
            state_ids = self.driver.find_element(By.XPATH,
                                                 "//div[starts-with(@id,'a') and contains(@id,"'-' + str(i) + ")]")
            state_ids.click()
            time.sleep(4)
            result = self.data.get_map_tooltip_info_validation(self, driver=self.driver)
            print(result)
            # if "Total Enrolled" and "Total Schools" and "District Name" and "State/UT name" in result[0]:
            #     self.logger.info("************ State Name ,Total Enrolled , Total Schools **************** ")
            #     assert True
            # else:
            #     self.logger.error("************ Tooltip information are missing in map **************")
            #     assert False
            self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
            time.sleep(2)

    def test_district_selection_of_each_state_options(self):
        state_list = []
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_District_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "filter-State/UT").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count = len(options)
        for i in range(count):
            state_ids = self.driver.find_element(By.XPATH,
                                                 "//div[starts-with(@id,'a') and contains(@id,"'-' + str(i) + ")]")
            state_name = self.driver.find_element(By.XPATH,
                                                  "//div[starts-with(@id,'a') and contains(@id,"'-' + str(
                                                      i) + ")]/span")
            state_list.append(state_name.text)
            state_ids.click()
            time.sleep(2)
            res = self.data.get_map_tooltip_info_validation(self, driver=self.driver)
            print(res)
            self.driver.find_element(By.ID, "filter-State/UT").click()
            time.sleep(2)

    def test_district_selection_of_each_metrics_state_options(self):
        state_list = []
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_District_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count = len(options)
        for i in range(count):
            state_ids = self.driver.find_element(By.XPATH,
                                                 "//div[starts-with(@id,'a') and contains(@id,"'-' + str(i) + ")]")
            state_ids.click()
            time.sleep(4)
            self.driver.find_element(By.ID, "filter-State/UT").click()
            time.sleep(2)
            options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
            count = len(options)
            for j in range(count):
                state_ids = self.driver.find_element(By.XPATH,
                                                     "//div[starts-with(@id,'a') and contains(@id,"'-' + str(j) + ")]")
                state_name = self.driver.find_element(By.XPATH,
                                                      "//div[starts-with(@id,'a') and contains(@id,"'-' + str(
                                                          j) + ")]/span")
                state_list.append(state_name.text)
                state_ids.click()
                time.sleep(2)
                res = self.data.get_map_tooltip_info_validation(self, driver=self.driver)
                print(res)
                self.driver.find_element(By.ID, "filter-State/UT").click()
                time.sleep(2)
            self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
            time.sleep(3)
        for k in range(len(state_list)):
            s = state_list[k]
            if s != s.lower() and s != s.upper() and s != s.isalnum():
                self.logger.info("********* State List Options are showing in dropdown ")
                assert True
            else:
                self.logger.error("************* State List Options are not proper ************")
                assert False

    def test_check_metrics_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_state_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count = len(options)
        if count != 0:
            self.logger.info("************* State Wise Metrics Dropdown having Options *************")
            assert True
        else:
            self.logger.error("************ Metrics Dropdown not having Options ****************")
            assert False

    def test_check_district_metrics_dropdown_options(self):
        self.driver.find_element(By.XPATH, self.pageobjects.pm_progress_status_tab).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.pm_District_btn).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "metricFilter-Metrics to be shown").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count1 = len(options)
        if count1 != 0:
            self.logger.info("************* State Wise Metrics Dropdown having Options *************")
            assert True
        else:
            self.logger.error("************ Metrics Dropdown not having Options ****************")
            assert False
        self.driver.find_element(By.ID, "filter-State/UT").click()
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, self.pageobjects.metric_options)
        count2 = len(options)
        if count2 != 0:
            self.logger.info("************* District Wise Metrics Dropdown having Options *************")
            assert True
        else:
            self.logger.error("************ State Names Dropdown not having Options ****************")
            assert False
