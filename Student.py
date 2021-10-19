from Guardian import guardian
from Teacher import teacher
from Test import test
from Grade import grade

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

    #student id
    @property
    def id(self) -> str:
        return self._id

    # first name
    @property
    def first_name(self) -> str:
        return self._first_name

    # middle name
    @property
    def middle_name(self) -> str:
        return self._middle_name

    # last name
    @property
    def last_name(self) -> str:
        return self._last_name
    
    # address
    @property
    def address(self) -> str:
        return self._address

    #country
    @property
    def country(self) -> str:
        return self._country

    # current level
    @property
    def current_level(self) -> str:
        return self._current_level

    # enrolled
    @property
    def enrolled(self) -> bool:
        return self._enrolled

     # teacher
    @property
    def teacher(self) -> teacher:
        return self._teacher

    # guardian
    @property
    def guardian(self) -> guardian:
        return self._guardian

    # test
    @property
    def test(self) -> test:
        return self._test
    
    #grade
    @property
    def grade(self) -> grade:
        return self._grade

    # student
    @property
    def students(self) -> list:
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

    # define the credential
    def credential(self,value: dict) -> None:
        self._id,self._first_name,self._middle_name,self._last_name,self._address,self._country,self._current_level,self._enrolled = value.values()

    # add student in the student-list
    def add_student(self,value: dict) -> None:
        self._students.append(value)
