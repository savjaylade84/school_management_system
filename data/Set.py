import Tools
from Grade import grade
from log import module_logs

''' 
        this module has test class that will contain
        all the test information that related to the 
        student information.
'''

class set:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'set.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._title:str = None
        self._set:list[test] = list()
        self._date:str
        self._total_score:int
        self._title,self._date,self._set,self._total_score = args
        self._data:dict = {'title':self._title,'date':self._date, 'set':self._set, 'total-score':self._total_score}

    @property
    def title(self) -> str:
        self._logger.log.info(f'property.getter - title -> {self._title}')
        return self._title

    @property
    def set(self) -> list:
        self._logger.log.info(f'property.getter - set -> {self._set}')
        return self._set

    @property
    def date(self) -> str:
        self._logger.log.info(f'property.getter - date -> {self._date}')
        return self._date

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
        self._title,self._date,self._set,self._total_score = value
        self._data = value

    def __rpr__(self):
        return f'set[{self._data}]'

    def __str__(self):
        return f'set[{self._data}]'

       
