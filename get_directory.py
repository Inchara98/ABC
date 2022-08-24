import configparser
import os


class DirectoryPath:
    cwd = os.path.dirname(__file__)

    def get_driver_path(self):
        driver_path = os.path.join(self.cwd, 'Driver/chromedriver')
        return driver_path

    def get_config_ini(self):
        config = configparser.RawConfigParser()
        config.read("../Configurations/config.ini")
        return config

    # logic to get report file
    def get_functional_report(self):
        func_report = os.path.join(self.cwd, 'Reports/Functional_Reports/Functional_Result.html')
        return func_report

    def get_regression_report(self):
        regression_report = os.path.join(self.cwd, 'Reports/Regression_Reports/Regression_Result.html')
        return regression_report

    def get_smoke_report(self):
        smoke_report = os.path.join(self.cwd, 'Reports/Smoke_Reports/Smoke_Result.html')
        return smoke_report

    def get_download_dir(self):
        download_path = os.path.join(self.cwd, 'Downloads')
        return download_path

    # logic to get path of log files
    def get_login_logfile(self):
        login_file = os.path.join(self.cwd, 'Login.log')
        return login_file

    def get_dashboard_logfile(self):
        dashboard_file = os.path.join(self.cwd, 'Dashboard.log')
        return dashboard_file

    def get_program_logfile(self):
        program_file = os.path.join(self.cwd, 'Program.log')
        return program_file
