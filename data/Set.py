from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from dataclasses import dataclass

''' 
        this module has test class that will contain
        all the test information that related to the 
        student information.
'''

@dataclass
class set:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'set.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._level:str
        self._title:str = None
        self._set:list[test] = list()
        self._start_date:str
        self._end_date:str
        self._total_score:int
        self._level,self._title,self._start_date,self._end_date,self._set,self._total_score = args
        self._data:dict = {'level':self._level,'title':self._title,'start-date':self._start_date,'end-date':self._end_date, 'set':self._set, 'total-score':self._total_score}

    @property
    def level(self) -> str:
        self._logger.log.info(f'property.getter - level -> {self._level}')
        return self._level

    @property
    def title(self) -> str:
        self._logger.log.info(f'property.getter - title -> {self._title}')
        return self._title

    @property
    def set(self) -> list:
        self._logger.log.info(f'property.getter - set -> {self._set}')
        return self._set

    @property
    def start_date(self) -> str:
        self._logger.log.info(f'property.getter - start_date -> {self._start_date}')
        return self._start_date

    @property
    def end_date(self) -> str:
        self._logger.log.info(f'property.getter - end_date -> {self._end_date}')
        return self._end_date

    @property
    def total_score(self) -> int:
        self._logger.log.info(f'property.getter - total_score -> {self._total_score}')
        return self._total_score

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - full_data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Set.py : property.setter - data')
        self._level,self._title,self._start_date,self._end_date,self._set,self._total_score = value
        self._data = value

    def __rpr__(self):
        return f'set[ {self._data} ]'

    def __str__(self):
        return f'set[ {self._data} ]'

       
