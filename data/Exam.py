from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Set import set

class exam:

    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Exam.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'exam.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__level:str
        self.__sets:list[set] = list()
        
        #declaration
        self.__level,self.__sets = args
        self.__data:dict = {'level':self.__level,'sets':self.__sets}

    ##################################[exam properties]#####################################################

    @property
    def level(self) -> str:
        self.__logger.log.info(f'property.getter - level -> {self.__level}')
        return self.__level

    @property
    def sets(self) -> list:
        self.__logger.log.info(f'property.getter - sets -> {self.__sets}')
        return self.__sets

    ##################################[exam information]#####################################################

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'exam.py : property.setter - data')
        self.__level,self.__sets = value
        self.__data = value

    def __rpr__(self):
        return f'exam[ {self.__data} ]'

    def __str__(self):
        return f'exam[ {self.__data} ]'
