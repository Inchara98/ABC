import configparser
import os
import time
from pathlib import Path

import pytest
from selenium import webdriver
from get_directory import DirectoryPath

config = configparser.RawConfigParser()
# config.read("../Configurations/config.ini")
path = Path(__file__)
ROOT_DIR = os.path.abspath("../../../Configurations")
config_path = os.path.join(ROOT_DIR, "config.ini")
config.read(config_path)


class ReadConfig:

    def __init__(self,driver):
        self.driver = driver
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_state_ApplicationURL():
        url = config.get('common info', 'stateURL')
        return url

    @staticmethod
    def get_state_Username():
        username = config.get('common info', 'stateUser')
        return username

    @staticmethod
    def get_state_Password():
        password = config.get('common info', 'statePassword')
        return password

    @staticmethod
    @pytest.fixture()
    def setup():
        path = DirectoryPath()
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': path.get_download_dir()}
        options.add_experimental_option('prefs', prefs)
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options, executable_path=path.get_driver_path())
        driver.implicitly_wait(30)
        return driver

    @staticmethod
    def get_chrome_browser():
        p = DirectoryPath()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # headless enable or disable
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options, executable_path=p.get_driver_path())
        return driver

    def get_the_application(self):
        driver = self.get_chrome_browser()
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get("https://cqube-nvskpack.tibilprojects.com/")
        time.sleep(5)
        return driver
