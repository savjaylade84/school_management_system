import Error
from log import module_log
from dataclasses import dataclass
from Tools import is_none

@dataclass
class report:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'report.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._title:str
        self._note:str
        self._date:str
        self._complainer:str
        self.status:str
        self._title:str, self._note:str, self._date:str, self._complainer:str, self.status = args
        self._data = {'title':self._title,'note':self._note,'date':self._date,'complaint-by':self._complainer,'status':self._status}

    @property
    def title(self) -> str:
        self._logger.log.info(f'property.getter - title -> {self._title}')
        return self._title

    @property
    def note(self) -> str:
        self._logger.log.info(f'property.getter - note -> {self._note}')
        return self._note

    @property
    def date(self) -> str:
        self._logger.log.info(f'property.getter - title -> {self._date}')
        return self._date

    @property
    def complainer(self) -> str:
        self._logger.log.info(f'property.getter - complainer -> {self._complainer}')
        return self._complainer

    @property
    def status(self) -> str:
        self._logger.log.info(f'property.getter - status -> {self._status}')
        return self._status

    @property
    def data(self) -> str:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Report.py : property.setter - data')
        self._title:str, self._note:str, self._date:str, self._complainer:str, self.status = value
        self._data = value