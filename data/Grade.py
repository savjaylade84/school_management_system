from data.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from Tools import is_none

@dataclass
class grade:
    
    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'test.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._title:str
        self._date:str
        self._grade:int
        self._title, self._date, self._grade = args
        self._data = ('title':self._title,'date':self._date,'grade:':self._grade)

    @property
    def title(self) -> str:
        self._logger.log.info(f'property.getter - title -> {self._title}')
        return self._title

    @property
    def date(self) -> str:
        self._logger.log.info(f'property.getter - date -> {self._date}')
        return self._date

        @property
    def grade(self) -> int:
        self._logger.log.info(f'property.getter - grade -> {self._grade}')
        return self._grade

