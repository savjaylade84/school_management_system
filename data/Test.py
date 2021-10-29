from data.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from Tools import is_none

''' 
        this module has test class that will contain
        all the test information that related to the 
        student information.
'''

@dataclass
class test:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'test.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._subject_code:str
        self._subject:str
        self._score:str
        self._subject, self._score = args
        self._data:dict = {'subject-code':self._subject_code,'subject':self._subject, 'score':self._score}

    @property
    def subject_code(self) -> str:
        self._logger.log.info(f'property.getter - subject -> {self._subject_code}')
        return self._subject_code

    @property
    def subject(self) -> str:
        self._logger.log.info(f'property.getter - subject -> {self._subject}')
        return self._subject

    @property
    def score(self) -> int:
        self._logger.log.info(f'property.getter - score -> {self._score}')
        return self._score

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Test.py : property.setter - data')
        self._subject, self._score = value
        self._data = value

    def __rpr__(self):
        return f'test[{self.data}]'

    def __str__(self):
        return f'test[{self.data}]'

