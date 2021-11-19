from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none

@dataclass
class report:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'report.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        self._id:str
        self._type:str
        self._title:str
        self._note:str
        self._date:str
        self._complainer:str
        self._status:str
        self._id,self._type,self._title:str, self._note:str, self._date:str, self._complainer:str, self._status = args
        self._data = {'student-id':self._id,'type':self._type,'title':self._title,'note':self._note,'date':self._date,'complaint-by':self._complainer,'status':self._status}

    @property
    def id(self) -> str:
        self._logger.log.info(f'property.getter - id -> {self._id}')
        return self._id

    @property
    def type(self) -> str:
        self._logger.log.info(f'property.getter - type -> {self._type}')
        return self._type

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
        self._id,self._type,self._title:str, self._note:str, self._date:str, self._complainer:str, self._status = value
        self._data = value

    def __rpr__(self):
        return f'report[ {self._data} ]'

    def __str__(self):
         return f'report[ {self._data} ]'