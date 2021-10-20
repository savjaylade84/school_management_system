import Tools
from log import module_log

''' 
        this module has teacher class that will contain
        all the teacher information that related to the 
        student information.
'''

class teacher:

    def __init__(self):
        self._id:str = None
        self._name:str = None
        self._subject:str = None
        self._teachers:list = list()
        self._logger = module_log(log_name = 'teacher.log',disable_log = False)

    @property
    def id(self) -> str:
        self._logger.log.info(message = f'function id -> {self._id}')
        return self._id

    @property
    def name(self) -> str:
        self._logger.log.info(message = f'function name -> {self._name}')
        return self._name

    @property
    def subject(self) -> str:
        self._logger.log.info(message = f'function subject -> {self._subject}')
        return self._subject

    @property
    def teachers(self) -> list:
        self._logger.log.info(message = f'function teachers -> {self._teachers}')
        return self._teachers

    # this will send a teacher information in a dictionary format
    @property
    def full_data(self) -> dict:
        self._logger.log.info(message = 'function full_data -> %s'.format({'subject':self._subject, 'teacher-id':self._id,'name':self._name}))
        return {'subject':self._subject, 'teacher-id':self._id,'name':self._name}

    # initialise a teacher inforamtion in the teacher object
    def define(value: dict) -> None:
        if is_none(value): raise NoneError from Error
        self._logger.log.info(message = f'function define <- {value}')
        self._subject,self._id,self._name = data

    # add a teacher in the teacher list
    def add_teacher(self,value: dict) -> None:
        if is_none(value): raise NoneError from Error
        self._logger.log.info(message = f'function add_teachers <- {value}')
        self._teachers.append(value)
        self._logger.log.info(message = f'function add_teachers : {self._teacher} <- {value}')

    # remove a teacher in the teacher list
    def remove_teacher(self,value: dict) -> None:
        if is_none(value): raise NoneError from Error
        self._logger.log.info(message = f'function remove_teachers <- {value}')
        self._teachers.remove(value)
        self._logger.log.info(message = f'function remove_teachers : {self._teacher} -> {value}')

    ''' 
        this will show object information
    '''

    def __rpr__(self):
        return f'teachers[list = {self._teachers}]'

    def __str__(self):
         return f'teachers[list = {self._teachers}]'


