from Grade import grade

class test:

    def __init__(self):
        self._set_name:str = None
        self._set_tests:list = list()
        self._grades:list = list()
        self._grades_name:str = None

    @property
    def set_name(self) -> str:
        return self._set_name

    @property
    def grades_name(self) -> str:
        return self._grades_name

    @property
    def grades(self) -> list:
        return self._grades
    
    @property
    def full_data(self) -> dict:
        return {'set-test':self._set_name,self._grades_name:self._grades}

    def add_grade(self,value: grade) -> None:
        self._grades.append(value.full_data)

    def add_set_test(self,test: dict) -> None:
        self._set_tests.append(test)

    def define(self,set_name: str,grades: list) -> None:
        self._set_name = set_name
        self._grades = grades

    def __rpr__(self):
        return f'test[set_test = {self._set_name},grades = {self._grades}]'

    def __str__(self):
        return f'test[set_test = {self._set_name},grades = {self._grades}]'

       
