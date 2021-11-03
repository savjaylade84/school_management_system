from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from Guardian import guardian
from Teacher import teacher
from Test import test
from Grade import grade

''' 
        this module has student class that will contain
        all the student information that related to the 
        student information.
'''

class student:

    def __init__(self):
        self._id:str = None
        self._first_name:str = None
        self._middle_name:str = None
        self._last_name:str = None
        self._address:str = None
        self._country:str = None
        self._current_level:str = None
        self._enrolled:bool = None
        self._test:test = test()
        self._guardian:guardian = guardian()
        self._teacher:teacher = teacher()
        self._grade:grade = grade()
        self._students:list = list()
        self._logger = module_log(log_name = 'student.log',disable_log = False)

    #student id
    @property
    def id(self) -> str:
        self._logger.log.info(f'function id -> {self._id}')
        return self._id

    # first name
    @property
    def first_name(self) -> str:
        self._logger.log.info(f'function first_name -> {self._first_name}')
        return self._first_name

    # middle name
    @property
    def middle_name(self) -> str:
        self._logger.log.info(f'function middle_name -> {self._middle_name}')
        return self._middle_name

    # last name
    @property
    def last_name(self) -> str:
        self._logger.log.info(f'function last_name -> {self._last_name}')
        return self._last_name
    
    # address
    @property
    def address(self) -> str:
        self._logger.log.info(f'function address -> {self._address}')
        return self._address

    #country
    @property
    def country(self) -> str:
        self._logger.log.info(f'function country -> {self._country}')
        return self._country

    # current level
    @property
    def current_level(self) -> str:
        self._logger.log.info(f'function current_level -> {self._current_level}')
        return self._current_level

    # enrolled
    @property
    def enrolled(self) -> bool:
        self._logger.log.info(f'function enrolled -> {self._enrolled}')
        return self._enrolled

     # teacher
    @property
    def teacher(self) -> teacher:
        self._logger.log.info(f'function teacher -> {self._teacher}')
        return self._teacher

    # guardian
    @property
    def guardian(self) -> guardian:
        self._logger.log.info(f'function guardian -> {self._guardian}')
        return self._guardian

    # test
    @property
    def test(self) -> test:
        self._logger.log.info(f'function test -> {self._test}')
        return self._test
    
    #grade
    @property
    def grade(self) -> grade:
        self._logger.log.info(f'function grade -> {self._grade}')
        return self._grade

    # student
    @property
    def students(self) -> list:
        self._logger.log.info(f'function student -> {self._student}')
        return self._students

    # give the whole raw data of student
    @property
    def full_data(self) -> dict:
        return {
            'student-id':self._id,
            'first-name' : self._first_name,
            'middle-name' : self._middle_name,
            'last-name' : self._last_name,
            'address' : self._address,
            'country' : self._country,
            'current-level' : self._current_level,
            'enrolled' : self._enrolled,
            'guardians' : self._guardians,
            'teachers' : self._teachers,
            'grades' : self._test.grades
        }

    # define the student information
    def define(self,value: dict) -> None:
        if is_none(value):raise NoneError from Error
        self._logger.log.info(f'function credential <- {value}')
        self._id,self._first_name,self._middle_name,self._last_name,self._address,self._country,self._current_level,self._enrolled = value.values()

    # add student in the student-list
    def add_student(self,value: dict) -> None:
        if is_none(value):raise NoneError from Error
        self._logger.log.info(f'function add_student <- {value}')
        self._students.append(value)

    # remove student in the student-list
    def remove_student(self,value: dict) -> None:
        if is_none(value):raise NoneError from Error
        self._logger.log.info(f'function remove_student <- {value}')
        self._students.remove(value)
        self._logger.log.info(f'function add_student : {self._student} -> {value}')

    
    def __repr__(self):
       return f'''student[
            student-id:{self._id},
            first-name = {self._first_name},
            middle-name = {self._middle_name},
            last-name = {self._last_name},
            address = {self._address},
            country = {self._country},
            current-level = {self._current_level},
            enrolled = {self._enrolled},
            test = {self._test},
            teacher = {self._teacher},
            guardian = {self._guardian}
        ]'''

    def __str__(self):
        return f'''student[
            student-id:{self._id},
            first-name = {self.first_name},
            middle-name = {self._middle_name},
            last-name = {self._last_name},
            address = {self._address},
            country = {self._country},
            current-level = {self._current_level},
            enrolled = {self._enrolled},
            test = {self._test},
            teacher = {self._teacher.full_data},
            guardian = {self._guardian.full_data}
        ]'''
