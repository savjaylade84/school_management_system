import json

class db_connection:

    def __init__(self,file_path = "",data_path = ""):
        self._file_path:str
        self._data_path:str
        self._data:dict
        self._file_path = file_path
        self._data_path = data_path

    def connect(self) -> None:
        with open(file_path) as file:
            self._data = json.loads(file)

    @property
    def object(self) -> dict:
        return self._data