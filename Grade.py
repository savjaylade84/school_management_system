from log import module_log

class grade:

    def __init__(self):
        self._subject:str = None
        self._score:int = None
        self._self._logger = module_log(log_name = 'grade.log',disable_log = False)

    @property
    def subject(self) -> str:
        self._logger.log.info(message = f'function subject -> {self._subject}')
        return self._subject

    @property
    def score(self) -> int:
        self._logger.log.info(message = f'function score -> {self._score}')
        return self._score

    @property
    def full_data(self) -> dict:
        self._logger.log.info(message = 'function full_data -> {0}'.format({'subject':self._subject,'score':self._score}))
        return {'subject':self._subject,'score':self._score}

    def define(value: dict) -> None:
        self._logger.log.info(message = f'function define <- {value}')
        self._subject, self._score = value

    def __rpr__(self):
        return f'grade[subject = {self._subject},score = {self._score}]'

    def __str__(self):
        return f'grade[subject = {self._subject},score = {self._score}]'

