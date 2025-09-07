
from src.ui_logic.ui_logic import *


def read(fil_name: str) -> SupervisedData:
    with open(fil_name, 'r') as file:
        file_content = file.read()
        name: str = file_content[0]
        value: int = int(file_content[1])
        data = SupervisedData(name, value)
        return data
