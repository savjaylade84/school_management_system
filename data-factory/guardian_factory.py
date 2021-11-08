from data.Guardian import guardian
from utils.Tools import is_none
from utils.Error import NoneError

class guardian_factory:
    
    def __init__(self,value: list[guardian] = list()):
        self._guardians:list[guardian]
        self._logger = module_log(log_name = 'guardian.log',disable_log = False)

    def add_guardian(self,value: guardian) -> None:
        if is_none(value): raise NoneError(f'guardian_factory.py : function add_guardian')
        self._logger.log.info( f'function add_guardians <- {value}')
        self._guardians.append(value)
        self._logger.log.info( f'function add_guardians : {self._guardians} <- {value}')

    def remove_guardian(self,value: guardian) -> None:
        if is_none(value): raise NoneError(f'guardian_factory.py : function remove_guardian')
        self._logger.log.info( f'function remove_guardians <- {value}')
        self._guardians.remove(value)
        self._logger.log.info( f'function remove_guardians : {self._guardians} -> {value}')

    def find_guardian(self,name: str, role: str) -> None:
        if is_none(name,role): raise NoneError(f'guardian_factory.py : function find_teacher')
        for guardian in self._guardians:
            if(guardian.name == name and guardian.role == role):
                return guardian
        return None

    def update_guardin(self,value: guardian,name: str,role: str) -> None:
        if is_none(value,name,role): raise NoneError(f'guardian_factory.py : function update_teacher')
        for guardian in self._guardians:
            if(guardian.name == name and guardian.role == role):
                guardian = value
