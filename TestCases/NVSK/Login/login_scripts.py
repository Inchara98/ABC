import logging

from selenium.webdriver.common.by import By

from PageObjects.Dashboard_Page import Dashboard_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class login():
    pageobjects = Dashboard_Objects()
    dirpath = ReadConfig()
    logger = Programs_logGen.setup_logger('log_pl', pageobjects.login_logfile, level=logging.DEBUG)
    driver = dirpath.get_chrome_browser()

    def test_check_whether_login_page_displayed(self):
        self.driver.get(self.dirpath.get_state_ApplicationURL())
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("*********** NVSK Login screen is displayed ************** ")

        else:
            self.logger.error("************* NVSK Login page is not displayed **************")
            assert False

    def test_check_whether_landing_page_displayed(self):
        self.driver.get(self.dirpath.get_state_ApplicationURL())
        self.driver.find_element(By.ID, self.pageobjects.username).send_keys(self.dirpath.get_state_Username())
        self.driver.find_element(By.ID, self.pageobjects.password).send_keys(self.dirpath.get_state_Password())
        a = self.driver.find_element_by_id(self.pageobjects.login_btn)
        if a.is_enabled():
            assert True
            self.logger.info(" landing page is displayed ")
        else:
            self.logger.error(" landing page is not displayed ")
            assert False

    def test_check_whether_landing_page_is_not_displayed_user_is_in_login_page(self):
        self.driver.get("https://cqube-nvskpack.tibilprojects.com/")
        self.driver.find_element_by_id("username1").send_keys()
        self.driver.find_element_by_id("password1").send_keys()
        self.driver.find_element_by_id("login").click()
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("landing page is not displayed")

        else:
            self.logger.error("user is in login page")
            assert False

    def test_invalid_user_name_invalid_password(self):
        self.driver.get("https://cqube-nvskpack.tibilprojects.com/")
        self.driver.find_element_by_id("username1").send_keys("cqube")
        self.driver.find_element_by_id("password1").send_keys("cqube123")
        self.driver.find_element_by_id("login").click()
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("landing page is not displayed")

        else:
            self.logger.error("user is in login page")
            assert False

    def test_invalid_user_name_valid_password(self):
        self.driver.get("https://cqube-ssp.tibilprojects.com/")
        self.driver.find_element_by_id("username1").send_keys("cqube")
        self.driver.find_element_by_id("password1").send_keys("H@ry@123#")
        self.driver.find_element_by_id("login").click()
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("landing page is not displayed")

        else:
            self.logger.error("user is in login page")
            assert False

    def test_valid_user_name_invalid_password(self):
        self.driver.get("https://cqube-nvskpack.tibilprojects.com/")
        self.driver.find_element_by_id("username1").send_keys("hr.vsk")
        self.driver.find_element_by_id("password1").send_keys("12345")
        self.driver.find_element_by_id("login").click()
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("landing page is not displayed")

        else:
            self.logger.error("user is in login page")
            assert False
