import Tools
from log import module_log
from dataclasses import dataclass

''' 
        this module has teacher class that will contain
        all the teacher information that related to the 
        student information.
'''

@dataclass
class teacher:

    def __init__(self,args*):
        self._id:str, self._name:str, self._subject:str = args
        self._data:dict = {'subject':self._subject, 'teacher-id':self._id,'name':self._name}
        self._logger:module_log = module_log(log_name = 'teacher.log',disable_log = False)

    @property
    def id(self) -> str:
        self._logger.log.info(message = f'function id -> {self._id}')
        return self._id

    @property
    def name(self) -> str:
        self._logger.log.info(message = f'function name -> {self._name}')
        return self._name

    @property
    def subject(self) -> str:
        self._logger.log.info(message = f'function subject -> {self._subject}')
        return self._subject

    @property
    def data(self) -> dict:
        self._logger.log.info(message = f'property - data -> {self.data}')
        return self._data

    @property.setter
    def data(self,value: teacher) -> None:
        if is_none(teacher): raise NoneError(f'Teacher.py : property.setter - data')
        self._id:str, self._name:str, self._subject:str = value.data   
        self._data = value.data 

    ''' 
        this will show object information
    '''

    def __rpr__(self):
        return f'teachers[list = {self._teachers}]'

    def __str__(self):
         return f'teachers[list = {self._teachers}]'


