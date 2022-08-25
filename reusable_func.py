import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class reusableFuncs:
    pageobjects = Program_Objects()
    dirpath = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)

    @staticmethod
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

    @staticmethod
    def test_click_on_A_default_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_default)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 16px;"' in self.driver.page_source:
            self.logger.info("************* A button is clicked *************")
            assert True
        else:
            self.logger.error("************** A button is not clicked *******************")
            count = count + 1
        return count

    @staticmethod
    def test_click_on_A_plus_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_plus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 18px;"' in self.driver.page_source:
            self.logger.info("************* A+ button is clicked *************")
            assert True
        else:
            self.logger.error("************** A+ button is not clicked *******************")
            count = count + 1
        return count

    @staticmethod
    def test_click_on_A_minus_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.pageobjects.a_minus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 16px;"' in self.driver.page_source:
            self.logger.info("************* A- button is clicked *************")
            assert True
        else:
            self.logger.error("************** A- button is not clicked *******************")
            count = count + 1
        return count

