from logs.log import module_log
from dataclasses import dataclass
from utils.Tools import is_none
from utils.Error import NoneError

''' 
        this module has teacher class that will contain
        all the teacher information that related to the 
        student information.
'''

@dataclass
class teacher:

    def __init__(self,*args):
        # create the log 
        self._logger:module_log = module_log(log_name = 'teacher.log',disable_log = False)
        # log the creation
        self._logger.log.debug(f'__init__ <- {args}')
        if is_none(args): raise NoneError(f'Teacher.py : function - __init__')

        #declare object variable and there types    
        self._id:str
        self._firt_name:str
        self._middle_name:str
        self._last_name:str
        self._email:str
        self._contact:str
        self._address:str
        self.country:str

        #initialize object variable
        self._id,self._first_name,self._middle_name,self._last_name,self._email,self._contact,self.address,self.coutry = args
        self._data:dict = { 'teacher-id':self._id,
                            'first-name':self._first_name,
                            'middle-name':self._middle_name,
                            'last-name':self._last_name,
                            'email':self._email,
                            'contact-no':self._contact,
                            'address':self.address,
                            'country':self.coutry}

    @property
    def id(self) -> str:
        self._logger.log.info( f'property.getter - id -> {self._id}')
        return self._id

    @property
    def first_name(self) -> str:
        self._logger.log.info( f'property.getter - first_name -> {self._first_name}')
        return self._first_name

    @property
    def middle_name(self) -> str:
        self._logger.log.info( f'property.getter - middle_name -> {self._middle_name}')
        return self._middle_name

    @property
    def last_name(self) -> str:
        self._logger.log.info( f'property.getter - last_name -> {self._last_name}')
        return self._last_name

    @property
    def email(self) -> str:
        self._logger.log.info( f'property.getter - email -> {self._email}')
        return self._email

    @property
    def contact_no(self) -> str:
        self._logger.log.info( f'property.getter - contact_no -> {self._contact_no}')
        return self._contact_no

    @property
    def address(self) -> str:
        self._logger.log.info( f'property.getter - address -> {self._address}')
        return self._address

    @property
    def country(self) -> str:
        self._logger.log.info( f'property.getter - country -> {self._country}')
        return self._country

    @property
    def data(self) -> dict:
        self._logger.log.info(f'property.getter - data -> {self._data}')
        return self._data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Teacher.py : property.setter - data')
        self._id,self._first_name,self._middle_name,self._last_name,self._email,self._contact,self.address,self.coutry = value
        self._data = value

    def __rpr__(self):
        return f'teacher[ {self._data} ]'

    def __str__(self):
         return f'teacher[ {self._data} ]'



