import logging
from logging.config import fileConfig


class Logger:
    def __init__(self):
        fileConfig('data/logger.ini')

    @staticmethod
    def instance():
        """
        Creates logger instance
        :return: returns newly created logger instance
        """
        return logging.getLogger()
