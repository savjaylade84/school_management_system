import Error
from log import module_log
from dataclasses import dataclass
from Tools import is_none

''' 
        this module has teacher class that will contain
        all the teacher information that related to the 
        student information.
'''

@dataclass
class teacher:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'teacher.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._id:str
        self._name:str
        self._subject:str
        self._id,self._name,self._subject = args
        self._data:dict = {'subject':self._subject, 'teacher-id':self._id,'name':self._name}

    @property
    def id(self) -> str:
        self._logger.log.info( f'property.getter - id -> {self._id}')
        return self._id

    @property
    def name(self) -> str:
        self._logger.log.info( f'property.getter - name -> {self._name}')
        return self._name

    @property
    def subject(self) -> str:
        self._logger.log.info( f'property.getter - subject -> {self._subject}')
        return self._subject

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Teacher.py : property.setter - data')
        self._id, self._name, self._subject = value
        self._data = value

    def __rpr__(self):
        return f'teachers[list = {self._data}]'

    def __str__(self):
         return f'teachers[list = {self._data}]'


