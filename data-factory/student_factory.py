from data.Student import student
from utils.Tools import is_none
from utils.Error import NoneError

class student_factory:
    
    def __init__(self,value: list[student] = list()):
        self._students:list[student]
        self._logger = module_log(log_name = 'student.log',disable_log = False)

    def add_student(self,value: student) -> None:
        if is_none(value): raise NoneError(f'student_factory.py : function add_student')
        self._logger.log.info( f'function add_students <- {value}')
        self._students.append(value)
        self._logger.log.info( f'function add_students : {self._students} <- {value}')

    def remove_student(self,value: student) -> None:
        if is_none(value): raise NoneError(f'student_factory.py : function remove_student')
        self._logger.log.info( f'function remove_students <- {value}')
        self._students.remove(value)
        self._logger.log.info( f'function remove_students : {self._students} -> {value}')

    def find_student(self,id: str) -> None:
        if is_none(id): raise NoneError(f'student_factory.py : function find_teacher')
        for student in self._students:
            if(student.id == id):
                return student
        return None

    def update_student    (self,id: str) -> None:
        if is_none(id): raise NoneError(f'student_factory.py : function update_teacher')
        for student in self._students:
            if(student.id == id):
                student = value