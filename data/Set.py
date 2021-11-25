from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Test import test

''' 
        this module has test class that will contain
        all the test information that related to the 
        student information.
'''

@dataclass
class set:

    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Set.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'set.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__title:str = None
        self.__tests:list[test] = list()
        self.__start_date:str
        self.__end_date:str
        self.__total_score:int

        #declaration
        self.__title,self.__start_date,self.__end_date,self.__tests,self.__total_score = args
        self.__data:dict = {'title':self.__title,'start-date':self.__start_date,'end-date':self.__end_date, 'tests':self.__tests, 'total-score':self.__total_score}

    ##################################[set properties]#####################################################

    @property
    def title(self) -> str:
        self.__logger.log.info(f'property.getter - title -> {self.__title}')
        return self.__title

    @property
    def tests(self) -> list:
        self.__logger.log.info(f'property.getter - tests -> {self.__tests}')
        return self.__tests

    @property
    def start_date(self) -> str:
        self.__logger.log.info(f'property.getter - start_date -> {self.__start_date}')
        return self.__start_date

    @property
    def end_date(self) -> str:
        self.__logger.log.info(f'property.getter - end_date -> {self.__end_date}')
        return self.__end_date

    @property
    def total_score(self) -> int:
        self.__logger.log.info(f'property.getter - total_score -> {self.__total_score}')
        return self.__total_score

    ##################################[set information]#####################################################

    @property
    def data(self) -> dict:
        self.__logger.log.info(f'property.getter - full_data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Set.py : property.setter - data')
        self.__title,self.__start_date,self.__end_date,self.__tests,self.__total_score = value
        self.__data = value

    def __rpr__(self):
        return f'set[ {self.__data} ]'

    def __str__(self):
        return f'set[ {self.__data} ]'

       
