from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from data.Guardian import guardian
from data.Test import test
from data.Grade import grade
from data.Set import set
from dataclasses import dataclass

''' 
        this module has student class that will contain
        all the student information that related to the 
        student information.
'''

@dataclass
class student:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'student.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')

        self._id:str
        self._firt_name:str
        self._middle_name:str
        self._last_name:str
        self._email:str
        self._contact:str
        self._address:str
        self.country:str
        self._current_level:str
        self._enrolled:bool
        self._guardians:list[guardian]
        self._grades:list[grade]
        self._exams:list[set]

        self._id,self._firt_name,self._middle_name,self._last_name,self._email,self._contact,self._address,self.country,self._current_level,self._enrolled,self._guardians,self._exams,self._grades = args

        self.data:dict = {  'student-id':self._id,
                            'first-name':self._firt_name,
                            'middle-name':self._middle_name,
                            'last-name':self._last_name,
                            'address':self._address,
                            'country':self.country,
                            'current-level':self._current_level,
                            'email':self._email,
                            'contact':self._contact,
                            'enrolled':self._enrolled,
                            'guardians':self._guardians,
                            'exam':self._exam,
                            'grades':self._grades}

    @property
    def student_id(self) -> str:
        self._logger.log.info(f'property.getter - student_id -> {self._student_id}')
        return self._student_id

    @property
    def first_name(self) -> str:
        self._logger.log.info(f'property.getter - first_name -> {self._firt_name}')
        return self._first_name

    @property
    def middle_name(self) -> str:
        self._logger.log.info(f'property.getter - middle_name -> {self._middle_name}')
        return self._middle_name

    @property
    def last_name(self) -> str:
        self._logger.log.info(f'property.getter - last_name -> {self._last_name}')
        return self._last_name
        
    @property
    def address(self) -> str:
        self._logger.log.info(f'property.getter - address -> {self._address}')
        return self._address

    @property
    def country(self) -> str:
        self._logger.log.info(f'property.getter - country -> {self._country}')
        return self._country

    @property
    def current_level(self) -> str:
        self._logger.log.info(f'property.getter - current_level -> {self._current_level}')
        return self._current_level

    @property
    def email(self) -> str:
        self._logger.log.info(f'property.getter - email -> {self._email}')
        return self._email

    @property
    def contact_no(self) -> str:
        self._logger.log.info(f'property.getter - contact_no -> {self._contact_no}')
        return self._contact_no

    @property
    def enrolled(self) -> str:
        self._logger.log.info(f'property.getter - enrolled -> {self._enrolled}')
        return self._enrolled

    @property
    def guardians(self) -> str:
        self._logger.log.info(f'property.getter - guardians -> {self._guardians}')
        return self._guardians

    @property
    def exams(self) -> str:
        self._logger.log.info(f'property.getter - exams -> {self._exams}')
        return self._exams
       
    @property
    def grades(self) -> str:
        self._logger.log.info(f'property.getter - grades -> {self._grades}')
        return self._grades


    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value:dict) -> None:
        if is_none(value): raise NoneError(f'Student.py : property.setter - data')
        self._level,self._title,self._start_date,self._end_date,self._set,self._total_score = value
        self._data = value

    def __rpr__(self):
        return f'teachers[ {self._data} ]'

    def __str__(self):
         return f'teachers[ {self._data} ]'

