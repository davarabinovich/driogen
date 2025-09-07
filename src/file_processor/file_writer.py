
from src.ui_logic.ui_logic import *


def write(content: SupervisedData, file_name: str):
    with open(file_name, 'w') as file:
        file.write(content.name)
        file.write(str(content.value))
