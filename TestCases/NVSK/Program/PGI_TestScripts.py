import logging
import re
import time

from selenium.webdriver.common.by import By

from PageObjects.Programs_Page import Program_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_PGI_Dashboard:
    data = ReadConfig()
    pageobjects = Program_Objects()
    driver = data.navigate_to_PGI_dashboard()
    logger = Programs_logGen.setup_logger('Program_PGI', pageobjects.program_logfile, level=logging.DEBUG)

    def test_click_on_the_pgi_button_from_menu(self):
        self.driver.find_element(By.ID, self.pageobjects.dashboard).click()
        time.sleep(2)
        if 'dashboard' in self.driver.current_url:
            self.logger.info("************* Dashboard Screen is Displayed ************ ")
            assert True
        else:
            self.logger.error("************* Dashboard button is not working ****************")
        self.driver.find_element(By.ID, self.pageobjects.pgi_button).click()
        time.sleep(2)
        if 'pgi' in self.driver.current_url:
            self.logger.info("**************** PGI Dashboard Is Displayed ****************")
            assert True
        else:
            self.logger.error("****************** PGI Dashboard button is Not working ***************")
            assert False

    # PGI Vanity Metrics Cards

    def test_check_learning_outcome_card_details(self):
        info_text = self.driver.find_element(By.XPATH, self.pageobjects.learning_info).get_attribute('title')
        learning_value = self.driver.find_element(By.XPATH, self.pageobjects.learning_value).text
        value = re.sub('\D', '', learning_value)
        learning_text = self.driver.find_element(By.XPATH, self.pageobjects.learning_text).text
        if info_text is not None and info_text != info_text.upper() and info_text != info_text.lower():
            self.logger.info("******************* Learning Outcome Card showing INFO ********************")
            assert True
        else:
            self.logger.error("*************** Learning outcome card is not showing Info **********************")
            assert False
        if value is not None and int(value) > 0:
            self.logger.info("************* Learning Outcome Value is showing in Card *************")
            assert True
        else:
            self.logger.error("***************** Learning outcome Value is not showing in Card **********")
            assert False
        if learning_text is not None and learning_text != learning_text.upper() and learning_text != learning_text.lower():
            self.logger.info("******************* Learning Outcome Card showing Learning Text ********************")
            assert True
        else:
            self.logger.error("*************** Learning outcome card is not showing Description *****************")
            assert False

    def test_check_access_card_details(self):
        info_text = self.driver.find_element(By.XPATH, self.pageobjects.access_info).get_attribute('title')
        access_value = self.driver.find_element(By.XPATH, self.pageobjects.access_value).text
        value = re.sub('\D', '', access_value)
        access_text = self.driver.find_element(By.XPATH, self.pageobjects.access_text).text
        if info_text is not None and info_text != info_text.upper() and info_text != info_text.lower():
            self.logger.info("******************* Access Card showing INFO ********************")
            assert True
        else:
            self.logger.error("*************** Access card is not showing Info ******************")
            assert False
        if value is not None and int(value) > 0:
            self.logger.info("************* Access Value is showing in Card *************")
            assert True
        else:
            self.logger.error("***************** Access Value is not showing in Card **********")
            assert False
        if access_text is not None and access_text != access_text.upper() and access_text != access_text.lower():
            self.logger.info("******************* Access Card showing Access Description ********************")
            assert True
        else:
            print(access_text)
            self.logger.error("*************** Access card is not showing Description *****************")
            assert False

    def test_check_infrastructure_card_details(self):
        info_text = self.driver.find_element(By.XPATH, self.pageobjects.infrastructure_info).get_attribute('title')
        access_value = self.driver.find_element(By.XPATH, self.pageobjects.infrastructure_value).text
        value = re.sub('\D', '', access_value)
        access_text = self.driver.find_element(By.XPATH, self.pageobjects.infrastructure_text).text
        if info_text is not None and info_text != info_text.upper() and info_text != info_text.lower():
            self.logger.info("******************* Infrastructure Card showing INFO ********************")
            assert True
        else:
            self.logger.error("*************** Infrastructure card is not showing Info ***************")
            assert False
        if value is not None and int(value) > 0:
            self.logger.info("************* Infrastructure Value is showing in Card *************")
            assert True
        else:
            self.logger.error("***************** Infrastructure Value is not showing in Card **********")
            assert False
        if access_text is not None and access_text != access_text.upper() and access_text != access_text.lower():
            self.logger.info("******************* Infrastructure Card showing Access Description ********************")
            assert True
        else:
            self.logger.error("*************** Infrastructure card is not showing Description ****************")
            assert False

    def test_check_equity_card_details(self):
        info_text = self.driver.find_element(By.XPATH, self.pageobjects.equity_info).get_attribute('title')
        access_value = self.driver.find_element(By.XPATH, self.pageobjects.equity_value).text
        value = re.sub('\D', '', access_value)
        access_text = self.driver.find_element(By.XPATH, self.pageobjects.equity_text).text
        if info_text is not None and info_text != info_text.upper() and info_text != info_text.lower():
            self.logger.info("******************* Equity Card showing INFO ********************")
            assert True
        else:
            self.logger.error("*************** Equity card is not showing Info **************")
            assert False
        if value is not None and int(value) > 0:
            self.logger.info("************* Equity Value is showing in Card *************")
            assert True
        else:
            self.logger.error("***************** Equity Value is not showing in Card **********")
            assert False
        if access_text is not None and access_text != access_text.upper() and access_text != access_text.lower():
            self.logger.info("******************* Equity Card showing Access Description ********************")
            assert True
        else:
            self.logger.error("*************** Equity card is not showing Description **************")
            assert False

    def test_check_Governance_card_details(self):
        info_text = self.driver.find_element(By.XPATH, self.pageobjects.governance_info).get_attribute('title')
        access_value = self.driver.find_element(By.XPATH, self.pageobjects.governance_value).text
        value = re.sub('\D', '', access_value)
        access_text = self.driver.find_element(By.XPATH, self.pageobjects.governance_text).text
        if info_text is not None and info_text != info_text.upper() and info_text != info_text.lower():
            self.logger.info("******************* Governance Card showing INFO ********************")
            assert True
        else:
            self.logger.error("*************** Governance card is not showing Info **************")
            assert False
        if value is not None and int(value) > 0:
            self.logger.info("************* Governance Value is showing in Card *************")
            assert True
        else:
            self.logger.error("***************** Governance Value is not showing in Card **********")
            assert False
        if access_text is not None and access_text != access_text.upper() and access_text != access_text.lower():
            self.logger.info("******************* Governance Card showing Access Description ********************")
            assert True
        else:
            self.logger.error("*************** Governance card is not showing Description **************")
            assert False
    # Clicking of all the tabs
    def test_click_on_the_implementation_status_tab(self):
        self.driver.find_element(By.XPATH, self.pageobjects.Implementation_Status_tab).click()
        time.sleep(2)
        result = self.driver.find_element(By.XPATH, self.pageobjects.implementation_tab_result).get_attribute('aria-selected')
        if result == "true":
            self.logger.info("**************** Implementation Tab is Clicked ************")
            assert True
        else:
            self.logger.error("*************** Implementation Tab is not Clicked ***********")
            assert False

    def test_click_on_the_state_wise_status_tab(self):
        self.driver.find_element(By.XPATH, self.pageobjects.state_wise_tab).click()
        time.sleep(2)
        result = self.driver.find_element(By.XPATH, self.pageobjects.statewise_perf_tab_result).get_attribute('aria-selected')
        if result == "true":
            self.logger.info("**************** State Wise Performance Tab is Clicked ************")
            assert True
        else:
            self.logger.error("*************** State Wise Performance Tab is not Clicked ***********")
            assert False

    def test_click_on_the_district_wise_status_tab(self):
        self.driver.find_element(By.XPATH, self.pageobjects.district_wise_tab).click()
        time.sleep(2)
        result = self.driver.find_element(By.XPATH, self.pageobjects.districtwise_tab_result).get_attribute('aria-selected')
        if result == "true":
            self.logger.info("**************** District Wise Performance Tab is Clicked ************")
            assert True
        else:
            self.logger.error("*************** District Wise Performance Tab is not Clicked ***********")
            assert False


