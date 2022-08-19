import logging
import time
from selenium import webdriver

from PageObjects.Dashboard_Page import Dashboard_Objects
from get_directory import DirectoryPath
from utilities import dummy, dashboard_logGen, login_logGen, Programs_logGen

login = "../Logs/Login.log"


class Test_Atria_Login_Page:
    logfile = Dashboard_Objects()
    baseURL = "https://cqube-release.tibilprojects.com/"
    valid_uname = "admin"
    valid_pwd = "Tibil@123"
    driver = webdriver.Chrome(executable_path='../Driver/chromedriver')
    logger = Modules_logGen.setup_logger('log_pl', logfile.login_logfile, level=logging.DEBUG)

    def test_navigation_to_the_application(self):
        self.driver.get(self.baseURL)
        self.logger.info("****** Launching the browser **************")
        self.logger.warn("***************cQube login page is warn displayed *********************")
        self.logger.error("***************cQube login page is warn displayed *********************")

        time.sleep(3)
        if 'cQube' in self.driver.page_source:
            print("Login page is displayed...")
            self.logger.info("***************cQube login page is not displayed *********************")
            self.logger.info("***************cQube login page is warn displayed *********************")
            self.driver.close()
        else:
            self.logger.error("***************cQube login page is not displayed *********************")
            assert False
        self.logger.info("************ navigation is completed **************")
