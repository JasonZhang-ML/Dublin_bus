import os
import logging
import logging.handlers as handlers


class Logger():

    def __init__(self, logger_name='MyLogger', logger_dir='.', console_log=True):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)
        log_path = os.path.join(logger_dir, '{}.log'.format(logger_name))
        file_handler = handlers.TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=2)
        
        fmt = logging.Formatter('[%(levelname)s]%(asctime)s: %(message)s')
        file_handler.setFormatter(fmt)
        self.__logger.addHandler(file_handler)
        
        if console_log:
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            console.setFormatter(fmt)
            self.__logger.addHandler(console)
    
    def INFO(self, *args):
        self.__logger.info(*args)

    def ERROR(self, *args):
        self.__logger.error(*args)

    def FATAL(self, *args):
        self.__logger.critical(*args)

    def WARN(self, *args):
        self.__logger.warning(*args)

    def DEBUG(self, *args):
        self.__logger.debug(*args)