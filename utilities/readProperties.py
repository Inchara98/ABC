import configparser
import os

from selenium import webdriver
from get_directory import DirectoryPath


class ReadConfig:
    path = DirectoryPath()
    config = configparser.RawConfigParser()
    data = config.read(os.path.join('../../../Configurations/config.ini'))

    @staticmethod
    def get_chrome_browser():
        p = DirectoryPath()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # headless enable or disable
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options, executable_path=p.get_driver_path())
        return driver

    def getApplicationURL(self):
        url = self.config.get('common info', 'baseURL')
        return url

    def getUsername(self):
        username = self.config.get('common info', 'username')
        return username

    def getPassword(self):
        password = self.config.get('common info', 'password')
        return password

    def get_state_ApplicationURL(self):
        url = self.config.get('common info', 'stateURL')
        return url

    def get_state_Username(self):
        username = self.config.get('common info', 'stateUser')
        return username

    def get_state_Password(self):
        password = self.config.get('common info', 'statePassword')
        return password
