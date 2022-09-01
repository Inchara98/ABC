import logging
import re
import time

import self as self
from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_Micro_improvements_Dashboard:
    data = ReadConfig()
    pageobjects = Program_Objects()
    driver = data.navigate_to_Micro_improvements()
    logger = Programs_logGen.setup_logger('Program_Micro_improvements', pageobjects.program_logfile, level=logging.DEBUG)

    # Program Vanity Cards
    def test_total_Micro_improvements_ongoing(self):
        Micro_improvements_info = self.driver.find_element(By.XPATH, self.pageobjects.total_Micro_improvements_ongoing_info).get_attribute('title')
        Micro_improvements= self.driver.find_element(By.XPATH, self.pageobjects.total_Micro_improvements_ongoing_value).text
        Micro_improvements_value = re.sub(self.pageobjects.L, "", Micro_improvements)
        Micro_improvements_text = self.driver.find_element(By.XPATH, self.pageobjects.total_Micro_improvements_ongoing_text).text
        if Micro_improvements_info is not None and Micro_improvements_text is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False
        if float(Micro_improvements_value) > 0 and Micro_improvements_value is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False


    def test_total_Micro_improvements_started(self):
        total_micro_improvements_started_info = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_started_info).get_attribute('title')
        total_micro_improvements_started_number = self.driver.find_element(By.XPATH,self.pageobjects. total_micro_improvements_started_number).text
        Micro_improvements_value = re.sub(self.pageobjects.L, "", total_micro_improvements_started_number)
        Micro_improvements_text = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_started_text).text
        if total_micro_improvements_started_info is not None and Micro_improvements_text is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False
        if float(Micro_improvements_value) > 0 and Micro_improvements_value is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False




    def test_total_Micro_improvements_progress(self):
        total_micro_improvements_in_progress_info = self.driver.find_element(By.XPATH,self.pageobjects. total_micro_improvements_in_progress_info).get_attribute('title')
        total_micro_improvements_in_progress_value = self.driver.find_element(By.XPATH,self.pageobjects. total_micro_improvements_in_progress_value).text
        Micro_improvements_value = re.sub(self.pageobjects.L, "", total_micro_improvements_in_progress_value)
        total_micro_improvements_in_progress_text = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_in_progress_text).text
        if  total_micro_improvements_in_progress_info is not None and total_micro_improvements_in_progress_text is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False
        if float(Micro_improvements_value) > 0 and Micro_improvements_value is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False

    def total_micro_improvements_in_submitted_info(self):
        total_micro_improvements_in_submitted_info = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_in_submitted_info).get_attribute('title')
        total_micro_improvements_in_submitted_value = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_in_submitted_value).text
        Micro_improvements_value = re.sub(self.pageobjects.L, "", total_micro_improvements_in_submitted_value)
        total_micro_improvements_in_submitted_text = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_started_text).text
        if total_micro_improvements_in_submitted_info is not None and total_micro_improvements_in_submitted_text is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False
        if float(Micro_improvements_value) > 0 and Micro_improvements_value is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False

    def total_micro_improvements_in_submitted_with_evidence(self):
        total_micro_improvements_in_submitted_with_evidence_info = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_started_info).get_attribute('title')
        total_micro_improvements_in_submitted_with_evidence_value = self.driver.find_element(By.XPATH,self.pageobjects.total_micro_improvements_in_submitted_with_evidence_value).text
        Micro_improvements_value = re.sub(self.pageobjects.L, "", total_micro_improvements_in_submitted_with_evidence_value)
        total_micro_improvements_in_submitted_with_evidence_text = self.driver.find_element(By.XPATH, self.pageobjects.total_micro_improvements_in_submitted_with_evidence_text).text
        if total_micro_improvements_in_submitted_with_evidence_info is not None and total_micro_improvements_in_submitted_with_evidence_text is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False
        if float(Micro_improvements_value) > 0 and Micro_improvements_value is not None:
            self.logger.info("*********** Micro_improvements Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro_improvements Card Values is Missing ************")
            assert False

    # Implementation Status Tab
    def test_click_on_the_implementation_tab_button(self):
        result = self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_micro_improvements).get_attribute('aria-selected')
        if "true" == result:
            self.logger.info("************* Implementation_Status_micro_improvements Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Implementation_Status_micro_improvements Tab is not clicked *********************")
            assert False

    def test_Implementation_Status_micro_improvements_a_plus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_micro_improvements).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Implementation_Status_micro_improvements_a_minus_button_on_cm_status(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_micro_improvements).click()
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
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_micro_improvements).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # Improvements Status
    def test_click_on_the_improvements_status_tab_button(self):
        result = self.driver.find_element(By.XPATH, self.pageobjects.improvements_status_micro_improvements).click()
        if "true" == result:
            self.logger.info("************* improvements_status_micro_improvements Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** improvements_status_micro_improvements Tab is not clicked *********************")
            assert False

    def test_program_dropdown_options(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_micro_improvements_dropdown_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** Program Dropdown not having Options **********")
            assert False


    def test_select_first_option_of_metric_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_Total_micro_improvements_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** total micro_improvements Option is not Selected **********")
            assert False

    def test_select_second_option_of_metric_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_micro_improvements_started_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** total micro_improvements started Option is not Selected **********")
            assert False


    def test_select_third_option_of_metric_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_micro_improvements_in_progress_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** total micro_improvements progress Option is not Selected **********")
            assert False

    def test_select_fourth_option_of_metric_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_micro_improvements_submitted_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** total micro_improvements submitted Option is not Selected **********")
            assert False


    def test_select_fifth_option_of_metric_dropdown(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.data.test_check_selection_micro_improvements_submitted_with_evidence_options(self.driver)
        print(result)
        if result == 0:
            pass
        else:
            self.logger.error("*********** total micro_improvements submitted with evidence Option is not Selected **********")
            assert False

