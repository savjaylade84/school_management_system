from logs.log import module_log

logger = module_log(log_name = 'error.log',disable_log = False)

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message,*input):
        self.__message = f'{message} -> [ Input Value ] : [ {input} ]'
        logger.log.warning(f'InputError:{self.__message}')

class FileNotFoundError(Error):
    def __init__(self,message,file_name):
        self.__message = f'{message} -> [ File Not Found ] @ {file_name}'
        logger.log.warning(f'FileNotFoundError:{self.__message}')

class NoneError(Error):
    def __init__(self,message):
        self.__message = f'{message} -> [ None Value ]'
        logger.log.warning(f'NoneError:{self.__message}')


class DisableError(Error):
    def __init__(self,message):
        self.__message = f'{message} -> [ Disable ]'
        logger.log.warning(f'DisableError:{self.__message}')