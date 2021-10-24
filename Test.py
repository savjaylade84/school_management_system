import Tools
from Grade import grade
from log import module_logs

''' 
        this module has test class that will contain
        all the test information that related to the 
        student information.
'''

class test:

    def __init__(self):
        self._set_name:str = None
        self._set_tests:list = list()
        self._grades:list = list()
        self._grades_name:str = None
        self._logger = module_log(log_name = 'test.log',disable_log = False)

    @property
    def set_name(self) -> str:
        self._logger.log.info(f'function set_name -> {self._set_name}')
        return self._set_name

    @property
    def grades_name(self) -> str:
        self._logger.log.info(f'function grades_name -> {self._grades_name}')
        return self._grades_name

    @property
    def grades(self) -> list:
        self._logger.log.info(f'function grades -> {self._grades}')
        return self._grades

    @property
    def set_tests(self) -> list:
        self._logger.log.info(f'function grades -> {self._set_tests}')
        return self._set_tests
    
    @property
    def full_data(self) -> dict:
        self._logger.log.info('function full_data -> {0}'.format({'set-test':self._set_name,self._grades_name:self._grades}))
        return {'set-test':self._set_name,self._grades_name:self._grades}

    def add_grade(self,value: grade) -> None:
        if is_none(value): raise NoneError from Error
        self._logger.log.info(f'function add_grade <- {value}')
        self._grades.append(value.full_data)

    def add_set_test(self,value: dict) -> None:
        if is_none(test):raise NoneError from Error
        self._logger.log.info(f'function add_set_test <- {test}')
        self._set_tests.append(test)

    def define(self,set_name: str,grades: list) -> None:
        if is_none(set_name,grades):raise NoneError from Error
        self._logger.log.info(f'function define <- {set_name}:{grades}')
        self._set_name = set_name
        self._grades = grades

    def remove_grade(self,value: dict) -> None:
        if is_none(value):raise NoneError from Error
        self._logger.log.info(f'function remove_grade <- {value}')
        self._grades.remove(value)
        self._logger.log.info(f'function remove_grade:{self._grades} -> {value}')

    def remove_set_test(self,value: dict) -> None:
        if is_none(value):raise NoneError from Error
        self._logger.log.info(f'function remove_set_test <- {value}')
        self._grades.remove(value)
        self._logger.log.info.(f'function remove_set_test : {self._set_tests} -> {value}')

    def __rpr__(self):
        return f'test[set_test = {self._set_name},grades = {self._grades}]'

    def __str__(self):
        return f'test[set_test = {self._set_name},grades = {self._grades}]'

       
