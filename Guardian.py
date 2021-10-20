import Tools
from log import module_log


''' 
        this module has guardian class that will contain
        all the guardian information that related to the 
        student information.
'''

class guardian:

    def __init__(self):
        self._name:str = None
        self._role:str = None
        self._contact:str = None
        self._guardians:list = list()
        self._logger = module_log(log_name = 'guardian.log',disable_log = False)

    @property
    def name(self) -> str:
        self._logger.log.info(message = f'function name -> {self._name}')
        return self._name

    @property
    def contact(self) -> str:
        self._logger.log.info(message = f'function contact -> {self._contact}')
        return self._contact

    @property
    def role(self) -> str:
        self._logger.log.info(message = f'function role -> {self._role}')
        return self._role

    @property
    def guardians(self) -> list:
        self._logger.log.info(message = f'function guardians -> {self._guardians}')
        return self._guardians

    @property
    def full_data(self) -> dict:
        self._logger.log.info(message = 'function full_data -> {0}'.format({'name':self._name,'contact-no':self._contact,'role':self._role}))
        return {'name':self._name,'contact-no':self._contact,'role':self._role}

    def define(value: dict) -> None:
        if is_none(value): raise NoneError from Error
        self._logger.log.info(message = f'function define <- {value}')
        self._name,self._contact,self._role = value

    def add_guardian(self,guardian: dict) -> None:
        if is_none(guardian): raise NoneError from Error
        self._logger.log.info(message = f'function add_guardians <- {guardian}')
        self._guardians.append(guardian)
        self._logger.log.info(message = f'function add_guardians : {self._guardians} <- {guardian}')

    def remove_guardian(self,guardian: dict) -> None:
        if is_none(guardian): raise NoneError from Error
        self._logger.log.info(message = f'function remove_guardians <- {guardian}')
        self._guardians.remove(guardian)
        self._logger.log.info(message = f'function remove_guardians : {self._guardians} -> {guardian}')

    def __rpr__(self):
        return f'guardian[name = {self._name},role = {self._role},contact = {self._contact}]'

    def __str__(self):
        return f'guardian[name = {self._name},role = {self._role},contact = {self._contact}]'

