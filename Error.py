import Exception
from log import module_log

logger = module_log(log_name = 'error.log',disable_log = False)

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        logger.log.warning(f'InputError:{message}')
        self.message = message

class FileNotFoundError(Error):
    def __init__(self,message,file_name):
        logger.log.warning(f'FileNotFoundError:{message}')
        self.message = message
        self.file_name = file_name

class NoneError(Error):
    def __init__(self,message)
        logger.log.warning(f'NoneError:{message}')
        self.message