from  utils.Error import NoneError
from utils.Tools import is_none
from dataclasses import dataclass

''' 
        this module has student class that will contain
        all the student information that related to the 
        student information.

        take note course is different in subject data
        course is just master list of all courses available 
        then subject is one of collection(each selected from course)
'''

@dataclass
class student:
    
    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_teacher_id = 'subject.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')

        self._code:str
        self._teacher_id:str
        self._grade:double
        
        self._code,self._teacher_id,self._grade = args
        self._data:dict = {'code':self._code,'teacher-id':self._teacher_id,'grade':self._grade}

    @property
    def code(self) -> str:
        self._logger.log.info(f'property.getter - code -> {self._code}')
        return self._code

    @property
    def teacher_id(self) -> str:
        self._logger.log.info(f'property.getter - teacher_id -> {self._teacher_id}')
        return self._teacher_id   

    @property
    def grade(self) -> double:
        self._logger.log.info(f'property.getter - grade -> {self._grade}')
        return self._grade   

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Subject.py : property.setter - data')
        self._code,self._teacher_id = value
        self._data = value


    def __rpr__(self):
        return f'subject[ {self._data} ]'

    def __str__(self):
         return f'subject[ {self._data} ]'