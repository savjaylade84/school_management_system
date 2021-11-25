import json
import yaml
from utils.Tools import is_none
from utils.Error import NoneError

def get_ui_link(ui_name:str) -> str:
    if is_none(ui_name): raise NoneError(f'settings.py : function - get_ui_link')
    with open('./desktop_gui/config/settings.yaml') as file:
        temp_yaml = yaml.load(file,Loader=yaml.FullLoader)
    return f'{temp_yaml["gui-path-file"][ui_name]}'


class appearance:
    
    def __init__(self):
        with open('./desktop_gui/config/settings.yaml') as file:
            self._yaml = yaml.load(file,Loader=yaml.FullLoader)

    @property
    def dark_mode(self) -> dict:
        return self._yaml['appearance']['theme']['dark-mode']

    @property
    def light_mode(self) -> dict:
        return self._yaml['appearance']['theme']['light-mode']

    @property
    def font_size(self) -> str:
        return self._yaml['appearance']['font-size']

    @property
    def font_family(self) -> str:
        return self._yaml['appearance']['font-family']


