from  utils.Error import NoneError
from utils.Tools import is_none
from dataclasses import dataclass

''' 
        this module has subject class that will contain
        all the student information that related to the 
        subject information.
'''

@dataclass
class subject:
    
    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'subject.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')

        self._code:str
        self._name:str
        self._minimal_req:str
        
        self._code,self._name = args
        self._data:dict = {'code':self._code,'name':self._name}

    @property
    def code(self) -> str:
        self._logger.log.info(f'property.getter - code -> {self._code}')
        return self._code

    @property
    def name(self) -> str:
        self._logger.log.info(f'property.getter - name -> {self._name}')
        return self._name   

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Student.py : property.setter - data')
        self._code,self._name = value
        self._data = value