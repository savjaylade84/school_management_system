from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Student import student

@dataclass
class subject:
    
    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'grade.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._level:str
        self._start_date:str
        self._end_date:str
        self._subjects:list[subject]
        self._level,self._start_date, self._end_date, self._subjects = args
        self._data = ('level':self._level,'start-date':self._start_date,'end-date':self._date,'subjects:':self._subjects)

    @property
    def level(self) -> str:
        self._logger.log.info(f'property.getter - level -> {self._level}')
        return self._level

    @property
    def start_date(self) -> str:
        self._logger.log.info(f'property.getter - start_date -> {self._start_date}')
        return self._start_date

    @property
    def end_date(self) -> str:
        self._logger.log.info(f'property.getter - end_date -> {self._end_date}')
        return self._end_date

        @property
    def subjects(self) -> int:
        self._logger.log.info(f'property.getter - subjects -> {self._subjects}')
        return self._subjects


     @property
    def data(self) -> str:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Grade.py : property.setter - data')
        self._level,self._start_date, self._end_date, self._subjects = value
        self._data = value

    def __rpr__(self):
        return f'subject[ {self._data} ]'

    def __str__(self):
         return f'subject[ {self._data} ]'

