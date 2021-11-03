import json
import yaml
import Tools
from utils.Error import NoneError

def get_ui_link(ui_name:str) -> str:
   # if is_none(value): raise NoneError(f'settings.py : function - get_ui_link')
    with open('./desktop_gui/config/config.yaml') as file:
        temp_yaml = yaml.load(file,Loader=yaml.FullLoader)
    return f'{temp_yaml["ui_link"][ui_name]}'

