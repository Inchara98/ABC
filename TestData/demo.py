import configparser
import os.path

from TestData.optimising_cardinfo import API_Responses
from utilities.readProperties import ReadConfig

api_info = API_Responses()
config = configparser.RawConfigParser()

configure = configparser.ConfigParser()
configure.read("../../../Configurations/config.ini")
url = configure.get('common info', 'baseURL')
print(url)
# username = config.getUsername()
# password = config.getPassword()
# print(url, username, password)
