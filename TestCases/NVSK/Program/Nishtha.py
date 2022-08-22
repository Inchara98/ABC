import logging

from selenium.webdriver.common.by import By

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class program_nishtha():
    pagobjects = Program_Objects()
    value = ""
    dirpath = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pagobjects.program_logfile, level=logging.DEBUG)
    driver = dirpath.get_chrome_browser()

    def test_check_whether_total_state_card(self):
        total_state = self.driver.find_element(By.ID, self.pagobjects.total_state).text
        if total_state == self.value:
            assert True
            self.logger.info("*********** Total state value is showing ***************")
        else:
            self.logger.error("***************  Total state value is not matching ************")
            assert False

