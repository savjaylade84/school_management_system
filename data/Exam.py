from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Set import set

class exam:


    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'set.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._level:str
        self._sets:list[set] = list()
        self._level,self._sets = args
        self._data:dict = {'level':self._level,'sets':self._sets}

    @property
    def level(self) -> str:
        self._logger.log.info(f'property.getter - level -> {self._level}')
        return self._level

    @property
    def sets(self) -> list:
        self._logger.log.info(f'property.getter - sets -> {self._sets}')
        return self._sets

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Set.py : property.setter - data')
        self._level,self._sets = value
        self._data = value

    def __rpr__(self):
        return f'exam[ {self._data} ]'

    def __str__(self):
        return f'exam[ {self._data} ]'
