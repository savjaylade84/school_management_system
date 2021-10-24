import Tools
from log import module_log


''' 
        this module has guardian class that will contain
        all the guardian information that related to the 
        student information.
'''
@dataclass
class guardian:

    def __init__(self,args*):
        self._name:str, self._role:str, self._contact:str = args
        self.data:dict = {'name':self._name:str, 'contact-no':self._contact:str, 'role':self._role:str}
        self._logger:module_log = module_log(log_name = 'guardian.log',disable_log = False)

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
    def data(self) -> dict:
        self._logger.log.info(message = f'property - data -> {self._data}')
        return self._data

    @property.setter
    def data(self,value: guardian) -> None:
        if is_none(value): raise NoneError(f'Guardian.py : property.setter - data')
        self._name,self._contact,self._role = value.data
        self._data = value.data

    def __rpr__(self):
        return f'guardian[name = {self._name},role = {self._role},contact = {self._contact}]'

    def __str__(self):
        return f'guardian[name = {self._name},role = {self._role},contact = {self._contact}]'

