import logging
import re
import time
from selenium.webdriver.common.by import By
from PageObjects.Dashboard_Page import Dashboard_Objects
from utilities import Programs_logGen
from utilities.readProperties import ReadConfig


class Test_Dashboard_Cards:
    data = ReadConfig()
    pageobjects = Dashboard_Objects()
    driver = data.navigate_to_dashboard()
    driver.implicitly_wait(50)
    logger = Programs_logGen.setup_logger('Dashboard_Cards', pageobjects.dashboard_logfile, level=logging.DEBUG)

    def test_validate_nishtha_card_metrics(self):
        nishtha_info = self.driver.find_element(By.XPATH, self.pageobjects.nishtha_info).get_attribute('title')
        teacher = self.driver.find_element(By.XPATH, self.pageobjects.total_teachers).text
        teacher_value = re.sub(self.pageobjects.L, "", teacher)
        course = self.driver.find_element(By.XPATH, self.pageobjects.total_course).text
        course_value = re.sub(self.pageobjects.K, "", course)
        teacher_text = self.driver.find_element(By.XPATH, self.pageobjects.teacher_text).text
        course_text = self.driver.find_element(By.XPATH, self.pageobjects.course_text).text
        if nishtha_info is not None and teacher_text is not None and course_text is not None:
            self.logger.info("*********** Nishtha Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if float(teacher_value) > 0 and teacher_value is not None:
            self.logger.info("*********** Nishtha Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if float(course_value) > 0 and course_value is not None:
            self.logger.info("*********** Nishtha Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False

    def test_check_navigation_to_nishtha_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.Nisha_dashboard).click()
        time.sleep(5)
        if 'nishtha' in self.driver.current_url and 'NISHTHA' in self.driver.page_source:
            self.logger.info("******************* Nishtha Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** Nishtha Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_diksha_card_metrics(self):
        diksha_info = self.driver.find_element(By.XPATH, self.pageobjects.diksha_info).get_attribute('title')
        total_content = self.driver.find_element(By.XPATH, self.pageobjects.total_content).text
        content_value = re.sub(self.pageobjects.L, "", total_content)
        total_etbs = self.driver.find_element(By.XPATH, self.pageobjects.total_etbs).text
        etb_value = re.sub(self.pageobjects.K, "", total_etbs)
        content_text = self.driver.find_element(By.XPATH, self.pageobjects.content_text).text
        etb_text = self.driver.find_element(By.XPATH, self.pageobjects.etb_text).text
        if diksha_info is not None and content_text is not None and etb_text is not None:
            self.logger.info("*********** Diksha Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Diksha Card Values is Missing ************")
            assert False
        if float(content_value) > 0 and content_value is not None:
            self.logger.info("*********** DIKSHA-ETB Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** DIKSHA-ETB Card Values is Missing ************")
            assert False
        if float(etb_value) > 0 and etb_value is not None:
            self.logger.info("*********** DIKSHA-ETB Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** DIKSHA-ETB Card Values is Missing ************")
            assert False

    def test_check_navigation_to_diksha_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.Diksha_dashboard).click()
        time.sleep(5)
        if 'etb' in self.driver.current_url and 'DIKSHA- ETB and eContent' in self.driver.page_source:
            self.logger.info("******************* DIKSHA-ETB Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** DIKSHA-ETB Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_micro_improvements_card_metrics(self):
        micro_info = self.driver.find_element(By.XPATH, self.pageobjects.micro_info).get_attribute('title')
        total_states = self.driver.find_element(By.XPATH, self.pageobjects.total_states).text
        tot_value = int(re.sub('\D', "", total_states))
        total_micro = self.driver.find_element(By.XPATH, self.pageobjects.total_micro).text
        micro_value = re.sub(self.pageobjects.K, "", total_micro)
        micro_text = self.driver.find_element(By.XPATH, self.pageobjects.micro_text).text
        states_text = self.driver.find_element(By.XPATH, self.pageobjects.states_text).text
        if micro_info is not None and micro_text is not None and states_text is not None:
            self.logger.info("*********** Micro Improvement Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro Improvement Card Values is Missing ************")
            assert False
        if int(tot_value) > 0 and tot_value is not None:
            self.logger.info("*********** Micro Improvement Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro Improvement Card Values is Missing ************")
            assert False
        if float(micro_value) > 0 and micro_value is not None:
            self.logger.info("*********** Micro Improvement Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Micro Improvement Card Values is Missing ************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_check_navigation_to_micro_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.Micro_Dashboard).click()
        time.sleep(5)
        if 'microimprovement' in self.driver.current_url and 'Micro-Improvements' in self.driver.page_source:
            self.logger.info("******************* Micro Improvement Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** Micro Improvement Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_pm_poshan_improvements_card_metrics(self):
        pm_info = self.driver.find_element(By.XPATH, self.pageobjects.pm_info).get_attribute('title')
        total_schools = self.driver.find_element(By.XPATH, self.pageobjects.total_schools).text
        school_value = re.sub(self.pageobjects.L, "", total_schools)
        total_state = self.driver.find_element(By.XPATH, self.pageobjects.total_state).text
        state_value = re.sub('\D', "", total_state)
        schools_text = self.driver.find_element(By.XPATH, self.pageobjects.schools_text).text
        pmstate_text = self.driver.find_element(By.XPATH, self.pageobjects.pmstate_text).text
        if pm_info is not None and schools_text is not None and pmstate_text is not None:
            self.logger.info("*********** PM POSHAN Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM POSHAN Card Values is Missing ************")
            assert False
        if float(school_value) > 0 and school_value is not None:
            self.logger.info("*********** PM POSHAN Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM POSHAN Card Values is Missing ************")
            assert False
        if int(state_value) > 0 and state_value is not None:
            self.logger.info("*********** PM POSHAN Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM POSHAN Card Values is Missing ************")
            assert False

    def test_check_navigation_to_pm_poshan_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.PM_dashboard).click()
        time.sleep(5)
        if 'poshan' in self.driver.current_url and 'PM POSHAN' in self.driver.page_source:
            self.logger.info("******************* PM-POSHAN Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** PM-POSHAN Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_nas_card_metrics(self):
        nas_info = self.driver.find_element(By.XPATH, self.pageobjects.nas_info).get_attribute('title')
        total_std_surveyed = self.driver.find_element(By.XPATH, self.pageobjects.total_std_surveyed).text
        std_value = re.sub(self.pageobjects.L, "", total_std_surveyed)
        total_scs_surveyed = self.driver.find_element(By.XPATH, self.pageobjects.total_scs_surveyed).text
        scs_value = re.sub(self.pageobjects.L, "", total_scs_surveyed)
        school_survey_text = self.driver.find_element(By.XPATH, self.pageobjects.school_survey_text).text
        student_survey_text = self.driver.find_element(By.XPATH, self.pageobjects.student_survey_text).text
        if nas_info is not None and school_survey_text is not None and student_survey_text is not None:
            self.logger.info("*********** NAS Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NAS Card Values is Missing ************")
            assert False
        if float(std_value) > 0 and std_value is not None:
            self.logger.info("*********** NAS Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NAS Card Values is Missing ************")
            assert False
        if float(scs_value) > 0 and scs_value is not None:
            self.logger.info("*********** NAS Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NAS Card Values is Missing ************")
            assert False

    def test_check_navigation_to_nas_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.NAS_dashboard).click()
        time.sleep(5)
        if 'nas' in self.driver.current_url and 'National Achievement Survey' in self.driver.page_source:
            self.logger.info("******************* NAS Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** NAS Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_udise_card_metrics(self):
        udise_info = self.driver.find_element(By.XPATH, self.pageobjects.udise_info).get_attribute('title')
        ts_surveyed = self.driver.find_element(By.XPATH, self.pageobjects.ts_surveyed).text
        ts_value = re.sub(self.pageobjects.L, "", ts_surveyed)
        total_teacher = self.driver.find_element(By.XPATH, self.pageobjects.total_teacher).text
        teacher_value = re.sub(self.pageobjects.L, "", total_teacher)
        ts_text = self.driver.find_element(By.XPATH, self.pageobjects.ts_text).text
        teachers_text = self.driver.find_element(By.XPATH, self.pageobjects.teachers_text).text
        if udise_info is not None and ts_text is not None and teachers_text is not None:
            self.logger.info("*********** UDISE+ Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** UDISE+ Card Values is Missing ************")
            assert False
        if float(ts_value) > 0 and ts_value is not None:
            self.logger.info("*********** UDISE+ Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** UDISE+ Card Values is Missing ************")
            assert False
        if float(teacher_value) > 0 and teacher_value is not None:
            self.logger.info("*********** UDISE+ Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** UDISE+ Card Values is Missing ************")
            assert False

    def test_check_navigation_to_udise_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.UDISE_dashbord).click()
        time.sleep(5)
        if 'udise' in self.driver.current_url and 'UDISE+' in self.driver.page_source:
            self.logger.info("******************* UDISE+ Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** UDISE+ Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_pgi_card_metrics(self):
        pgi_info = self.driver.find_element(By.XPATH, self.pageobjects.pgi_info).get_attribute('title')
        pg_states = self.driver.find_element(By.XPATH, self.pageobjects.pg_states).text
        state_value = int(re.sub('\D', "", pg_states))
        pg_parameters = self.driver.find_element(By.XPATH, self.pageobjects.pg_parameters).text
        parameter_value = int(re.sub('\D', "", pg_parameters))
        pg_state_text = self.driver.find_element(By.XPATH, self.pageobjects.pg_state_text).text
        pg_parameters_text = self.driver.find_element(By.XPATH, self.pageobjects.pg_parameters_text).text
        if pgi_info is not None and pg_state_text is not None and pg_parameters_text is not None:
            self.logger.info("*********** PGI Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PGI Card Values is Missing ************")
            assert False
        if int(state_value) > 0 and state_value is not None:
            self.logger.info("*********** PGI Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PGI Card Values is Missing ************")
            assert False
        if int(parameter_value) > 0 and parameter_value is not None:
            self.logger.info("*********** PGI Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PGI Card Values is Missing ************")
            assert False

    def test_check_navigation_to_PGI_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.PGI_dashboard).click()
        time.sleep(5)
        if 'pgi' in self.driver.current_url and 'Perfomance Grading Index' in self.driver.page_source:
            self.logger.info("******************* PGI Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** PGI Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_nipun_card_metrics(self):
        nipun_info = self.driver.find_element(By.XPATH, self.pageobjects.nipun_info).get_attribute('title')
        total_learnings = self.driver.find_element(By.XPATH, self.pageobjects.total_learnings).text
        learnings_value = re.sub(self.pageobjects.L, "", total_learnings)
        total_contents = self.driver.find_element(By.XPATH, self.pageobjects.total_contents).text
        contents_value = re.sub(self.pageobjects.K, "", total_contents)
        learning_text = self.driver.find_element(By.XPATH, self.pageobjects.learning_text).text
        contents_text = self.driver.find_element(By.XPATH, self.pageobjects.contents_text).text
        if nipun_info is not None and learning_text is not None and contents_text is not None:
            self.logger.info("*********** NIPUN Bharath Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NIPUN Bharath Card Values is Missing ************")
            assert False
        if float(learnings_value) > 0 and learnings_value is not None:
            self.logger.info("*********** NIPUN Bharath Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NIPUN Bharath Card Values is Missing ************")
            assert False
        if float(contents_value) > 0 and contents_value is not None:
            self.logger.info("*********** NIPUN Bharath Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NIPUN Bharath Card Values is Missing ************")
            assert False

    def test_check_navigation_to_NIPUN_Bharath_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.NIPUN_dashboard).click()
        time.sleep(5)
        if 'nipunbharath' in self.driver.current_url and 'NIPUN Bharat' in self.driver.page_source:
            self.logger.info("******************* NIPUN Bharath Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** NIPUN Bharath Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_ncert_card_metrics(self):
        ncert_info = self.driver.find_element(By.XPATH, self.pageobjects.ncert_info).get_attribute('title')
        total_enrolment = self.driver.find_element(By.XPATH, self.pageobjects.total_enrolment).text
        enrolment_value = re.sub(self.pageobjects.L, "", total_enrolment)
        total_certification = self.driver.find_element(By.XPATH, self.pageobjects.total_certification).text
        certfication_value = re.sub(self.pageobjects.K, "", total_certification)
        enrolment_text = self.driver.find_element(By.XPATH, self.pageobjects.enrolment_text).text
        certification_text = self.driver.find_element(By.XPATH, self.pageobjects.certification_text).text
        if ncert_info is not None and enrolment_text is not None and certification_text is not None:
            self.logger.info("*********** NCERT Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCERT Card Values is Missing ************")
            assert False
        if float(enrolment_value) > 0 and enrolment_value is not None:
            self.logger.info("*********** NCERT Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCERT Card Values is Missing ************")
            assert False
        if float(certfication_value) > 0 and certfication_value is not None:
            self.logger.info("*********** NCERT Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCERT Card Values is Missing ************")
            assert False

    def test_check_navigation_to_NCERT_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.NCERT_dashboard).click()
        time.sleep(5)
        if 'quizzes' in self.driver.current_url and 'NCERT Quiz' in self.driver.page_source:
            self.logger.info("******************* NCERT Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** NCERT Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_validate_ncf_card_metrics(self):
        ncf_info = self.driver.find_element(By.XPATH, self.pageobjects.ncf_info).get_attribute('title')
        total_participating = self.driver.find_element(By.XPATH, self.pageobjects.total_participating).text
        participating_value = re.sub('\D', "", total_participating)
        total_paper = self.driver.find_element(By.XPATH, self.pageobjects.total_paper).text
        paper_value = re.sub('\D', "", total_paper)
        participating_text = self.driver.find_element(By.XPATH, self.pageobjects.participating_text).text
        paper_text = self.driver.find_element(By.XPATH, self.pageobjects.paper_text).text
        if ncf_info is not None and participating_text is not None and paper_text is not None:
            self.logger.info("*********** NCF Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCF Card Values is Missing ************")
            assert False
        if int(participating_value) > 0 and participating_value is not None:
            self.logger.info("*********** NCF Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCF Card Values is Missing ************")
            assert False
        if int(paper_value) > 0 and paper_value is not None:
            self.logger.info("*********** NCF Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** NCF Card Values is Missing ************")
            assert False

    def test_check_navigation_to_ncf_dashboard(self):
        self.driver.find_element(By.XPATH, self.pageobjects.NCF_dashboard).click()
        time.sleep(5)
        if 'ncf' in self.driver.current_url and 'National Curriculum Framework' in self.driver.page_source:
            self.logger.info("******************* NCF Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** NCF Dashboard Button is not Working ******************")
            assert False
        self.driver.find_element(By.ID, self.pageobjects.Dashboard_btn).click()

    def test_a_plus_button_on_cm_status(self):
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
        a_minus = self.data.test_click_on_A_minus_button(self.driver)
        if a_minus == 0:
            self.logger.info("********** A- button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A- button is not working as expected ****************")
            assert False

    def test_a_default_button_on_cm_status(self):
        a_plus = self.data.test_click_on_A_default_button(self.driver)
        if a_plus == 0:
            self.logger.info("********** A button is working as expected ******************")
            self.driver.refresh()
            assert True
        else:
            self.logger.error("************** A  button is not working as expected ****************")
            assert False
