import logging
import logging.config
import yaml

''' 
    this module will log every module in the system

    in the constructor of the module_log:

    --log_name - the name of the logger of the module
    --disable_log - this will disable the log of the entire logs in
                    module

    in every function in module_log:
    --message - the message that will input
    --disable - this will exclude a log from disabling the entire logs in
                the constructor 

'''

class module_log:
    
    def __init__(self,log_name:str = " ",disable_log: bool = False):
        ''' 
            get the configuration of the logging in the .config
            directory
        '''
        with open('./logs/.config/log.yaml','r') as file:
            self._yaml = yaml.load(file,Loader=yaml.FullLoader)     # convert the yaml object to json object
        logging.config.dictConfig(self._yaml)                       # load the json object that has log config
        self._logger = logging.getLogger(log_name)                  # get the logger name in the log config
        self._disable_log = disable_log                             # this will diable the entire logs in the module

    @property
    def log(self):
        if self._disable_log: raise NoneError(f'log.py : property.getter - data')
        return self._logger

