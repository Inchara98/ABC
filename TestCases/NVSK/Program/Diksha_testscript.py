import logging
import re
import time
from selenium.webdriver.common.by import By
from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_Diksha_Dashboard:
    data = ReadConfig()
    pageobjects = Program_Objects()
    driver = data.navigate_to_Diksha()
    logger = Programs_logGen.setup_logger('Program_Diksha', pageobjects.program_logfile, level=logging.DEBUG)

    # Program Vanity Cards
    def test_total_status_card(self):
        States_info = self.driver.find_element(By.XPATH, self.pageobjects.Totalstates_info).get_attribute('title')
        States = self.driver.find_element(By.XPATH, self.pageobjects.Totalstates_UT).text
        States_value = re.sub(self.pageobjects.L, "", States)
        State_text = self.driver.find_element(By.XPATH, self.pageobjects.Totalstates_text).text
        if States_info is not None and State_text is not None:
            self.logger.info("*********** State Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** State Card Values is Missing ************")
            assert False
        if float(States_value) > 0 and States_value is not None:
            self.logger.info("*********** State Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** State Card Values is Missing ************")
            assert False

    def test_total_ETB_card(self):
        ETB_info = self.driver.find_element(By.XPATH, self.pageobjects.Total_ETB_info).get_attribute('title')
        ETB = self.driver.find_element(By.XPATH, self.pageobjects.Total_ETB).text
        ETB_value = re.sub(self.pageobjects.L, "", ETB)
        ETB_text = self.driver.find_element(By.XPATH, self.pageobjects.Total_ETB_text).text
        if ETB_info is not None and ETB_text is not None:
            self.logger.info("*********** ETB Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** ETB Card Values is Missing ************")
            assert False
        if float(ETB_value) > 0 and ETB_value is not None:
            self.logger.info("*********** ETB Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** ETB Card Values is Missing ************")
            assert False

    def test_Total_QR_Code_code_card(self):
        QR_code_info = self.driver.find_element(By.XPATH, self.pageobjects.Total_QR_Code_info).get_attribute('title')
        QR_Code = self.driver.find_element(By.XPATH, self.pageobjects.Total_QR_Code).text
        QR_Code_value = re.sub(self.pageobjects.L, "", QR_Code)
        QR_Code_text = self.driver.find_element(By.XPATH, self.pageobjects.Total_QR_Code_text).text
        if QR_code_info is not None and QR_Code_text is not None:
            self.logger.info("*********** QR_Code Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** QR_Code Card Values is Missing ************")
            assert False
        if float(QR_Code_value) > 0 and QR_Code_value is not None:
            self.logger.info("*********** QR_Code Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** QR_Code Card Values is Missing ************")
            assert False

    def test_Learning_session_card(self):
        Learning_session_info = self.driver.find_element(By.XPATH, self.pageobjects.Total_Content_info).get_attribute(
            'title')
        Learning_session = self.driver.find_element(By.XPATH, self.pageobjects.Total_Content).text
        Learning_session_value = re.sub(self.pageobjects.L, "", Learning_session)
        Learning_session_text = self.driver.find_element(By.XPATH, self.pageobjects.Total_Content_text).text
        if Learning_session_info is not None and Learning_session_text is not None:
            self.logger.info("*********** Learning_session Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Learning_session Card Values is Missing ************")
            assert False
        if float(Learning_session_value) > 0 and Learning_session_value is not None:
            self.logger.info("*********** Learning_session Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Learning_session Card Values is Missing ************")
            assert False

    def test_Total_time_spent_card(self):
        Potential_user_info = self.driver.find_element(By.XPATH, self.pageobjects.Total_time_spent_info).get_attribute(
            'title')
        Potential_user = self.driver.find_element(By.XPATH, self.pageobjects.Total_time_spent).text
        Potential_user_value = re.sub(self.pageobjects.L, "", Potential_user)
        Potential_user_text = self.driver.find_element(By.XPATH, self.pageobjects.Total_time_spent_text).text
        if Potential_user_info is not None and Potential_user_text is not None:
            self.logger.info("*********** Potential_user Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Potential_user Card Values is Missing ************")
            assert False
        if float(Potential_user_value) > 0 and Potential_user_value is not None:
            self.logger.info("*********** Potential_user Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Potential_user Card Values is Missing ************")
            assert False

    def test_click_the_Diksha_button(self):
        self.driver.find_element(By.ID, self.pageobjects.dashboard).click()
        time.sleep(3)
        if 'dashboard' in self.driver.current_url:
            self.logger.info("************** Dashboard screen is displaying ***************")
        else:
            self.logger.error("*********** Dashboard page is not showing ************** ")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(3)
        if 'etb' in self.driver.current_url:
            self.logger.info("************** Diksha screen is displaying ***************")
        else:
            self.logger.error("*********** Diksha page is not showing ************** ")
            assert False

    # Implementation Status
    def test_click_on_the_implementation_tab_button(self):
        # self.driver.find_element(By.ID, self.pageobjects.Implementation_Status).click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_tab).get_attribute(
            'aria-selected')
        if "true" == result:
            self.logger.info("************* Implementation Status Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Implementation Status Tab is not clicked *********************")
            assert False

    def test_Implementation_Status_a_plus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Implementation_Status_a_minus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_tab).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Implementation_Status_a_default_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Implementation_Status_tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # ETB coverage status
    def test_click_on_the_ETB_Coverage_tab_button(self):
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).get_attribute(
            'aria-selected')
        if "true" == result:
            self.logger.info("************* Implementation Status Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Implementation Status Tab is not clicked *********************")
            assert False

    def test_check_table_state_headers_clickable(self):
        self.logger.info("**************Clicking table headers *****************")
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, self.pageobjects.State_column).get_attribute('aria-sort')

        self.driver.find_element(By.XPATH, self.pageobjects.State_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.pageobjects.State_column).get_attribute('aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("state Header is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(now, "******** Status Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_column).get_attribute(
            'aria-sort')
        if sec_click == 'ascending' or "descending":
            assert True
        else:
            self.logger.error(sec_click, "******** Status Header sorting is not working ***********")
            assert False

    def test_check_table_curriculum_textbook_headers_clickable(self):
        self.logger.info("**************Clicking table headers *****************")
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_column).get_attribute(
            'aria-sort')

        self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_column).get_attribute('aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("Curriculum textbook is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(now, "******** Curriculum textbook Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.Energised_Textbook_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.Energised_Textbook_column).get_attribute(
            'aria-sort')
        if sec_click == 'ascending' or "descending":
            assert True
        else:
            self.logger.error(sec_click, "******** Curriculum textbook Header sorting is not working ***********")
            assert False

    def test_check_table_energised_textbook_headers_clickable(self):
        self.logger.info("**************Clicking table headers *****************")
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, self.pageobjects.Energised_Textbook_column).get_attribute(
            'aria-sort')

        self.driver.find_element(By.XPATH, self.pageobjects.Energised_Textbook_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.pageobjects.Energised_Textbook_column).get_attribute('aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("Energised textbook is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(now, "******** Energised textbook Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.per_Energised_Textbook_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.per_Energised_Textbook_column).get_attribute(
            'aria-sort')
        if sec_click == 'ascending' or "descending":
            assert True
        else:
            self.logger.error(sec_click, "******** Energised textbook Header sorting is not working ***********")
            assert False

    def test_check_table_per_Energised_textbook_headers_clickable(self):
        self.logger.info("**************Clicking table headers *****************")
        self.driver.find_element(By.ID, self.pageobjects.Diksha).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, self.pageobjects.per_Energised_Textbook_column).get_attribute(
            'aria-sort')

        self.driver.find_element(By.XPATH, self.pageobjects.per_Energised_Textbook_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.pageobjects.per_Energised_Textbook_column).get_attribute(
            'aria-sort')
        if now == 'ascending' or "descending":
            self.logger.info("% energised textbook is clicked and table values are changed ")
            assert True
        else:
            self.logger.error(now, "******** % energised textbook Header sorting is not working ***********")
            assert False
        self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.pageobjects.Curiculum_Textbook_column).get_attribute(
            'aria-sort')
        if sec_click == 'ascending' or "descending":
            assert True
        else:
            self.logger.error(sec_click, "******** % energised textbook Header sorting is not working ***********")
            assert False

    def test_ETB_Coverage_a_plus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_ETB_Coverage_a_minus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_ETB_Coverage_a_default_button(self):
        self.driver.find_element(By.ID, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    # Content Coverage On QR
    def test_click_on_the_Content_Coverage_tab_button(self):
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.Content_Coverage_Tab).get_attribute(
            'aria-selected')
        if "true" == result:
            self.logger.info("************* Content Coverage Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Content Coverage Tab is not clicked *********************")
            assert False

    def test_Content_Coverage_a_plus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Content_Coverage_Tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Content_Coverage_a_minus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Content_Coverage_Tab).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Content_Coverage_a_default_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Content_Coverage_Tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False

    def test_Check_Case_in_state_column(self):
        self.driver.find_element(By.XPATH, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(5)
        count = 0
        rows_count = self.driver.find_elements(By.XPATH, "//td[1]")
        d = []
        for i in range(1, len(rows_count)):
            a = self.driver.find_element(By.XPATH,
                                         "//app-material-heat-chart-table/div/table/tbody/tr[" + str(i) + "]/td[1]")
            d.append(a.text)
        print(d)
        for j in range(1, len(d)):
            s = d[j]
            if s != s.lower() and s != s.upper() and "_" not in s:
                print(s, 'is camel case')
            else:
                print(s, 'is not in camel case')
                count = count + 1
        if count == 0:
            assert True
        else:
            assert False

    def test_check_value_curiculum_textbook_column(self):
        self.driver.find_element(By.XPATH, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(5)
        count = 0
        rows_count = self.driver.find_elements(By.XPATH, "//td[2]")
        d = []
        for i in range(1, len(rows_count)):
            a = self.driver.find_element(By.XPATH,
                                         "//app-material-heat-chart-table/div/table/tbody/tr[" + str(i) + "]/td[2]")
            d.append(a.text)
        print(d)
        for j in range(1, len(d)):
            s = d[j]
            if int(s) >= 0:
                print(s, 'Not less than 0')
            else:
                print(s, 'less than 0')
                count = count + 1
        if count == 0:
            assert True
        else:
            assert False

    def test_check_value_energised_textbook_column(self):
        self.driver.find_element(By.XPATH, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(5)
        count = 0
        rows_count = self.driver.find_elements(By.XPATH, "//td[3]")
        d = []
        for i in range(1, len(rows_count)):
            a = self.driver.find_element(By.XPATH,
                                         "//app-material-heat-chart-table/div/table/tbody/tr[" + str(i) + "]/td[3]")
            d.append(a.text)
        print(d)
        for j in range(1, len(d)):
            s = d[j]
            if int(s) >= 0:
                print(s, 'Not less than 0')
            else:
                print(s, 'less than 0')
                count = count + 1
        if count == 0:
            assert True
        else:
            assert False

    def test_check_value_per_energised_textbook_column(self):
        self.driver.find_element(By.XPATH, self.pageobjects.ETB_Coverage_Tab).click()
        time.sleep(5)
        count = 0
        rows_count = self.driver.find_elements(By.XPATH, "//td[4]")
        d = []
        for i in range(1, len(rows_count)):
            a = self.driver.find_element(By.XPATH,
                                         "//app-material-heat-chart-table/div/table/tbody/tr[" + str(i) + "]/td[4]")
            d.append(a.text)
        print(d)
        for j in range(1, len(d)):
            s = d[j]
            if int(s) >= 0:
                print(s, 'Not less than 0')
            else:
                print(s, 'less than 0')
                count = count + 1
        if count == 0:
            assert True
        else:
            assert False


    #Learning session on potential users
    def test_click_on_the_Learning_session_potential_tab_button(self):
        time.sleep(2)
        result = self.driver.find_element(By.ID, self.pageobjects.Learning_session_potential_tab).get_attribute(
            'aria-selected')
        if "true" == result:
            self.logger.info("************* Learning session Potential Tab is Clicked *************")
            assert True
        else:
            self.logger.error("**************** Learning session Potential is not clicked *********************")
            assert False

    def test_Learning_session_Potential_user_a_plus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Learning_session_potential_tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_plus_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A+ button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A+ button is not working as expected ****************")
            assert False

    def test_Learning_session_Potential_user_a_minus_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Learning_session_potential_tab).click()
        time.sleep(2)
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_Learning_session_Potential_user_a_default_button(self):
        self.driver.find_element(By.ID, self.pageobjects.Learning_session_potential_tab).click()
        time.sleep(2)
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False
