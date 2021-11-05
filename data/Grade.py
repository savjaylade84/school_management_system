from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none

@dataclass
class grade:
    
    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'grade.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._subject_code:str
        self._teacher_id:str
        self._date:str
        self._grade:int
        self._subject_code,self._teacher_id, self._date, self._grade = args
        self._data = ('subject-code':self._subject_code,'teacher-id':self._teacher_id,'date':self._date,'grade:':self._grade)

    @property
    def subject_code(self) -> str:
        self._logger.log.info(f'property.getter - subject_code -> {self._subject_code}')
        return self._subject_code

    @property
    def teacher_id(self) -> str:
        self._logger.log.info(f'property.getter - teacher_id -> {self._teacher_id}')
        return self._teacher_id

    @property
    def date(self) -> str:
        self._logger.log.info(f'property.getter - date -> {self._date}')
        return self._date

        @property
    def grade(self) -> int:
        self._logger.log.info(f'property.getter - grade -> {self._grade}')
        return self._grade


     @property
    def data(self) -> str:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Report.py : property.setter - data')
        self._subject_code,self._teacher_id, self._date, self._grade = value
        self._data = value

    def __rpr__(self):
        return f'grade[ {self._data} ]'

    def __str__(self):
         return f'grade[ {self._data} ]'

