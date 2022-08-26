import logging
import re
import time
from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_Nishtha_Dashboard:
    data = ReadConfig()
    pageobjects = Program_Objects()
    driver = data.navigate_to_nishtha()
    logger = Programs_logGen.setup_logger('Program_Nishtha', pageobjects.program_logfile, level=logging.DEBUG)

    # Program Vanity Cards
    def test_check_whether_total_state_card(self):
        total_state = self.driver.find_element(By.XPATH, self.pageobjects.total_state).text
        if int(total_state) > 0 and total_state is not None:
            self.logger.info("*********** Total state value is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total state value is not matching ************")
            assert False

    def test_check_whether_total_enrolment_card(self):
        total_enrollment = self.driver.find_element(By.XPATH, self.pageobjects.total_enrollment).text
        enrollment = re.sub('\D', "", total_enrollment)
        if int(enrollment) > 0 and total_enrollment is not None:
            self.logger.info("*********** Total enrollment value is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total enrollment value is not matching ************")
            assert False

    def test_check_whether_total_completion_card(self):
        total_completion = self.driver.find_element(By.XPATH, self.pageobjects.total_completion).text
        completion = re.sub('\D', "", total_completion)
        if int(completion) > 0 and total_completion is not None:
            self.logger.info("*********** Total completion value is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total completion value is not matching ************")
            assert False

    def test_check_whether_total_certification_card(self):
        total_certification = self.driver.find_element(By.XPATH, self.pageobjects.total_certification).text
        certification = re.sub('\D', "", total_certification)
        if int(certification) > 0 and total_certification is not None:
            self.logger.info("*********** Total certification value is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total certification value is not matching ************")
            assert False

    def test_check_whether_total_Medium_card(self):
        total_medium = self.driver.find_element(By.XPATH, self.pageobjects.total_medium).text
        if int(total_medium) > 0 and total_medium is not None:
            self.logger.info("*********** Total medium value is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total medium value is not matching ************")
            assert False

    def test_check_whether_total_state_Tittle(self):
        total_state_Tittle = self.driver.find_element(By.XPATH, self.pageobjects.total_state_Tittle).text
        if total_state_Tittle in self.driver.page_source:
            self.logger.info("*********** Total state Tittle is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total state Tittle is not matching ************")
            assert False

    def test_check_whether_total_enrolment_Tittle(self):
        total_enrolment_Tittle = self.driver.find_element(By.XPATH, self.pageobjects.total_enrollment_Tittle).text
        if total_enrolment_Tittle in self.driver.page_source:
            self.logger.info("*********** Total enrolment Tittle is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total enrolment Tittle is not matching ************")
            assert False

    def test_check_whether_total_completion_Tittle(self):
        total_completion_Tittle = self.driver.find_element(By.XPATH, self.pageobjects.total_completion_Tittle).text
        if total_completion_Tittle in self.driver.page_source:
            assert True
            self.logger.info("*********** Total completion value is showing ***************")
        else:
            self.logger.error("***************  Total completion value is not matching ************")
            assert False

    def test_check_whether_total_certification_Tittle(self):
        total_certification_Tittle = self.driver.find_element(By.XPATH,
                                                              self.pageobjects.total_certification_Tittle).text
        if total_certification_Tittle in self.driver.page_source:
            self.logger.info("*********** Total certification Tittle is showing ***************")
            assert True
        else:
            self.logger.error("***************  Total certification Tittle is not matching ************")
            assert False

    def test_check_whether_total_Medium_Tittle(self):
        total_medium_Tittle = self.driver.find_element(By.XPATH, self.pageobjects.total_medium_Tittle).text
        if total_medium_Tittle in self.driver.page_source:
            assert True
            self.logger.info("*********** Total medium Tittle is showing ***************")
        else:
            self.logger.error("***************  Total medium Tittle is not matching ************")
            assert False

    def test_click_the_nishtha_button(self):
        self.driver.find_element(By.ID, self.pageobjects.nishtha).click()
        time.sleep(3)
        if 'nishtha' in self.driver.current_url:
            self.logger.info("************** Nishtha screen is displaying ***************")
        else:
            self.logger.error("*********** Nishtha page is not showing ************** ")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.dashboard).click()
        time.sleep(3)
        if 'dashboard' in self.driver.current_url:
            self.logger.info("************** Dashboard screen is displaying ***************")
        else:
            self.logger.error("*********** Dashboard page is not showing ************** ")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.nishtha).click()
        time.sleep(3)

    # Implementation Status Tab
    def test_click_on_the_implementation_tab_button(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* Implementation Status Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Implementation Status Tab is not clicked *********************")
            assert False

    def test_program_dropdown_options(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_nishtha_dropdown_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** Program Dropdown not having Options **********")
            assert False

    def test_select_second_option_of_program_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False

    def test_select_third_option_of_program_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False

    def test_select_First_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False

    def test_Implementation_Status_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Implementation_Status_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Implementation_Status_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    #   Courses and Medium status Tab
    def test_program_course_medium_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_nishtha_dropdown_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** Program Dropdown not having Options **********")
            assert False

    def test_course_medium_select_second_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False

    def test_course_medium_select_third_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False

    def test_course_medium_select_First_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False

    def test_selection_of_first_option_check_table_values(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False
        state_name = self.data.test_validate_state_column_names(self.driver)
        if state_name == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 State Names are not Proper **********")
            assert False
        course_value = self.data.test_validate_course_column_validate(self.driver)
        if course_value == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Course Values are not Proper **********")
            assert False
        medium_values = self.data.test_validate_medium_column_values(self.driver)
        if medium_values == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Medium Values are not Proper **********")
            assert False

    def test_selection_of_second_option_check_table_values(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False
        state_name = self.data.test_validate_state_column_names(self.driver)
        if state_name == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 State Names are not Proper **********")
            assert False
        course_value = self.data.test_validate_course_column_validate(self.driver)
        if course_value == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Course Values are not Proper **********")
            assert False
        medium_values = self.data.test_validate_medium_column_values(self.driver)
        if medium_values == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Medium Values are not Proper **********")
            assert False

    def test_selection_of_third_option_check_table_values(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False
        state_name = self.data.test_validate_state_column_names(self.driver)
        if state_name == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 State Names are not Proper **********")
            assert False
        course_value = self.data.test_validate_course_column_validate(self.driver)
        if course_value == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Course Values are not Proper **********")
            assert False
        medium_values = self.data.test_validate_medium_column_values(self.driver)
        if medium_values == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Medium Values are not Proper **********")
            assert False

    def test_click_on_course_and_medium_tab(self):
        self.driver.find_element(By.ID, self.pageobjects.nishtha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(3)
        result = self.driver.find_element(By.ID, self.pageobjects.CM_status).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* Courses and Medium status is clicked *************")
            assert True
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
        if len(state_tablevals) == len(state_name) - 1:
            self.logger.info("************ State Table values are showing ****************")
            assert True
        else:
            self.logger.error("************ State names are not showing **************")
            assert False

    def test_check_course_table_values(self):
        course_tablevals = []
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
                assert False

    def test_check_medium_table_values(self):
        medium_tablevals = []
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
                assert False

    def test_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
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
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            print("value :", a_minus)
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.CM_status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    #   % against Potential Base
    def test_click_on_the_potential_tab_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.Potential_Base).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* Potential Base Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Potential Base Tab is not clicked *********************")
            assert False

    def test_program_potential_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        result = self.data.test_check_nishtha_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** Potential Program Dropdown not having Options **********")
            assert False

    def test_potential_select_second_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False

    def test_potential_select_third_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False

    def test_potential_select_First_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False

    def test_Potential_Base_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Potential_Base_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Potential_Base_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Potential_Base).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    #   District Wise Status Tab
    def test_click_on_the_district_status_tab_button(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.District_Status).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* District Status Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** District Status Tab is not clicked *********************")
            assert False

    def test_program_district_status_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.test_check_district_program_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** District Wise Program Dropdown not having Options **********")
            assert False

    def test_state_district_status_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.test_check_states_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names Dropdown not having Options **********")
            assert False

    def test_district_wise_select_second_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False

    def test_district_wise_select_third_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False

    def test_district_wise_select_First_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False

    def test_overall_program_with_all_the_states(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_N1_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_1).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_N2_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_2).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_N3_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_3).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_District_Status_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_District_Status_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_District_Status_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.District_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # Course Wise Status
    def test_click_on_the_course_wise_tab_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.District_Status).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* District Status Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** District Status Tab is not clicked *********************")
            assert False

    def test_program_course_status_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.data.test_check_district_program_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** District Wise Program Dropdown not having Options **********")
            assert False

    def test_state_course_status_dropdown_options(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.data.test_check_states_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names Dropdown not having Options **********")
            assert False

    def test_course_district_wise_select_second_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_2_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 2.0 Option is not Selected **********")
            assert False

    def test_course_course_district_wise_select_third_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_3_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 3.0 Option is not Selected **********")
            assert False

    def test_course_district_wise_select_First_option_of_program_dropdown(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_nishtha_1_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** NISHTHA 1.0 Option is not Selected **********")
            assert False

    def test_course_N1_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_1).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_Course_N2_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_2).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_Course_N3_option_with_state_list(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pageobjects.Choose_Program).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.pageobjects.Nishtha_3).click()
        time.sleep(2)
        result = self.data.selecting_the_state_dropdown_options(self.driver)
        if result == 0:
            pass
        else:
            self.logger.error("*********** State Names are not selected from Dropdown **********")
            assert False

    def test_Course_Status_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Course_Status_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Course_Status_a_default_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Course_Status).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False
