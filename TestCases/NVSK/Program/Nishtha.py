import logging
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Programs_Page import Program_Objects
from reusable_func import re_call_func
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class program_nishtha:
    pageobjects = Program_Objects()
    Tittle = ""
    data = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)
    driver = data.get_chrome_browser()
    resue = re_call_func(driver)
    driver.implicitly_wait(50)
    driver.maximize_window()
    driver.get(data.getApplicationURL())
    time.sleep(5)
    driver.find_element(By.ID, pageobjects.nishtha).click()
    time.sleep(3)

    def test_click_the_nishtha_button(self):
        self.driver.find_element(By.ID, self.pageobjects.dashboard).click()
        self.driver.find_element(By.ID, self.pageobjects.nishtha).click()
        time.sleep(3)
        if 'nishtha' in self.driver.current_url:
            self.logger.info("********** Nishtha Button is worknig  ************")
            assert True
        else:
            self.logger.error("************* Nishtha Button is not working ****************")
            assert False

    # Program Vanity Cards
    def test_check_whether_total_state_card(self):
        total_state = self.driver.find_element(By.ID, self.pageobjects.total_state).text
        print(total_state)
        if total_state > 0 and total_state is not None:
            assert True
            self.logger.info("*********** Total state value is showing ***************")
        else:
            self.logger.error("***************  Total state value is not matching ************")
            assert False

    def test_check_whether_total_enrolment_card(self):
        total_enrollment = self.driver.find_element(By.ID, self.pageobjects.total_enrollment).text
        if total_enrollment > 0 and total_enrollment is not None:
            assert True
            self.logger.info("*********** Total enrollment value is showing ***************")
        else:
            self.logger.error("***************  Total enrollment value is not matching ************")
            assert False

    def test_check_whether_total_completion_card(self):
        total_completion = self.driver.find_element(By.ID, self.pageobjects.total_completion).text
        if total_completion > 0 and total_completion is not None:
            assert True
            self.logger.info("*********** Total completion value is showing ***************")
        else:
            self.logger.error("***************  Total completion value is not matching ************")
            assert False

    def test_check_whether_total_certification_card(self):
        total_certification = self.driver.find_element(By.ID, self.pageobjects.total_certification).text
        if total_certification > 0 and total_certification is not None:
            assert True
            self.logger.info("*********** Total certification value is showing ***************")
        else:
            self.logger.error("***************  Total certification value is not matching ************")
            assert False

    def test_check_whether_total_Medium_card(self):
        total_medium = self.driver.find_element(By.ID, self.pageobjects.total_medium).text
        if total_medium > 0 and total_medium is not None:
            assert True
            self.logger.info("*********** Total medium value is showing ***************")
        else:
            self.logger.error("***************  Total medium value is not matching ************")
            assert False

    def test_check_whether_total_state_Tittle(self):
        total_state_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_state_Tittle).text
        if total_state_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total state Tittle is showing ***************")
        else:
            self.logger.error("***************  Total state Tittle is not matching ************")
            assert False

    def test_check_whether_total_enrolment_Tittle(self):
        total_enrolment_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_enrollment_Tittle).text
        if total_enrolment_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total enrolment Tittle is showing ***************")
        else:
            self.logger.error("***************  Total enrolment Tittle is not matching ************")
            assert False

    def test_check_whether_total_completion_Tittle(self):
        total_completion_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_completion_Tittle).text
        if total_completion_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total completion value is showing ***************")
        else:
            self.logger.error("***************  Total completion value is not matching ************")
            assert False

    def test_check_whether_total_certification_Tittle(self):
        total_certification_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_certification_Tittle).text
        if total_certification_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total certification Tittle is showing ***************")
        else:
            self.logger.error("***************  Total certification Tittle is not matching ************")
            assert False

    def test_check_whether_total_Medium_Tittle(self):
        total_medium_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_medium_Tittle).text
        if total_medium_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total medium Tittle is showing ***************")
        else:
            self.logger.error("***************  Total medium Tittle is not matching ************")
            assert False

    # Implementation stages related scripts
    def test_check_programs_dropdown(self):
        dropdown = Select(self.driver.find_element(By.ID, self.pageobjects.Select_Program_Dropdown))
        j = 1
        for i in range(1, len(dropdown.options)):
            dropdown.select_by_index(i)
            print(dropdown.options[i].text, 'Program is selected ')
            if dropdown.options[i].text in self.driver.page_source():
                assert True
                self.logger.info("*********** Program is Selecting ***************")
            else:
                self.logger.error("***************  Program is not selecting ************")
                assert False

    def test_check_clear_dropdown_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        program_options = Select(self.driver.find_element(By.XPATH, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        if count != 0:
            self.logger.info("********** Program dropdown having options **************")
            assert True
        else:
            self.logger.error("************* Program dropdown not having options ***************")
            assert False

    def test_Implementation_status_select_each_options_from_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        program_options = Select(self.driver.find_element(By.ID, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        for i in range(count):
            program_options.select_by_index(i)
            program_name = program_options.options[i].text
            self.logger(program_options.options[i].text, " is selected ...")
            if program_name == program_options.first_selected_option.text:
                assert True
                self.logger.info("********* Program is selected *************")
            else:
                self.logger.error(program_name, program_options.first_selected_option.text,
                                  "******** is not selected ... *********")
                assert False

    def test_check_FullScreen_button(self):
        a = self.driver.get_window_size()
        fullscreen = self.driver.find_element(By.ID, self.pageobjects.FullScreen)
        fullscreen.click()
        b = self.driver.get_window_size()
        if a != b:
            assert True
            self.logger.info("*********** Program is Selected ***************")
        else:
            self.logger.error("***************  Program is not selected ************")
            assert False

    def test_zoomin_button(self):
        zoomin = self.driver.find_element((By.ID, self.pageobjects.Zoomin))
        zoomin.click()

    def test_zoomout_button(self):
        zoomout = self.driver.find_element(By.ID, self.pageobjects.Zoomout)
        zoomout.click()

    def test_fontsize_increase_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A+ button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_fontsize_decrease_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A- button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Default_Font_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        a_plus = self.resue.test_click_on_A_default_button()
        if a_plus != 0:
            self.logger.info("********** A button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # Course and Medium status
    def test_click_on_course_and_medium_tab(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        result = self.driver.find_element(By.ID, self.pageobjects.CM_status).get_attribute('aria-selected')
        if str(True) == result:
            assert True
            self.logger.info("***************** Clicked the Courses & Medium Tab **********************")
        else:
            self.logger.error("***************** Courses & Medium Tab is not clicked **********************")
            assert False

    def test_check_whether_dropdown_option(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        program_options = Select(self.driver.find_element(By.ID, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        if count != 0:
            self.logger.info("********** Program dropdown having options **************")
            assert True
        else:
            self.logger.error("************* Program dropdown not having options ***************")
            assert False

    def test_select_each_options_from_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        program_options = Select(self.driver.find_element(By.ID, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        for i in range(count):
            program_options.select_by_index(i)
            program_name = program_options.options[i].text
            self.logger(program_options.options[i].text, " is selected ...")
            if program_name == program_options.first_selected_option.text:
                assert True
                self.logger.info("********* Program is selected *************")
            else:
                self.logger.error(program_name, program_options.first_selected_option.text,
                                  "******** is not selected ... *********")
                assert False

    def test_check_table_state_headers_clickable(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        status = self.driver.find_element(By.XPATH, self.pageobjects.state_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.pageobjects.state_header).click()
        now = self.driver.find_element(By.XPATH, self.pageobjects.state_sort).get_attribute('aria-sort')
        if status != now:
            assert True
            self.logger.info("*********** State table header is Sorting working *****************")
        else:
            self.logger.error(status, now, "********Status Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if now != sec_click:
            assert True
            self.logger.info("*********** Status table header is Sorting working *****************")
        else:
            self.logger.error(status, now, "********Status Header sorting is not working ***********")
            assert False

    def test_check_table_courses_headers_clickable(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        status = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        now = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if status != now:
            assert True
            self.logger.info("*********** Courses Launched table header is Sorting working *****************")
        else:
            self.logger.error(status, now, "********Course launched Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if now != sec_click:
            assert True
            self.logger.info("*********** Courses Launched table header is Sorting working *****************")
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
            self.logger.error(status, now, "********Course launched Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.course_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.course_sort).get_attribute('aria-sort')
        if now != sec_click:
            assert True
            self.logger.info("*********** Medium table header is Sorting working *****************")
        else:
            self.logger.error(status, now, "******** Medium Header sorting is not working ***********")
            assert False

    def test_check_state_table_values(self):
        state_tablevals = []
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        state_name = self.driver.find_elements(By.XPATH, self.pageobjects.state_values)
        for i in range(len(state_name)):
            state_tablevals.append(state_name)
        if len(state_tablevals) == len(state_name):
            assert True
            self.logger.info("************ State Table values are showing ****************")
        else:
            self.logger.error(len(state_tablevals), len(state_name),
                              "************ State names are not showing**************")
            assert False
        # validate camel cases
        for i in range(len(state_tablevals)):
            if state_tablevals[i] != state_tablevals[i].lower() and state_tablevals[i] != state_tablevals[
                i].upper() and "_" not in state_tablevals[i]:
                self.logger.info("*********** State Names are in Camel Cases *************")
                assert True
            else:
                self.logger.error("*********** State Names are Not in Camel Cases *************")
                assert False

    def test_check_course_table_values(self):
        course_tablevals = []
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        course_name = self.driver.find_elements(By.XPATH, self.pageobjects.course_values)
        for i in range(len(course_name)):
            course_tablevals.append(course_name)
        if len(course_tablevals) == len(course_name):
            assert True
            self.logger.info("************ Course Table Values are showing ****************")
        else:
            self.logger.error(len(course_tablevals), len(course_name),
                              "************ Course Values are not showing **************")
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
        for i in range(len(medium_val)):
            medium_tablevals.append(medium_val)
        if len(medium_tablevals) == len(medium_val):
            assert True
            self.logger.info("************ Course Table Values are showing ****************")
        else:
            self.logger.error(len(medium_tablevals), len(medium_val),
                              "************ Course Values are not showing **************")
            assert False
        for i in range(len(medium_tablevals)):
            if medium_tablevals[i] is not str:
                self.logger.info("*********** Course Values are Integers  *************")
                assert True
            else:
                self.logger.error("*********** Course Values are Not Integers *************")
                assert False

    def test_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A+ button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A- button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        a_plus = self.resue.test_click_on_A_default_button()
        if a_plus != 0:
            self.logger.info("********** A button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # % against potential base
    def test_click_on_per_against_Potential_base(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        result = self.driver.find_element(By.ID, self.pageobjects.CM_status).get_attribute('aria-selected')
        if str(True) == result:
            assert True
            self.logger.info("***************** Clicked the % against potential base Tab **********************")
        else:
            self.logger.error("***************** % against potential base Tab is not clicked **********************")
            assert False

    def test_PAP_Base_dropdown_option(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        program_options = Select(self.driver.find_element(By.ID, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        if count != 0:
            self.logger.info("********** Program dropdown having options **************")
            assert True
        else:
            self.logger.error("************* Program dropdown not having options ***************")
            assert False

    def test_PAP_base_select_each_options_from_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        program_options = Select(self.driver.find_element(By.ID, self.pageobjects.Program_dropdown))
        count = len(program_options.options)
        for i in range(count):
            program_options.select_by_index(i)
            program_name = program_options.options[i].text
            self.logger(program_options.options[i].text, " is selected ...")
            if program_name == program_options.first_selected_option.text:
                assert True
                self.logger.info("********* Program is selected *************")
            else:
                self.logger.error(program_name, program_options.first_selected_option.text,
                                  "******** is not selected ... *********")
                assert False

    def test_a_plus_button_on_PAP_Base(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A+ button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_a_minus_button_on_PAP_Base(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        a_plus = self.resue.test_click_on_A_plus_button()
        if a_plus != 0:
            self.logger.info("********** A- button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_a_default_button_on_PAP_Base(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        a_plus = self.resue.test_click_on_A_default_button()
        if a_plus != 0:
            self.logger.info("********** A button is working as expected ******************")
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    def test_clear_dropdown_button_PAP(self):
        self.driver.find_element(By.ID, self.pageobjects.PAP_Base).click()
        dropdown = Select(self.driver.find_element(By.XPATH, self.pageobjects.Select_Program_Dropdown))
        default_option = dropdown.first_selected_option.text()
        dropdown.select_by_index(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Clear_Button).click()
        if default_option in self.driver.page_source:
            assert True
            self.logger.info("*********** Program is Selected ***************")
        else:
            self.logger.error("***************  Program is not selected ************")
            assert False