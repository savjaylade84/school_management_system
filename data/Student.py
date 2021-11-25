from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Guardian import guardian
from data.Test import test
from data.Grade import grade
from data.exam import exam
from dataclasses import dataclass

''' 
        this module has student class that will contain
        all the student information that related to the 
        student information.
'''

@dataclass
class student:

    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Student.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'student.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__id:str
        self.__firt_name:str
        self.__middle_name:str
        self.__last_name:str
        self.__email:str
        self.__contact:str
        self.__address:str
        self.__country:str
        self.__current_level:str
        self.__enrolled:bool
        self.__guardians:list[guardian]
        self.__grades:list[grade]
        self.__exams:list[exam]

        #declaration
        self.__id,self.__firt_name,self.__middle_name,self.__last_name,self.__email,self.__contact,self.__address,self.__country,self.__current_level,self.__enrolled,self.__guardians,self.__exams,self.__grades = args

        self.data:dict = {  'student-id':self.__id,
                            'first-name':self.__firt_name,
                            'middle-name':self.__middle_name,
                            'last-name':self.__last_name,
                            'address':self.__address,
                            'country':self.__country,
                            'current-level':self.__current_level,
                            'email':self.__email,
                            'contact':self.__contact,
                            'enrolled':self.__enrolled,
                            'guardians':self.__guardians,
                            'exam':self.__exam,
                            'grades':self.__grades}

    ##################################[student properties]#####################################################

    @property
    def student_id(self) -> str:
        self.__logger.log.info(f'property.getter - student_id -> {self.__student_id}')
        return self.__student_id

    @property
    def first_name(self) -> str:
        self.__logger.log.info(f'property.getter - first_name -> {self.__firt_name}')
        return self.__first_name

    @property
    def middle_name(self) -> str:
        self.__logger.log.info(f'property.getter - middle_name -> {self.__middle_name}')
        return self.__middle_name

    @property
    def last_name(self) -> str:
        self.__logger.log.info(f'property.getter - last_name -> {self.__last_name}')
        return self.__last_name
        
    @property
    def address(self) -> str:
        self.__logger.log.info(f'property.getter - address -> {self.__address}')
        return self.__address

    @property
    def country(self) -> str:
        self.__logger.log.info(f'property.getter - country -> {self.__country}')
        return self.__country

    @property
    def current_level(self) -> str:
        self.__logger.log.info(f'property.getter - current_level -> {self.__current_level}')
        return self.__current_level

    @property
    def email(self) -> str:
        self.__logger.log.info(f'property.getter - email -> {self.__email}')
        return self.__email

    @property
    def contact_no(self) -> str:
        self.__logger.log.info(f'property.getter - contact_no -> {self.__contact_no}')
        return self.__contact_no

    @property
    def enrolled(self) -> str:
        self.__logger.log.info(f'property.getter - enrolled -> {self.__enrolled}')
        return self.__enrolled

    @property
    def guardians(self) -> str:
        self.__logger.log.info(f'property.getter - guardians -> {self.__guardians}')
        return self.__guardians

    @property
    def exams(self) -> str:
        self.__logger.log.info(f'property.getter - exams -> {self.__exams}')
        return self.__exams
       
    @property
    def grades(self) -> str:
        self.__logger.log.info(f'property.getter - grades -> {self.__grades}')
        return self.__grades

    ##################################[student information]#####################################################

    @property
    def data(self) -> dict:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Student.py : property.setter - data')
        self.__level,self.__title,self.__start_date,self.__end_date,self.__set,self.__total_score = value
        self.__data = value

    def __rpr__(self):
        return f'student[ {self.__data} ]'

    def __str__(self):
         return f'student[ {self.__data} ]'

