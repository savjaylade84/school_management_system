import json
import Tools
import Error
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
        if is_none(id): raise NoneError('student_manager -> function find_credential: None Value has been pass')
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

    # find the set of grades data
    def find_test(self,id: str,level: str,test: str) -> dict:
        if is_none(id,level,test): raise NoneError('student_manager -> function find_test: None Value has been pass')
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for _test in student['grades'][level]:
                    if _test['set-test'] == test:
                        return True
        return False

    # find the specific grade data in the set of grades
    def find_grade(self,id: str,level: str,test: str,type: str,subject: str) -> bool:
        if is_none(id,level,test,type,subject): raise NoneError('student_manager -> function find_grade: None Value has been pass')
        for student in self._student_json['students']:
            if(student['student-id'] == id):
                for grade in student['grades'][level][test][type]:
                    if subject == None: return None
                    if grade['subject'] == subject:
                        return True
        return False
    
    # find the specific guardian data in the list of guardian
    def find_guardian(self,id: str,role: str) -> bool:
        if is_none(id,role): raise NoneError('student_manager -> function find_guardian: None Value has been pass')
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
        if is_none(student): raise NoneError('student_manager -> function add_student: None Value has been pass')
        self._student.students.add_student(value student.full_data)

    # add guardian in the list
    def add_guardian(self,guardian: guardian) -> None:
        if is_none(guardian): raise NoneError('student_manager -> function add_guardian: None Value has been pass')
        self._student.guardian.add_guardian(value = guardian.full_data)

    # add grade in the list
    def add_grade(self,grade: grade) -> None:
        if is_none(grade): raise NoneError('student_manager -> function add_grade: None Value has been pass')
        self._student.set_test.add_grade(value = grade.full_data)

    # add set test in the list
    def add_set_test(self,test: test) -> None:
        if is_none(grade): raise NoneError('student_manager -> function add_set_test: None Value has been pass')
        self._student.set_test.add_set_test(value = test.full_data)

    # update student
    def update_student(self,data: student,id: str) -> None:
        if is_none(data,id): raise NoneError('student_manager -> function update_student: None Value has been pass')
        for student in self._student.students:
            if(student.id == id):
                student = data.full_data

    # update guardian
    def update_guardian(self,data: guardian,name: str,role: str) -> None:
        if is_none(data,name,role): raise NoneError('student_manager -> function update_guardian: None Value has been pass')
        for guardian in self._student.guardian.guardians:
            if(guardian.name == name and guardian.role == role):
                guardian = data.full_data
            
    # update grade
    def update_grade(self,data: grade,subject: str) -> None:
        if is_none(data,name,role): raise NoneError('student_manager -> function update_grade: None Value has been pass')
        for grade in self._student.test.grades:
            if(grade.subject == subject):
                grade = data.full_data

    #underconstruction
    def update_set_test(self,data: test,grades_name: str) -> None:
        if is_none(data,name,role): raise NoneError('student_manager -> function update_set_test: None Value has been pass')
        for set_test in self._student.test.set_tests:
            if(set_test.grades_name == grades_name):
                

    # remove student
    def remove_student(self,value:dict) -> None:
        if is_none(value):raise NoneError('student_manager -> function remove_student: None Value has been pass')
        self._student.remove_student(value)

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

