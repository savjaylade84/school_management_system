from  utils.Error import NoneError
from utils.Tools import is_none
from dataclasses import dataclass

''' 
        this module has student class that will contain
        all the student information that related to the 
        student information.

        take note course is different in subject data
        course is just master list of all courses available 
        then subject is one of collection(each selected from course)
'''

@dataclass
class student:
    
    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Subject.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_teacher_id = 'subject.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__code:str
        self.__teacher_id:str
        self.__grade:double
        
        #declaration
        self.__code,self.__teacher_id,self.__grade = args
        self.__data:dict = {'code':self.__code,'teacher-id':self.__teacher_id,'grade':self.__grade}

    ##################################[subject properties]#####################################################

    @property
    def code(self) -> str:
        self.__logger.log.info(f'property.getter - code -> {self.__code}')
        return self.__code

    @property
    def teacher_id(self) -> str:
        self.__logger.log.info(f'property.getter - teacher_id -> {self.__teacher_id}')
        return self.__teacher_id   

    @property
    def grade(self) -> double:
        self.__logger.log.info(f'property.getter - grade -> {self.__grade}')
        return self.__grade   

    ##################################[subject information]#####################################################

    @property
    def data(self) -> dict:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Subject.py : property.setter - data')
        self.__code,self.__teacher_id = value
        self.__data = value


    def __rpr__(self):
        return f'subject[ {self.__data} ]'

    def __str__(self):
         return f'subject[ {self.__data} ]'