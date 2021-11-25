from data.Student import student
from data.Teacher import teacher
from data.Subject import subject
from data.Report import report
from data.Guardian import guardian
from data.Grade import grade
from data.Exam import exam
from data.Set import set
from data.Test import test
from data.Course import course

class teacher_manager:
    def __init__(self,teacher_list:list[teacher]):
        self.__teacher_list:list[teacher] = teacher_list
    
    def add(self,new_data:teacher) -> None:
        self.__teacher_list.append(new_data)

    def remove(self,id:str) -> None:
        for teacher in self.__teacher_list
            if(teacher.id == id):
                self.__teacher_list.remove(teacher)

    def update(self,id:str,new_data:teacher) -> None:
        for teacher in self.__teacher_list:
            if(teacher.id == id):
                teacher = new_data

    def find(self,id:str) -> bool:
        for teacher in self.__teacher_list
            if(teacher.id == id):
                return True
        return False

class course_manager:
    def __init__(self,course_list: list[course])
        self.__course_list:list[course] = course_list

    def add(self,new_data:course) -> None:
        self.__course_list.append(new_data)

    def remove(self,code:str) -> None:
        for course in self.__course_list:
            if(course.code == code):
                self.__course_list.remove(course)

    def update(self,code:str,new_data:course) -> None:
        for course in self.__course_list:
            if(course.code == code):
                course == new_data

    def find(self,code:str) -> bool:
        for course in self.__course_list:
            if(course.code == code):
                return True
        return False

class report_manager:

    def __init__(self,report_list: list[report]):
        self.__report_list:list[report] = report_list

    def add(self,new_data: report) -> None:
        self.__report_list.append(new_data)

    def remove(self,id:str,type:str) -> None:
        for report in self.__report_list:
            if(report.id == id and report.type == type):
                self.__report_list.remove(report)
    
    def update(self,id:str,type:str,new_data:report) -> None:
        for report in self.__report_list:
            if(report.id == id and report.type == type):
                report = new_data

    def find(self,id:str,type:str) -> bool:
        for report in self.__report_list:
            if(report.id == id and report.type == type):
                return True
        return False      

class student_manager:

    ##################################[initialising]#####################################################

    def __init__(self,student_list: list[student]):
        self.__student_list:list[student] = student_list

    ##################################[adding]#####################################################

    def add(self,new_data: student) -> None:
        self.__student_list.append(new_data)

    def add_guardian(self,id:str,new_data:guardian) -> None:
        for student in self.__student_list:
            if(student.id == id):
                student.guardians.append(new_data)

    # adding some entity in the grades and subject
    def add_grades(self,id:str,new_data:grade) -> None:
        for student in self.__student_list:
            if(student.id == id):
                student.grades.append(new_data)

    def add_subject(self,id:str,level:str,new_data_subject) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in self.student_list.grades:
                    if(grade.level == level):
                        grade.subjects.append(new_data)

    # adding some entity in the test and exams
    def add_exams(self,id:str,new_data:exam) -> None:
        for student in self.__student_list:
            if(student.id == id):
                student.exams.append(new_data)

    def add_set(self,id:str,set_level:str,new_data:set) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        exam.sets.append(new_data)

    def add_test(self,id:str,set_level:str,set_title,new_data:test) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == set_title):
                                set.tests.append(test)

    ##################################[removing]#####################################################

    def remove_guardian(self,id:str,role:str,name:str) -> None:
        for student in self._student_list:
            if(student.id == id):
                for guardian in student.guardians:
                    if(guardian.name == name and guardian.role == role):
                        student.guardians.remove(guardian)

    # removing some entity in the grades and subject
    def remove_grades(self,id:str,level:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in student.grades:
                    if(grade.level == level):
                        student.grades.remove(grade)

    def remove_subject(self,id:str,level:str,subject_code:str,teacher_id:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in self.student_list.grades:
                    if(grade.level == level):
                        for subject in grade.subjects:
                            if(subject.code == subject_code and subject.teacher_id == teacher_id):
                                grade.subjects.remove(subject)

    # remove some entity in the test and exams
    def remove_exams(self,id:str,level:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for exam in student.exams:
                    if(exam.level == level):
                        student.exams.remove(exam)

    def remove_set(self,id:str,set_level:str,title:str) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == title):
                                exam.sets.remove(set)

    def remove_test(self,id:str,set_level:str,set_title,subject_code:str) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == set_title):
                                for test in set.tests
                                    if(test.subject_code == subject_code):
                                        set.tests.remove(test)

    def remove(self,id:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                self.__student_list.remove(student)

    ##################################[updating]#####################################################

    def update_guardian(self,id:str,role:str,name:str,new_data:guardian) -> None:
        for student in self._student_list:
            if(student.id == id):
                for guardian in student.guardians:
                    if(guardian.name == name and guardian.role == role):
                        guardian = new_data

    # updating some entity in the grades and subject
    def update_grades(self,id:str,level:str,new_data:grade) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in student.grades:
                    if(grade.level == level):
                        grade = new_data

    def update_subject(self,id:str,level:str,subject_code:str,teacher_id:str,new_data:subject) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in self.student_list.grades:
                    if(grade.level == level):
                        for subject in grade.subjects:
                            if(subject.code == subject_code and subject.teacher_id == teacher_id):
                                subject = new_data

    # updating some entity in the test and exams
    def update_exams(self,id:str,level:str,new_data:exam) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for exam in student.exams:
                    if(exam.level == level):
                        exam = new_data

    def update_set(self,id:str,set_level:str,title:str,new_data:set) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == title):
                                set = new_data

    def update_test(self,id:str,set_level:str,set_title,subject_code:str,new_data:test) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == set_title):
                                for test in set.tests
                                    if(test.subject_code == subject_code):
                                        test = new_data

    def update(self,id:str,new_data:student) -> None:
        for student in self.__student_list:
            if(student.id == id):
                student == new_data

    ##################################[finding]#####################################################

    def find(self,id:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                return True
        return False


    def find_guardian(self,id:str,role:str,name:str) -> None:
        for student in self._student_list:
            if(student.id == id):
                for guardian in student.guardians:
                    if(guardian.name == name and guardian.role == role):
                        return True
        return False

    # finding some entity in the grades and subject
    def find_grades(self,id:str,level:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in student.grades:
                    if(grade.level == level):
                        return True
        return False

    def find_subject(self,id:str,level:str,subject_code:str,teacher_id:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for grade in self.student_list.grades:
                    if(grade.level == level):
                        for subject in grade.subjects:
                            if(subject.code == subject_code and subject.teacher_id == teacher_id):
                                return True
        return False

    # finding some entity in the test and exams
    def find_exams(self,id:str,level:str) -> None:
        for student in self.__student_list:
            if(student.id == id):
                for exam in student.exams:
                    if(exam.level == level):
                        return True
        return False

    def find_set(self,id:str,set_level:str,title:str) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == title):
                                return True
        return False

    def find_test(self,id:str,set_level:str,set_title,subject_code:str) -> None:
        for student in self.__student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.sets:
                            if(set.title == set_title):
                                for test in set.tests
                                    if(test.subject_code == subject_code):
                                        return True
        return False

