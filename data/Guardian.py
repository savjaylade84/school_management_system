from utils.Error import NoneError
from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none

''' 
        this module has guardian class that will contain
        all the guardian information that related to the 
        student information.
'''

@dataclass
class guardian:

    def __init__(self,*args):
        # create the log
        self._logger:module_log = module_log(log_name = 'guardian.log',disable_log = False)
        # log the creation
        if is_none(args): raise NoneError(f'Guardian.py : function - __init__')
        self._logger.log.debug(f'__init__ <- {args}')
        self._name:str
        self._role:str
        self._contact:str
        self._name, self._role, self._contact = args
        self._data:dict = {'name':self._name, 'contact-no':self._contact, 'role':self._role}

    @property
    def name(self) -> str:
        self._logger.log.info( f'property.getter - name -> {self._name}')
        return self._name

    @property
    def contact(self) -> str:
        self._logger.log.info( f'property.getter - contact -> {self._contact}')
        return self._contact

    @property
    def role(self) -> str:
        self._logger.log.info( f'property.getter - role -> {self._role}')
        return self._role

    @property
    def data(self) -> dict:
        self._logger.log.info( f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Guardian.py : property.setter - data')
        self._name,self._contact,self._role = value
        self._data = value

    def __rpr__(self):
        return f'guardian[{self._data}]'

    def __str__(self):
        return f'guardian[{self._data}]'

