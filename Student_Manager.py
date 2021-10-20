import json
import Tools
from Student import student
from Grade import grade
from Teacher import teacher
from Guardian import guardian
from Test import test

class student_manager:

    def __init__(self,path: str,student_obj: student = None):
        self._path:str = path
        self._student_list:dict = dict({'students':list()})
        self._student:student = self.__init(student_obj)
        # get the json file before using the student manager class
        with open(self._path) as file:
            self._student_json = json.load(file)

    ''' 
        initialize  the student object depending on 
        the pass argument in the constructor if the 
        pass argument then new student object will implemented
        otherwise the pass argument will be use.
    '''
    def __init(self,obj: student) -> student:
        if is_none(obj): return student()
        return obj

    # find the credential data
    def find_credential(self,id: str) -> bool:
        if is_none(id): raise NoneError from Error
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                self._student.define(value = {
                                'student-id':student['student-id'],
                                'first-name':student['first-name'],
                                'middle-name':student['middle-name'],
                                'last-name':student['last-name'],
                                'address':student['address'],
                                'country':student['country'],
                                'school-level':student['current-level'],
                                'enrolled':student['enrolled']
                            })
                return True
        return False

    #  find the specific teacher data
    def find_teacher(self,id: str,level: str,subject: str) -> bool:
        if is_none(id,level,subject): raise NoneError from Error
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for teacher in student['teachers'][level]:
                    if teacher['subject'] == subject:
                        self._student.teacher.define(value = teacher)
                return True
        return False
    
    # find the set of grades data
    def find_test(self,id: str,level: str,test: str) -> dict:
        if is_none(id,level,test): raise NoneError from Error
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for _test in student['grades'][level]:
                    if _test['set-test'] == test:
                        return True
        return False

    # find the specific grade data in the set of grades
    def find_grade(self,id: str,level: str,test: str,type: str,subject: str) -> bool:
        if is_none(id,level,test,type,subject): raise NoneError from Error
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for grade in student['grades'][level][test][type]:
                    if subject == None: return None
                    if grade['subject'] == subject:
                        return True
        return False
    
    # find the specific guardian data in the list of guardian
    def find_guardian(self,id: str,role: str) -> bool:
        if is_none(id,role): raise NoneError from Error
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for guardian in student['guardians']:
                    if guardian['role'] == role:
                        return True
        return False

    # send all the raw data of the student
    def get_student_all(self) -> dict:
        return self._student_json['students']

    # add student in the list
    def add_student(self,student: student) -> None:
        if is_none(student): raise NoneError from Error
        self._student.students.add_student(value student.full_data)

    # add teacher in the list
    def add_teacher(self,teacher: teacher) -> None:
        if is_none(teacher): raise NoneError from Error
        self._student.teacher.add_teacher(value = teacher.full_data)

    # add guardian in the list
    def add_guardian(self,guardian: guardian) -> None:
        if is_none(guardian): raise NoneError from Error
        self._student.guardian.add_guardian(value = guardian.full_data)

    # add grade in the list
    def add_grade(self,grade: grade) -> None:
        if is_none(grade): raise NoneError from Error
        self._student.set_test.add_grade(value = grade.full_data)

    # add set test in the list
    def add_set_test(self,test: test) -> None:
        if is_none(grade): raise NoneError from Error
        self._student.set_test.add_set_test(value = test.full_data)

    # update student
    def update_student(self,data: student,id: str) -> None:
        if is_none(data,id): raise NoneError from Error
        for student in self._student.students:
            if(student.id == id):
                student = data.full_data

    # update teacher
    def update_teacher(self,data: teacher,id: str) -> None:
        if is_none(data,id): raise NoneError from Error
        for teacher in self._student.teacher.teachers:
            if(teacher.id == id):
                teacher = data.full_data 

    # update guardian
    def update_guardian(self,data: guardian,name: str,role: str) -> None:
        if is_none(data,name,role): raise NoneError from Error
        for guardian in self._student.guardian.guardians:
            if(guardian.name == name and guardian.role == role):
                guardian = data.full_data



    # save the data in the json file
    def save_data(self) -> bool:

        with open(self._path,'w') as file:
            '''
                transform to a json format and write the whole thing in 
                a json file
            '''
            json.dump(self._student_list,file,indent=2)
            return True
        return False

