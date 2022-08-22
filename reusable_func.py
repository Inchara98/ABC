from selenium.webdriver.support.select import Select
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class re_call_func:
    pageobjects = Program_Objects()
    dirpath = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.program_logfile, level=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

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
