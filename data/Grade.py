from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Student import student

@dataclass
class subject:
    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Grade.py : function - __init__')
            
        # create the log 
        self.__logger:module_log = module_log(log_name = 'grade.log',disable_log = False)
        # log the creation

        #initialize
        self.__logger.log.debug(f'__init__ <- {args}')
        self.__level:str
        self.__start_date:str
        self.__end_date:str
        self.__subjects:list[subject]

        #declaration
        self.__level,self.__start_date, self.__end_date, self.__subjects = args
        self.__data = ('level':self.__level,'start-date':self.__start_date,'end-date':self.__date,'subjects:':self.__subjects)

    ##################################[grade properties]#####################################################

    @property
    def level(self) -> str:
        self.__logger.log.info(f'property.getter - level -> {self.__level}')
        return self.__level

    @property
    def start_date(self) -> str:
        self.__logger.log.info(f'property.getter - start_date -> {self.__start_date}')
        return self.__start_date

    @property
    def end_date(self) -> str:
        self.__logger.log.info(f'property.getter - end_date -> {self.__end_date}')
        return self.__end_date

    @property
    def subjects(self) -> int:
        self.__logger.log.info(f'property.getter - subjects -> {self.__subjects}')
        return self.__subjects

    ##################################[grade information]#####################################################

     @property
    def data(self) -> str:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Grade.py : property.setter - data')
        self.__level,self.__start_date, self.__end_date, self.__subjects = value
        self.__data = value

    def __rpr__(self):
        return f'subject[ {self.__data} ]'

    def __str__(self):
         return f'subject[ {self.__data} ]'

