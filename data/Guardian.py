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

    ##################################[initialising]#####################################################
    def __init__(self,*args):

        if is_none(args): raise NoneError(f'Guardian.py : function - __init__')

        # create the log
        self.__logger:module_log = module_log(log_name = 'guardian.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize
        self.__name:str
        self.__role:str
        self.__contact:str

        #declaration
        self.__name, self.__role, self.__contact = args
        self.__data:dict = {'name':self.__name, 'contact-no':self.__contact, 'role':self.__role}

    ##################################[guardian properties]#####################################################

    @property
    def name(self) -> str:
        self.__logger.log.info( f'property.getter - name -> {self.__name}')
        return self.__name

    @property
    def contact(self) -> str:
        self.__logger.log.info( f'property.getter - contact -> {self.__contact}')
        return self.__contact

    @property
    def role(self) -> str:
        self.__logger.log.info( f'property.getter - role -> {self.__role}')
        return self.__role

    ##################################[guardian information]#####################################################
    @property
    def data(self) -> dict:
        self.__logger.log.info( f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Guardian.py : property.setter - data')
        self.__name,self.__contact,self.__role = value
        self.__data = value

    def __rpr__(self):
        return f'guardian[ {self.__data} ]'

    def __str__(self):
        return f'guardian[ {self.__data} ]'

