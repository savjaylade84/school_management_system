from logs.log import module_log

logger = module_log(log_name = 'error.log',disable_log = False)

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message,*input):
        self._message = f'{message} -> [ Input Value ] : [ {input} ]'
        logger.log.warning(f'InputError:{self._message}')

class FileNotFoundError(Error):
    def __init__(self,message,file_name):
        self._message = f'{message} -> [ File Not Found ] @ {file_name}'
        logger.log.warning(f'FileNotFoundError:{self._message}')

class NoneError(Error):
    def __init__(self,message):
        self._message = f'{message} -> [ None Value ]'
        logger.log.warning(f'NoneError:{self._message}')


class DisableError(Error):
    def __init__(self,message):
        self._message = f'{message} -> [ Disable ]'
        logger.log.warning(f'DisableError:{self._message}')