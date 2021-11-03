from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from utils.Error import NoneError

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
        if is_none(args): raise NoneError(f'Teacher.py : function - __init__')
        self._id:str
        self._name:str
        self._subject:str
        self._subject_code:str
        self._id,self._name,self._subject,self._subject_code = args
        self._data:dict = {'teacher-id':self._id,'name':self._name,'subject':self._subject,'subject-code':self._subject_code}

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
    def subject_code(self) -> str:
        self._logger.log.info( f'property.getter - subject_code -> {self._subject_code}')
        return self._subject_code

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Teacher.py : property.setter - data')
        self._id, self._name, self._subject,self._subject_code = value
        self._data = value

    def __rpr__(self):
        return f'teachers[list = {self._data}]'

    def __str__(self):
         return f'teachers[list = {self._data}]'



