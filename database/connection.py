import json
from logs.log import module_log
from utils.Tools import is_none

class db_connection:

    def __init__(self,file_path = "",data_path = ""):
         # create the log 
        self._logger:module_log = module_log(log_name = 'database.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {file_path,data_path}')
        self._file_path:str = file_path
        self._data_path:str = data_path
        self._data:str = dict()
        self._logger.log.debug(f'__init__ <- {self._file_path,self._data_path,self._data}')

    def connect(self) -> None:
        with open(self._file_path,'r') as file:
            self._data = json.load(file)
            if is_none(self._data): raise NoneError(f'connection.py : function - connect')
        self._logger.log.info(f'function - connection -> {self._data}')

    @property
    def object(self) -> dict:
           return self._data[self._data_path]

    @object.setter
    def object(self,object:dict) -> None:
        if is_none(self._data): raise NoneError(f'connection.py : property.setter - object')
        self._logger.log.info(f' property.setter object <- {object}')
        self._data[self._data_path] = object

    def save(self) -> bool:
        with open(self._file_path,'w') as file:
            json.dump(self._data,file,indent=2)
            return True
        return False