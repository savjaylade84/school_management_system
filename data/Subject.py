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

        self._subject_code:str
        self._subject:str
        self._minimal_req:str
        
        self._subject_code,self._subject,self._minimal_req = args
        self._data:dict = {'subject-code':self._subject_code,'subject':self._subject,'level-minimal-requirement':self._minimal_req}

    @property
    def subject_code(self) -> str:
        self._logger.log.info(f'property.getter - subject_code -> {self._subject_code}')
        return self._subject_code

    @property
    def subject(self) -> str:
        self._logger.log.info(f'property.getter - subject -> {self._subject}')
        return self._subject   

    @property
    def minimal_req(self) -> str:
        self._logger.log.info(f'property.getter - minimal_req -> {self._minimal_req}')
        return self._minimal_req     

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Student.py : property.setter - data')
        self._subject_code,self._subject,self._minimal_req = value
        self._data = value