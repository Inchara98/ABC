import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class program_nishtha():
    pageobjects = Program_Objects()
    value = ""
    Tittle = ""
    dirpath = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)
    driver = dirpath.get_chrome_browser()

    def test_check_whether_total_state_card(self):
        total_state = self.driver.find_element(By.ID, self.pageobjects.total_state).text
        if total_state > 0 and total_state != None:
            assert True
            self.logger.info("*********** Total state value is showing ***************")
        else:
            self.logger.error("***************  Total state value is not matching ************")
            assert False

    def test_check_whether_total_enrollment_card(self):
        total_enrollment = self.driver.find_element(By.ID, self.pageobjects.total_enrollment).text
        if total_enrollment == self.value:
            assert True
            self.logger.info("*********** Total enrollment value is showing ***************")
        else:
            self.logger.error("***************  Total enrollment value is not matching ************")
            assert False

    def test_check_whether_total_completion_card(self):
        total_completion = self.driver.find_element(By.ID, self.pageobjects.total_completion).text
        if total_completion == self.value:
            assert True
            self.logger.info("*********** Total completion value is showing ***************")
        else:
            self.logger.error("***************  Total completion value is not matching ************")
            assert False

    def test_check_whether_total_certification_card(self):
        total_certification = self.driver.find_element(By.ID, self.pageobjects.total_certification).text
        if total_certification == self.value:
            assert True
            self.logger.info("*********** Total certification value is showing ***************")
        else:
            self.logger.error("***************  Total certification value is not matching ************")
            assert False

    def test_check_whether_total_Medium_card(self):
        total_medium = self.driver.find_element(By.ID, self.pageobjects.total_medium).text
        if total_medium == self.value:
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

    def test_check_whether_total_enrollment_Tittle(self):
        total_enrollment_Tittle = self.driver.find_element(By.ID, self.pageobjects.total_enrollment_Tittle).text
        if total_enrollment_Tittle == self.Tittle:
            assert True
            self.logger.info("*********** Total enrollment Tittle is showing ***************")
        else:
            self.logger.error("***************  Total enrollment Tittle is not matching ************")
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

    def test_check_programs_dropdown(self):
        dropdown = Select(self.driver.find_element(By.ID,self.pageobjects.Select_Program_Dropdown))
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
        dropdown = Select(self.driver.find_element(By.ID,self.pageobjects.Select_Program_Dropdown))
        default_option = dropdown.first_selected_option.text()
        dropdown.select_by_index(2)
        self.driver.find_element(By.ID,self.pageobjects.Clear_Button).click()
        if default_option in self.driver.page_source:
            assert True
            self.logger.info("*********** Program is Selected ***************")
        else:
            self.logger.error("***************  Program is not selected ************")
            assert False


