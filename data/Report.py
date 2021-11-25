from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none

@dataclass
class report:

    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Report.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'report.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__id:str
        self.__type:str
        self.__title:str
        self.__note:str
        self.__date:str
        self.__complainer:str
        self.__status:str

        #declaration
        self.__id,self.__type,self.__title:str, self.__note:str, self.__date:str, self.__complainer:str, self.__status = args
        self.__data = {'student-id':self.__id,'type':self.__type,'title':self.__title,'note':self.__note,'date':self.__date,'complaint-by':self.__complainer,'status':self.__status}

    ##################################[report properties]#####################################################

    @property
    def id(self) -> str:
        self.__logger.log.info(f'property.getter - id -> {self.__id}')
        return self.__id

    @property
    def type(self) -> str:
        self.__logger.log.info(f'property.getter - type -> {self.__type}')
        return self.__type

    @property
    def title(self) -> str:
        self.__logger.log.info(f'property.getter - title -> {self.__title}')
        return self.__title

    @property
    def note(self) -> str:
        self.__logger.log.info(f'property.getter - note -> {self.__note}')
        return self.__note

    @property
    def date(self) -> str:
        self.__logger.log.info(f'property.getter - title -> {self.__date}')
        return self.__date

    @property
    def complainer(self) -> str:
        self.__logger.log.info(f'property.getter - complainer -> {self.__complainer}')
        return self.__complainer

    @property
    def status(self) -> str:
        self.__logger.log.info(f'property.getter - status -> {self.__status}')
        return self.__status

    ##################################[report information]#####################################################

    @property
    def data(self) -> str:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Report.py : property.setter - data')
        self.__id,self.__type,self.__title:str, self.__note:str, self.__date:str, self.__complainer:str, self.__status = value
        self.__data = value

    def __rpr__(self):
        return f'report[ {self.__data} ]'

    def __str__(self):
         return f'report[ {self.__data} ]'