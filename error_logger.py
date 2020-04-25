import sys
from datetime import datetime


class ErrorLogger:
    def __init__(self, file: str):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        if type(value) == type("string"):
            self.__file = value
        else:
            raise Exception(f"ValueError: File should be an str not {type(value).__name__}")

    def get_error(self, e: Exception):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        now_time = datetime.now()
        return f"""------- [{now_time}]:
        File: {__file__}
        [Error: {exc_type.__name__}]: {e} 
        Line: {exc_tb.tb_lineno}"""

    def save(self, e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        now_time = datetime.now()
        error_text = f"""------- [{now_time}]:
        File: {__file__}
        [Error: {exc_type.__name__}]: {e} 
        Line: {exc_tb.tb_lineno}

"""
        with open(self.__file, "a") as file:
            file.write(error_text)
