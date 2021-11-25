import json
from logs.log import module_log
from utils.Tools import is_none

class db_connection:

    ##################################[initialising]#####################################################
    def __init__(self,file_path:str,data_path:str):

         # create the log 
        self.__logger:module_log = module_log(log_name = 'database.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {file_path,data_path}')

        #initialize
        self.__file_path:str = file_path
        self.__data_path:str = data_path
        self.__data:str = dict()

        self.__logger.log.debug(f'__init__ <- {self.__file_path,self.__data_path,self.__data}')

    def connect(self) -> None:
        with open(self.__file_path,'r') as file:
            self.__data = json.load(file)
            if is_none(self.__data): raise NoneError(f'connection.py : function - connect')
        self.__logger.log.info(f'function - connection -> {self.__data}')

    def save(self) -> bool:
        with open(self.__file_path,'w') as file:
            json.dump(self.__data,file,indent=2)
            return True
        return False

    ##################################[connection properties]#####################################################

    @property
    def object(self) -> dict:
           return self.__data[self.__data_path]

    @object.setter
    def object(self,object:dict) -> None:
        if is_none(self.__data): raise NoneError(f'connection.py : property.setter - object')
        self.__logger.log.info(f' property.setter object <- {object}')
        self.__data[self.__data_path] = object
