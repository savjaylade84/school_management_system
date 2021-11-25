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

    ##################################[initialising]#####################################################
     def __init__(self,*args):
        
        if is_none(args): raise NoneError(f'Teacher.py : function - __init__')

        # create the log 
        self.__logger:module_log = module_log(log_name = 'teacher.log',disable_log = False)
        # log the creation
        self.__logger.log.debug(f'__init__ <- {args}')

        #initialize   
        self.__id:str
        self.__firt_name:str
        self.__middle_name:str
        self.__last_name:str
        self.__email:str
        self.__contact:str
        self.__address:str
        self.country:str

        #declare
        self.__id,self.__first_name,self.__middle_name,self.__last_name,self.__email,self.__contact,self.address,self.coutry = args
        self.__data:dict = { 'teacher-id':self.__id,
                            'first-name':self.__first_name,
                            'middle-name':self.__middle_name,
                            'last-name':self.__last_name,
                            'email':self.__email,
                            'contact-no':self.__contact,
                            'address':self.address,
                            'country':self.coutry}

    ##################################[teacher properties]#####################################################

    @property
    def id(self) -> str:
        self.__logger.log.info( f'property.getter - id -> {self.__id}')
        return self.__id

    @property
    def first_name(self) -> str:
        self.__logger.log.info( f'property.getter - first_name -> {self.__first_name}')
        return self.__first_name

    @property
    def middle_name(self) -> str:
        self.__logger.log.info( f'property.getter - middle_name -> {self.__middle_name}')
        return self.__middle_name

    @property
    def last_name(self) -> str:
        self.__logger.log.info( f'property.getter - last_name -> {self.__last_name}')
        return self.__last_name

    @property
    def email(self) -> str:
        self.__logger.log.info( f'property.getter - email -> {self.__email}')
        return self.__email

    @property
    def contact_no(self) -> str:
        self.__logger.log.info( f'property.getter - contact_no -> {self.__contact_no}')
        return self.__contact_no

    @property
    def address(self) -> str:
        self.__logger.log.info( f'property.getter - address -> {self.__address}')
        return self.__address

    @property
    def country(self) -> str:
        self.__logger.log.info( f'property.getter - country -> {self.__country}')
        return self.__country

    ##################################[teacher information]#####################################################

    @property
    def data(self) -> dict:
        self.__logger.log.info(f'property.getter - data -> {self.__data}')
        return self.__data

    @data.setter
    def data(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'Teacher.py : property.setter - data')
        self.__id,self.__first_name,self.__middle_name,self.__last_name,self.__email,self.__contact,self.address,self.coutry = value
        self.__data = value

    def __rpr__(self):
        return f'teacher[ {self.__data} ]'

    def __str__(self):
         return f'teacher[ {self.__data} ]'



