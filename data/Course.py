from  utils.Error import NoneError
from utils.Tools import is_none
from dataclasses import dataclass

''' 
        this module has course class that will contain
        all the student information that related to the 
        course information.

        take note course is different in subject data
        course is just master list of all courses available 
        then subject is one of collection(each selected from course)
'''

@dataclass
class course:
    
    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Course.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'course.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__code:str
        self.__name:str
        
        #declaration
        self.__code,self.__name = args
        self.__data:dict = {'code':self.__code,'name':self.__name}

    ##################################[course properties]#####################################################

    @property
    def code(self) -> str:
        self.__logger.log.info(f'property.getter - code -> {self.__code}')
        return self.__code

    @property
    def name(self) -> str:
        self.__logger.log.info(f'property.getter - name -> {self.__name}')
        return self.__name   

    ##################################[course information]#####################################################

    @property
    def data(self) -> dict:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Course.py : property.setter - data')
        self.__code,self.__name = value
        self.__data = value

    
    def __rpr__(self):
        return f'course[ {self.__data} ]'

    def __str__(self):
         return f'course[ {self.__data} ]'