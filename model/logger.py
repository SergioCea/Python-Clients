import logging
import os
from logging.handlers import TimedRotatingFileHandler
import yaml


class Logger:
    def __init__(self, settings_file: str = ''):
        self.log_dir = None
        self.log_level = None
        self.log_days = None

        self.configure_settings(settings_file)
        self.logger = self.create_timed_rotating_log()

    def configure_settings(self, settings_file):
        with open(settings_file) as stream:
            try:
                conf = yaml.safe_load(stream)
                self.log_dir = conf.get('log_dir')
                self.log_level = conf.get('log_level')
                self.log_days = conf.get('log_days')
            except yaml.YAMLError as e:
                print(e)

    def create_timed_rotating_log(self):
        # Create de folder
        folderExist = os.path.exists(self.log_dir)
        if not folderExist:
            os.makedirs(self.log_dir)
        # Creates a rotating log
        logger = logging.getLogger('facturacion')
        level = logging.getLevelName(self.log_level)
        logger.setLevel(level)

        # Here we define our formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file = self.log_dir+"facturacion.log"

        logHandler = TimedRotatingFileHandler(log_file, "midnight", backupCount=self.log_days)
        logHandler.suffix = "%Y-%m-%d"
        logHandler.setLevel(level)
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)

        return logger
