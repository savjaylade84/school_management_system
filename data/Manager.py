from data.Student import student
from data.Teacher import teacher
from data.Subject import subject
from data.Report import report
from data.Guardian import guardian
from data.Grade import grade
from data.Exam import exam
from data.Set import set
from data.Test import test

class teacher_manager:
    def __init__(self,teacher_list:list[teacher]):
        self._teacher_list:list[teacher] = teacher_list
    
    def add(self,new_data:teacher):
        self._teacher_list.append(new_data)

    def remove(self,id:str):
        for teacher in self._teacher_list
            if(teacher.id == id):
                self._teacher_list.remove(teacher)

    def find(self,id:str):
        for teacher in self._teacher_list
            if(teacher.id == id):
                return True
        return False

class subject_manager:
    def __init__(self,subject_list: list[subject])
        self._subject_list:list[subject] = subject_list

    def add(self,new_data:subject):
        self._subject_list.append(new_data)

    def remove(self,code:str):
        for subject in self._subject_list:
            if(subject.code == code):
                self._subject_list.remove(subject)

    def update(self,code:str,new_data:subject):
        for subject in self._subject_list:
            if(subject.code == code):
                subject == new_data

    def find(self,code:str):
        for subject in self._subject_list:
            if(subject.code == code):
                return True
        return False

class report_manager:

    def __init__(self,report_list: list[report]):
        self._report_list:list[report] = report_list

    def add(self,new_data: report):
        self._report_list.append(new_data)

    def remove(self,id:str,type:str):
        for report in self._report_list:
            if(report.id == id and report.type == type):
                self._report_list.remove(report)
    
    def update(self,id:str,type:str,new_data:report):
        for report in self._report_list:
            if(report.id == id and report.type == type):
                report = new_data

    def find(self,id:str,type:str):
        for report in self._report_list:
            if(report.id == id and report.type == type):
                return True
        return False      

class student_manager:

    def __init__(self,student_list: list[student]):
        self._student_list:list[student] = student_list

    def add(self,new_data: student):
        self._student_list.append(new_data)

    def add_guardian(self,id:str,new_data:guardian):
        for student in self._student_list:
            if(student.id == id):
                student.guardians.append(new_data)

    def add_grades(self,id:str,new_data:grade):
        for student in self._student_list:
            if(student.id == id):
                student.grades.append(new_data)

    def add_exams(self,id:str,new_data:exam):
        for student in self._student_list:
            if(student.id == id):
                student.exams.append(new_data)

    def add_set(self,id:str,set_level:str,new_data:set):
        for student in self._student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        exam.set.append(new_data)

    def add_test(self,id:str,set_level:str,set_title,new_data:test):
        for student in self._student_list:
            if(student.id == id):   
                for exam in student.exams:
                    if(exam.level == set_level):
                        for set in exam.set:
                            if(set.title == set_title):
                                set.append(test)
                                

    def remove(self,id:str):
        for student in self._student_list:
            if(student.id == id):
                self._student_list.remove(student)

    def update(self,id:str,new_data:student):
        for student in self._student_list:
            if(student.id == id):
                student == new_data

    def find(self,id:str):
        for student in self._student_list:
            if(student.id == id):
                return True
        return False

