import Error
import Tools
from Teacher import teacher


class teacher_factory:
    
    def __init__(self,value:list[teacher] = list()):
        self._teachers:list[teacher] = value
        self._logger = module_log(log_name = 'teacher.log',disable_log = False)

    # add a teacher in the teacher list
    def add_teacher(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'teacher_factory.py : function add_teacher')
        self._logger.log.info(message = f'function add_teachers <- {value}')
        self._teachers.append(value)
        self._logger.log.info(message = f'function add_teachers : {self._teacher} <- {value}')

    # remove a teacher in the teacher list
    def remove_teacher(self,value: dict) -> None:
        if is_none(value): raise NoneError(f'teacher_factory.py : function remove_teacher')
        self._logger.log.info(message = f'function remove_teachers <- {value}')
        self._teachers.remove(value)
        self._logger.log.info(message = f'function remove_teachers : {self._teacher} -> {value}')

    # find a teacher and return it
    def find_teacher(self,teacher_id:str) -> teacher:
        if is_none(teacher_id): raise NoneError(f'teacher_factory.py : function find_teacher')
        self._logger.log.info(message = f'function find_teachers <- {teacher_id}')
        for teacher in teachers:
            if(teacher.id == teacher_id):
                return teacher
        return None

    # update a teacher and return it
    def update_teacher(setl,value: teacher,teacher_id: str) -> None:
        if is_none(value,teacher_id): raise NoneError(f'teacher_factory.py : function update_teacher')
        for teacher in teachers:
            if(teacher.id == teacher_id):
                teacher = value

        
