

""" 
    Author: John Jayson B. De Leon
    Email Address: savjaylade84@gmail.com
    Github: savjaylade
    Version: 1.10v
"""

from Student_Manager import student_manager
from Student import student

def init():
    data = student()
    students = student_manager('dummy_data.json',data)
    student_id = input('enter id: ')

    print(students.find_test(id = student_id,level = 'senior-high',test = 'first-quarter'))
    
       
    
    print('full-detail of data:',data)

if __name__ == '__main__':
    init()