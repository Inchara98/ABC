
from selenium import webdriver

from get_directory import DirectoryPath


class ReadConfig:
    path = DirectoryPath()
    config = path.get_config_ini()

    @staticmethod
    def get_chrome_browser():
        p = DirectoryPath()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # headless enable or disable
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options, executable_path=p.get_driver_path())
        return driver

    @staticmethod
    def getApplicationURL(self):
        url = self.config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername(self):
        username = self.config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword(self):
        password = self.config.get('common info', 'password')
        return password
