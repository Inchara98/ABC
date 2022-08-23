import logging
from os import remove
from os.path import exists

from PageObjects.Dashboard_Page import Dashboard_Objects
from get_directory import DirectoryPath

location = DirectoryPath()

logfiles = Dashboard_Objects()


def setup_logger(logger_name, log_file, level=logging.WARNING):
    # Erase log if already exists
    if exists(log_file):
        remove(log_file)
    # Configure log file
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)
    return l


if __name__ == '__main__':
    setup_logger('log_pl', logfiles.login_logfile, logging.DEBUG)
